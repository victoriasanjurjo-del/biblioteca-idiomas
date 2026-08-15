import sys
# pyrefly: ignore [missing-import]
from PySide6.QtCore import Qt
# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QInputDialog,
    QMessageBox,
    QLabel,
    QStackedWidget,
    QLineEdit,
    QFrame,
    QDialog,
    QFormLayout,
    QTextEdit,
    QComboBox,
    QScrollArea,
    QSizePolicy,
)

from language_library.database import (
    get_languages,
    add_language,
    get_entries,
    get_entry,
    add_entry,
    update_entry,
    get_word_families,
    add_word_family,
)
from language_library.ui.styles import APP_STYLESHEET


# ---------------------------------------------------------------------------
# Helper: dialog for adding / editing a full entry
# ---------------------------------------------------------------------------

class EntryDialog(QDialog):
    """Modal form for creating or editing a word entry."""

    def __init__(self, parent=None, title: str = "Entrada", entry: dict = None, is_spanish: bool = False):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(440)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(14)
        layout.setContentsMargins(24, 24, 24, 24)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignRight)

        # Word
        self.field_text = QLineEdit()
        self.field_text.setPlaceholderText("Escribe la palabra o expresión")
        form.addRow("Palabra:", self.field_text)

        # Pronunciation
        self.field_pronunciation = QLineEdit()
        self.field_pronunciation.setPlaceholderText("ej. /ko.ˈsi.na/")
        form.addRow("Pronunciación:", self.field_pronunciation)

        # Translation (hidden when the language itself is Spanish)
        self.field_translation = QLineEdit()
        self.field_translation.setPlaceholderText("Traducción al español")
        self._translation_row_label = QLabel("Traducción:")
        form.addRow(self._translation_row_label, self.field_translation)
        if is_spanish:
            self.field_translation.hide()
            self._translation_row_label.hide()

        # Definition
        self.field_definition = QTextEdit()
        self.field_definition.setPlaceholderText("Definición o descripción de la palabra")
        self.field_definition.setFixedHeight(90)
        form.addRow("Definición:", self.field_definition)

        # Word Family
        self.combo_family = QComboBox()
        self._load_families()
        form.addRow("Familia de palabras:", self.combo_family)

        layout.addLayout(form)

        # Button to add a new word family inline
        self.btn_new_family = QPushButton("+ Nueva familia de palabras")
        self.btn_new_family.setObjectName("secondaryBtn")
        self.btn_new_family.clicked.connect(self._add_new_family)
        layout.addWidget(self.btn_new_family)

        # Divider
        line = QFrame()
        line.setObjectName("dividerLine")
        line.setFixedHeight(1)
        layout.addWidget(line)

        # Accept / Cancel buttons
        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setObjectName("secondaryBtn")
        self.btn_accept = QPushButton("Guardar")
        self.btn_accept.setObjectName("primaryBtn")
        btn_row.addStretch()
        btn_row.addWidget(self.btn_cancel)
        btn_row.addWidget(self.btn_accept)
        layout.addLayout(btn_row)

        self.btn_cancel.clicked.connect(self.reject)
        self.btn_accept.clicked.connect(self.accept)

        # Pre-fill if editing
        if entry:
            self.field_text.setText(entry.get("text", ""))
            self.field_pronunciation.setText(entry.get("pronunciation") or "")
            self.field_translation.setText(entry.get("translation") or "")
            self.field_definition.setPlainText(entry.get("definition") or "")
            wf_id = entry.get("word_family_id")
            if wf_id is not None:
                idx = self.combo_family.findData(wf_id)
                if idx >= 0:
                    self.combo_family.setCurrentIndex(idx)

    def _load_families(self):
        self.combo_family.clear()
        self.combo_family.addItem("— Sin familia —", None)
        for fam in get_word_families():
            self.combo_family.addItem(fam["name"], fam["id"])

    def _add_new_family(self):
        name, ok = QInputDialog.getText(self, "Nueva Familia", "Nombre de la familia de palabras:")
        if not ok or not name.strip():
            return
        fam_id = add_word_family(name.strip())
        if fam_id is None:
            QMessageBox.warning(self, "Error", f"Ya existe una familia llamada '{name.strip()}' o no se pudo crear.")
            return
        self._load_families()
        idx = self.combo_family.findData(fam_id)
        if idx >= 0:
            self.combo_family.setCurrentIndex(idx)

    # --- Result accessors ---
    def get_text(self) -> str:
        return self.field_text.text().strip()

    def get_pronunciation(self) -> str:
        return self.field_pronunciation.text().strip()

    def get_translation(self) -> str:
        return self.field_translation.text().strip()

    def get_definition(self) -> str:
        return self.field_definition.toPlainText().strip()

    def get_word_family_id(self):
        return self.combo_family.currentData()


