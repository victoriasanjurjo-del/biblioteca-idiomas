"""
content_list.py — Panel de contenido con pestañas (Palabras, Frases, Textos).

Muestra las entradas de un idioma seleccionado y permite crear nuevas.
"""

from pathlib import Path

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QTabWidget,
    QPushButton, QStackedWidget,
)
from PySide6.QtCore import Signal, Qt

from ui.resources import UI_TEXT, CATEGORY_WORDS, CATEGORY_PHRASES, CATEGORY_TEXTS
from ui.theme import COLORS


class ContentList(QWidget):
    """
    Panel con pestañas para Palabras, Frases y Textos de un idioma.
    Muestra las listas de entradas y botones para crear nuevas.
    """

    # Señales
    entry_selected = Signal(str, str, dict)  # (idioma, categoría, entry_dict)
    new_word_requested = Signal()
    new_phrase_requested = Signal()
    new_text_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_language: str | None = None

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Contenedor principal (stacked: mensaje de bienvenida / contenido)
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # --- Página 0: Mensaje de bienvenida ---
        welcome = QWidget()
        welcome_layout = QVBoxLayout(welcome)
        welcome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome_icon = QLabel("📖")
        welcome_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_icon.setStyleSheet("font-size: 48px; margin-bottom: 16px;")
        welcome_layout.addWidget(welcome_icon)

        welcome_text = QLabel(UI_TEXT["select_language"])
        welcome_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_text.setStyleSheet(f"""
            font-size: 15px;
            color: {COLORS['text_secondary']};
        """)
        welcome_layout.addWidget(welcome_text)

        self.stack.addWidget(welcome)

        # --- Página 1: Contenido del idioma ---
        content_page = QWidget()
        content_layout = QVBoxLayout(content_page)
        content_layout.setContentsMargins(16, 16, 16, 16)
        content_layout.setSpacing(12)

        # Encabezado del idioma
        self.language_header = QLabel()
        self.language_header.setStyleSheet(f"""
            font-size: 22px;
            font-weight: 700;
            color: {COLORS['text']};
            padding: 4px 0;
        """)
        content_layout.addWidget(self.language_header)

        # Pestañas
        self.tabs = QTabWidget()
        content_layout.addWidget(self.tabs)

        # Pestaña: Palabras
        self.words_tab = self._create_tab(
            UI_TEXT["new_word"],
            self.new_word_requested,
        )
        self.tabs.addTab(self.words_tab["widget"], UI_TEXT["tab_words"])

        # Pestaña: Frases
        self.phrases_tab = self._create_tab(
            UI_TEXT["new_phrase"],
            self.new_phrase_requested,
        )
        self.tabs.addTab(self.phrases_tab["widget"], UI_TEXT["tab_phrases"])

        # Pestaña: Textos
        self.texts_tab = self._create_tab(
            UI_TEXT["new_text"],
            self.new_text_requested,
        )
        self.tabs.addTab(self.texts_tab["widget"], UI_TEXT["tab_texts"])

        self.stack.addWidget(content_page)

        # Empezar con el mensaje de bienvenida
        self.stack.setCurrentIndex(0)

    def _create_tab(self, button_text: str, signal: Signal) -> dict:
        """Crea una pestaña con lista de entradas y botón de crear."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 8, 0, 0)
        layout.setSpacing(8)

        # Botón para crear nueva entrada
        btn_layout = QHBoxLayout()
        new_btn = QPushButton(button_text)
        new_btn.setProperty("cssClass", "primary")
        new_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        new_btn.clicked.connect(signal.emit)
        btn_layout.addWidget(new_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Lista de entradas
        entry_list = QListWidget()
        entry_list.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        layout.addWidget(entry_list)

        # Mensaje vacío
        empty_label = QLabel(UI_TEXT["no_entries"])
        empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_label.setStyleSheet(f"""
            color: {COLORS['text_dim']};
            font-size: 13px;
            padding: 40px 20px;
        """)
        layout.addWidget(empty_label)

        return {
            "widget": widget,
            "list": entry_list,
            "empty_label": empty_label,
        }

    def show_language(self, language: str, entries: dict[str, list[dict]]):
        """
        Muestra el contenido de un idioma.

        Args:
            language: Nombre del idioma.
            entries: Diccionario con listas de entradas por categoría.
                     {"palabras": [...], "frases": [...], "textos": [...]}
        """
        self._current_language = language
        self.language_header.setText(language)

        # Actualizar cada pestaña
        self._fill_tab(self.words_tab, language, CATEGORY_WORDS,
                       entries.get(CATEGORY_WORDS, []))
        self._fill_tab(self.phrases_tab, language, CATEGORY_PHRASES,
                       entries.get(CATEGORY_PHRASES, []))
        self._fill_tab(self.texts_tab, language, CATEGORY_TEXTS,
                       entries.get(CATEGORY_TEXTS, []))

        # Mostrar la página de contenido
        self.stack.setCurrentIndex(1)

    def _fill_tab(self, tab: dict, language: str, category: str,
                  entries: list[dict]):
        """Llena una pestaña con las entradas."""
        entry_list: QListWidget = tab["list"]
        empty_label: QLabel = tab["empty_label"]

        entry_list.clear()

        # Desconectar señales anteriores para evitar duplicados
        try:
            entry_list.itemDoubleClicked.disconnect()
        except RuntimeError:
            pass

        for entry in entries:
            item = QListWidgetItem(f"  {entry['title']}")
            item.setData(Qt.ItemDataRole.UserRole, entry)
            entry_list.addItem(item)

        has_entries = len(entries) > 0
        entry_list.setVisible(has_entries)
        empty_label.setVisible(not has_entries)

        # Conectar doble clic para abrir entradas
        entry_list.itemDoubleClicked.connect(
            lambda item, lang=language, cat=category: self._on_entry_clicked(
                item, lang, cat
            )
        )

    def _on_entry_clicked(self, item: QListWidgetItem, language: str,
                          category: str):
        entry_data = item.data(Qt.ItemDataRole.UserRole)
        if entry_data:
            self.entry_selected.emit(language, category, entry_data)

    def get_current_language(self) -> str | None:
        return self._current_language

    def show_welcome(self):
        """Vuelve al mensaje de bienvenida."""
        self._current_language = None
        self.stack.setCurrentIndex(0)