# ---------------------------------------------------------------------------
# Helper: dialog for adding a language (with family)
# ---------------------------------------------------------------------------

class LanguageDialog(QDialog):
    """Modal form for creating a new language with an optional family."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo Idioma")
        self.setMinimumWidth(380)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(14)
        layout.setContentsMargins(24, 24, 24, 24)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignRight)

        self.field_name = QLineEdit()
        self.field_name.setPlaceholderText("ej. Japonés")
        form.addRow("Idioma:", self.field_name)

        self.field_family = QLineEdit()
        self.field_family.setPlaceholderText("ej. Japónico, Romance, Germánico…")
        form.addRow("Familia lingüística:", self.field_family)

        layout.addLayout(form)

        line = QFrame()
        line.setObjectName("dividerLine")
        line.setFixedHeight(1)
        layout.addWidget(line)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setObjectName("secondaryBtn")
        self.btn_accept = QPushButton("Crear idioma")
        self.btn_accept.setObjectName("primaryBtn")
        btn_row.addStretch()
        btn_row.addWidget(self.btn_cancel)
        btn_row.addWidget(self.btn_accept)
        layout.addLayout(btn_row)

        self.btn_cancel.clicked.connect(self.reject)
        self.btn_accept.clicked.connect(self.accept)

    def get_name(self) -> str:
        return self.field_name.text().strip()

    def get_language_family(self) -> str:
        return self.field_family.text().strip()


# ---------------------------------------------------------------------------
# Main Window
# ---------------------------------------------------------------------------

class LanguageLibraryWindow(QMainWindow):
    """Main application window handling language list, entries, and word detail."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Library")
        self.resize(820, 580)
        self.setMinimumSize(650, 460)

        # Apply global theme stylesheet
        self.setStyleSheet(APP_STYLESHEET)

        self.current_language_id = None
        self.current_language_name = None
        self.current_language_family = None
        self.current_entry_id = None

        self.all_languages = []
        self.all_entries = []

        # Central container
        central_container = QWidget()
        central_container.setObjectName("centralWidget")
        main_layout = QVBoxLayout(central_container)
        main_layout.setContentsMargins(28, 24, 28, 24)
        main_layout.setSpacing(16)
        self.setCentralWidget(central_container)

        # Stacked widget for navigation between views
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        self._setup_language_view()   # index 0
        self._setup_entries_view()    # index 1
        self._setup_word_detail_view()  # index 2

        self.stack.setCurrentIndex(0)
        self.refresh_language_list()

    # -----------------------------------------------------------------------
    # Vista 1: Lista de Idiomas
    # -----------------------------------------------------------------------

    def _setup_language_view(self):
        self.lang_page = QWidget()
        layout = QVBoxLayout(self.lang_page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)

        header_box = QVBoxLayout()
        header_box.setSpacing(2)
        title = QLabel("Colección de Idiomas")
        title.setObjectName("headerTitle")
        subtitle = QLabel("Explora y gestiona tus bibliotecas de expresiones y vocabulario.")
        subtitle.setObjectName("headerSubtitle")
        header_box.addWidget(title)
        header_box.addWidget(subtitle)
        layout.addLayout(header_box)

        self.lang_search = QLineEdit()
        self.lang_search.setObjectName("searchBar")
        self.lang_search.setPlaceholderText("🔍 Buscar idioma...")
        self.lang_search.textChanged.connect(self._filter_languages)
        layout.addWidget(self.lang_search)

        self.lang_list = QListWidget()
        layout.addWidget(self.lang_list)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        self.btn_add_lang = QPushButton("+ Nuevo idioma")
        self.btn_add_lang.setObjectName("primaryBtn")
        self.btn_open_lang = QPushButton("Abrir biblioteca →")
        self.btn_open_lang.setObjectName("secondaryBtn")
        btn_layout.addWidget(self.btn_add_lang)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_open_lang)
        layout.addLayout(btn_layout)

        self.btn_add_lang.clicked.connect(self.add_language_dialog)
        self.btn_open_lang.clicked.connect(self.open_selected_language)
        self.lang_list.itemDoubleClicked.connect(self.open_language_item)

        self.stack.addWidget(self.lang_page)

    # -----------------------------------------------------------------------
    # Vista 2: Lista de Entradas de un Idioma
    # -----------------------------------------------------------------------

    def _setup_entries_view(self):
        self.entry_page = QWidget()
        layout = QVBoxLayout(self.entry_page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)

        header_box = QVBoxLayout()
        header_box.setSpacing(2)
        self.entry_header = QLabel("Entradas")
        self.entry_header.setObjectName("headerTitle")
        self.entry_subtitle = QLabel("Frases, palabras y expresiones registradas.")
        self.entry_subtitle.setObjectName("headerSubtitle")
        header_box.addWidget(self.entry_header)
        header_box.addWidget(self.entry_subtitle)
        layout.addLayout(header_box)

        self.entry_search = QLineEdit()
        self.entry_search.setObjectName("searchBar")
        self.entry_search.setPlaceholderText("🔍 Buscar en las expresiones...")
        self.entry_search.textChanged.connect(self._filter_entries)
        layout.addWidget(self.entry_search)

        self.entry_list = QListWidget()
        layout.addWidget(self.entry_list)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        self.btn_back = QPushButton("← Volver a Idiomas")
        self.btn_back.setObjectName("secondaryBtn")
        self.btn_edit_entry = QPushButton("Editar seleccionada")
        self.btn_edit_entry.setObjectName("earthBtn")
        self.btn_add_entry = QPushButton("+ Agregar entrada")
        self.btn_add_entry.setObjectName("primaryBtn")
        btn_layout.addWidget(self.btn_back)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_edit_entry)
        btn_layout.addWidget(self.btn_add_entry)
        layout.addLayout(btn_layout)

        self.btn_back.clicked.connect(self.show_language_view)
        self.btn_add_entry.clicked.connect(self.add_entry_dialog)
        self.btn_edit_entry.clicked.connect(self.edit_selected_entry)
        # Double-click → go to word detail view
        self.entry_list.itemDoubleClicked.connect(self.open_entry_item)

        self.stack.addWidget(self.entry_page)

    # -----------------------------------------------------------------------
    # Vista 3: Detalle de Palabra
    # -----------------------------------------------------------------------

    def _setup_word_detail_view(self):
        self.word_page = QWidget()
        outer = QVBoxLayout(self.word_page)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # Make it scrollable in case the window is small
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        outer.addWidget(scroll)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        scroll.setWidget(container)

        # --- 4 Info Cards row ---
        cards_row = QHBoxLayout()
        cards_row.setSpacing(12)

        self.card_id      = self._make_info_card("🔑", "ID")
        self.card_lang    = self._make_info_card("🌐", "Idioma")
        self.card_lfamily = self._make_info_card("🧬", "Familia lingüística")
        self.card_wfamily = self._make_info_card("📂", "Familia de palabras")

        for card in (self.card_id, self.card_lang, self.card_lfamily, self.card_wfamily):
            cards_row.addWidget(card)

        layout.addLayout(cards_row)

        # --- Divider ---
        div = QFrame()
        div.setObjectName("dividerLine")
        div.setFixedHeight(1)
        layout.addWidget(div)

        # --- Central word info (vertically centered in remaining space) ---
        # Wrap in a widget that fills and centers vertically
        center_wrapper = QWidget()
        center_wrapper.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        center_vbox = QVBoxLayout(center_wrapper)
        center_vbox.setContentsMargins(40, 32, 40, 16)
        center_vbox.setSpacing(0)
        center_vbox.addStretch(1)

        center_layout = QVBoxLayout()
        center_layout.setSpacing(0)
        center_layout.setAlignment(Qt.AlignHCenter)

        # Word
        self.lbl_word = QLabel("—")
        self.lbl_word.setObjectName("wordMain")
        self.lbl_word.setAlignment(Qt.AlignCenter)
        self.lbl_word.setWordWrap(True)
        center_layout.addWidget(self.lbl_word)

        # Pronunciation (shown only when available)
        self.lbl_pronunciation = QLabel("")
        self.lbl_pronunciation.setObjectName("wordPronunciation")
        self.lbl_pronunciation.setAlignment(Qt.AlignCenter)
        self.lbl_pronunciation.setWordWrap(True)
        center_layout.addWidget(self.lbl_pronunciation)

        # Spacer between word and translation
        spacer_1 = QWidget()
        spacer_1.setFixedHeight(20)
        spacer_1.setObjectName("transparentSpacer")
        center_layout.addWidget(spacer_1)

        # Thin decorative divider
        mini_div_1 = QFrame()
        mini_div_1.setObjectName("miniDivider")
        mini_div_1.setFixedHeight(1)
        mini_div_1.setMaximumWidth(200)
        mini_div_1_container = QHBoxLayout()
        mini_div_1_container.addStretch()
        mini_div_1_container.addWidget(mini_div_1)
        mini_div_1_container.addStretch()
        center_layout.addLayout(mini_div_1_container)

        spacer_2 = QWidget()
        spacer_2.setFixedHeight(12)
        spacer_2.setObjectName("transparentSpacer")
        center_layout.addWidget(spacer_2)

        # Translation section
        self.lbl_translation_label = QLabel("TRADUCCIÓN AL ESPAÑOL")
        self.lbl_translation_label.setObjectName("wordTranslationLabel")
        self.lbl_translation_label.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(self.lbl_translation_label)

        spacer_3 = QWidget()
        spacer_3.setFixedHeight(4)
        spacer_3.setObjectName("transparentSpacer")
        center_layout.addWidget(spacer_3)

        self.lbl_translation = QLabel("")
        self.lbl_translation.setObjectName("wordTranslation")
        self.lbl_translation.setAlignment(Qt.AlignCenter)
        self.lbl_translation.setWordWrap(True)
        center_layout.addWidget(self.lbl_translation)

        spacer_4 = QWidget()
        spacer_4.setFixedHeight(20)
        spacer_4.setObjectName("transparentSpacer")
        center_layout.addWidget(spacer_4)

        # Definition section
        self.lbl_definition_label = QLabel("DEFINICIÓN")
        self.lbl_definition_label.setObjectName("wordDefinitionLabel")
        self.lbl_definition_label.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(self.lbl_definition_label)

        spacer_5 = QWidget()
        spacer_5.setFixedHeight(4)
        spacer_5.setObjectName("transparentSpacer")
        center_layout.addWidget(spacer_5)

        self.lbl_definition = QLabel("")
        self.lbl_definition.setObjectName("wordDefinition")
        self.lbl_definition.setAlignment(Qt.AlignCenter)
        self.lbl_definition.setWordWrap(True)
        center_layout.addWidget(self.lbl_definition)

        center_vbox.addLayout(center_layout)
        center_vbox.addStretch(1)
        layout.addWidget(center_wrapper)

        # --- Bottom action bar ---
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        btn_layout.setContentsMargins(0, 12, 0, 0)
        self.btn_back_to_entries = QPushButton("← Volver a Entradas")
        self.btn_back_to_entries.setObjectName("secondaryBtn")
        self.btn_edit_word = QPushButton("Editar palabra")
        self.btn_edit_word.setObjectName("earthBtn")
        btn_layout.addWidget(self.btn_back_to_entries)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_edit_word)
        layout.addLayout(btn_layout)

        self.btn_back_to_entries.clicked.connect(self.show_entries_view)
        self.btn_edit_word.clicked.connect(self._edit_current_word)

        self.stack.addWidget(self.word_page)

    def _make_info_card(self, icon: str, label: str) -> QFrame:
        """Build a single info card widget (icon + label + value)."""
        card = QFrame()
        card.setObjectName("infoCard")
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 14, 16, 14)
        card_layout.setSpacing(4)

        lbl_icon = QLabel(icon)
        lbl_icon.setObjectName("cardIcon")
        lbl_icon.setAlignment(Qt.AlignLeft)

        lbl_label = QLabel(label.upper())
        lbl_label.setObjectName("cardLabel")
        lbl_label.setAlignment(Qt.AlignLeft)

        lbl_value = QLabel("—")
        lbl_value.setObjectName("cardValue")
        lbl_value.setAlignment(Qt.AlignLeft)
        lbl_value.setWordWrap(True)

        card_layout.addWidget(lbl_icon)
        card_layout.addWidget(lbl_label)
        card_layout.addWidget(lbl_value)

        # Store reference to value label for updating later
        card._value_label = lbl_value
        return card

    def _set_card_value(self, card: QFrame, value: str):
        card._value_label.setText(value or "—")

    # -----------------------------------------------------------------------
    # Vista 1 handlers
    # -----------------------------------------------------------------------

    def refresh_language_list(self):
        self.all_languages = get_languages()
        self._filter_languages()

    def _filter_languages(self):
        query = self.lang_search.text().strip().lower()
        self.lang_list.clear()
        filtered = [
            row for row in self.all_languages
            if not query or query in row["name"].lower()
        ]
        for row in filtered:
            item = QListWidgetItem(f"📚  {row['name']}")
            item.setData(Qt.UserRole, row["id"])
            self.lang_list.addItem(item)

        if not filtered and self.all_languages:
            empty_item = QListWidgetItem("No se encontraron idiomas que coincidan.")
            empty_item.setFlags(Qt.NoItemFlags)
            self.lang_list.addItem(empty_item)
        elif not self.all_languages:
            empty_item = QListWidgetItem("No hay idiomas creados aún. Haz clic en '+ Nuevo idioma' para comenzar.")
            empty_item.setFlags(Qt.NoItemFlags)
            self.lang_list.addItem(empty_item)

    def add_language_dialog(self):
        dlg = LanguageDialog(self)
        if dlg.exec() != QDialog.Accepted:
            return
        name = dlg.get_name()
        language_family = dlg.get_language_family()
        if not name:
            QMessageBox.warning(self, "Error", "El nombre del idioma no puede estar vacío.")
            return
        lang_id = add_language(name, language_family)
        if lang_id is None:
            QMessageBox.warning(self, "Error", f"No se pudo crear. Ya existe un idioma llamado '{name}' o ocurrió un error.")
            return
        self.refresh_language_list()

    def open_selected_language(self):
        current_item = self.lang_list.currentItem()
        if not current_item or not current_item.flags() & Qt.ItemIsEnabled:
            QMessageBox.information(self, "Atención", "Por favor, selecciona un idioma de la lista.")
            return
        self.open_language_item(current_item)

    def open_language_item(self, item: QListWidgetItem):
        lang_id = item.data(Qt.UserRole)
        if lang_id is None:
            return
        # Find full language data (including family)
        lang_data = next((r for r in self.all_languages if r["id"] == lang_id), None)
        self.current_language_id = lang_id
        self.current_language_name = item.text().replace("📚  ", "")
        self.current_language_family = lang_data["language_family"] if lang_data else None
        self.entry_header.setText(f"Idioma: {self.current_language_name}")
        self.entry_subtitle.setText(f"Explora y gestiona el contenido de {self.current_language_name}.")
        self.entry_search.clear()
        self.refresh_entries_list()
        self.stack.setCurrentIndex(1)

    # -----------------------------------------------------------------------
    # Vista 2 handlers
    # -----------------------------------------------------------------------

    def refresh_entries_list(self):
        if self.current_language_id is None:
            self.all_entries = []
        else:
            self.all_entries = get_entries(self.current_language_id)
        self._filter_entries()

    def _filter_entries(self):
        query = self.entry_search.text().strip().lower()
        self.entry_list.clear()
        filtered = [
            row for row in self.all_entries
            if not query or query in row["text"].lower()
        ]
        for row in filtered:
            item = QListWidgetItem(row["text"])
            item.setData(Qt.UserRole, row["id"])
            self.entry_list.addItem(item)

        if not filtered and self.all_entries:
            empty_item = QListWidgetItem("No se encontraron entradas que coincidan con la búsqueda.")
            empty_item.setFlags(Qt.NoItemFlags)
            self.entry_list.addItem(empty_item)
        elif not self.all_entries:
            empty_item = QListWidgetItem("Aún no hay entradas en este idioma. Usa '+ Agregar entrada'.")
            empty_item.setFlags(Qt.NoItemFlags)
            self.entry_list.addItem(empty_item)

    def add_entry_dialog(self):
        if self.current_language_id is None:
            return
        is_spanish = (self.current_language_name or "").strip().lower() == "español"
        dlg = EntryDialog(self, title="Agregar Entrada", is_spanish=is_spanish)
        if dlg.exec() != QDialog.Accepted:
            return
        text = dlg.get_text()
        if not text:
            QMessageBox.warning(self, "Error", "La entrada no puede estar vacía.")
            return
        entry_id = add_entry(
            self.current_language_id,
            text,
            dlg.get_pronunciation(),
            dlg.get_translation(),
            dlg.get_definition(),
            dlg.get_word_family_id(),
        )
        if entry_id is None:
            QMessageBox.warning(self, "Error", "No se pudo guardar la entrada.")
            return
        self.refresh_entries_list()

    def edit_selected_entry(self):
        current_item = self.entry_list.currentItem()
        if not current_item or not current_item.flags() & Qt.ItemIsEnabled:
            QMessageBox.information(self, "Atención", "Por favor, selecciona una entrada de la lista.")
            return
        self._open_edit_dialog(current_item.data(Qt.UserRole))

    def open_entry_item(self, item: QListWidgetItem):
        """Double-click → navigate to word detail view."""
        entry_id = item.data(Qt.UserRole)
        if entry_id is None:
            return
        self._show_word_detail(entry_id)

    def _open_edit_dialog(self, entry_id: int):
        row = get_entry(entry_id)
        if row is None:
            return
        is_spanish = (self.current_language_name or "").strip().lower() == "español"
        dlg = EntryDialog(
            self,
            title="Editar Entrada",
            entry=dict(row),
            is_spanish=is_spanish,
        )
        if dlg.exec() != QDialog.Accepted:
            return
        new_text = dlg.get_text()
        if not new_text:
            QMessageBox.warning(self, "Error", "La entrada no puede estar vacía.")
            return
        success = update_entry(
            entry_id,
            new_text,
            dlg.get_pronunciation(),
            dlg.get_translation(),
            dlg.get_definition(),
            dlg.get_word_family_id(),
        )
        if not success:
            QMessageBox.warning(self, "Error", "No se pudo actualizar la entrada.")
            return
        self.refresh_entries_list()
        # If we're coming back from the detail view, refresh it too
        if self.current_entry_id == entry_id:
            self._show_word_detail(entry_id)

    # -----------------------------------------------------------------------
    # Vista 3 handlers
    # -----------------------------------------------------------------------

    def _show_word_detail(self, entry_id: int):
        row = get_entry(entry_id)
        if row is None:
            return
        self.current_entry_id = entry_id

        # Populate 4 cards
        self._set_card_value(self.card_id,      f"WRD-{entry_id:04d}")
        self._set_card_value(self.card_lang,    self.current_language_name or "—")
        self._set_card_value(self.card_lfamily, self.current_language_family or "—")
        self._set_card_value(self.card_wfamily, row["word_family_name"] or "—")

        # Populate central word info
        self.lbl_word.setText(row["text"] or "—")
        self.lbl_pronunciation.setText(row["pronunciation"] or "")
        self.lbl_translation.setText(row["translation"] or "—")
        self.lbl_definition.setText(row["definition"] or "—")

        # Show/hide pronunciation line
        self.lbl_pronunciation.setVisible(bool(row["pronunciation"]))

        # Hide translation section when the language is Spanish
        is_spanish = (self.current_language_name or "").strip().lower() == "español"
        self.lbl_translation_label.setVisible(not is_spanish)
        self.lbl_translation.setVisible(not is_spanish)

        self.stack.setCurrentIndex(2)

    def _edit_current_word(self):
        if self.current_entry_id is not None:
            self._open_edit_dialog(self.current_entry_id)
            # After editing, refresh the detail view
            self._show_word_detail(self.current_entry_id)

    def show_entries_view(self):
        self.current_entry_id = None
        self.stack.setCurrentIndex(1)

    def show_language_view(self):
        self.current_language_id = None
        self.current_language_name = None
        self.current_language_family = None
        self.lang_search.clear()
        self.stack.setCurrentIndex(0)
        self.refresh_language_list()
