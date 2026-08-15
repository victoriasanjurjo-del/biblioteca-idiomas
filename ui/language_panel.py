"""
language_panel.py — Panel lateral con la lista de idiomas.
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton,
)
from PySide6.QtCore import Signal, Qt

from ui.resources import UI_TEXT, get_flag
from ui.theme import COLORS


class LanguagePanel(QWidget):
    """Panel lateral que muestra los idiomas disponibles y permite crear nuevos."""

    # Señales
    language_selected = Signal(str)    # Emite el nombre del idioma seleccionado
    new_language_requested = Signal()  # Emite cuando se pide crear un idioma nuevo

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(200)
        self.setMaximumWidth(280)

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 16, 12, 12)
        layout.setSpacing(12)

        # Título de la aplicación
        app_title = QLabel(UI_TEXT["app_title"])
        app_title.setStyleSheet(f"""
            font-size: 20px;
            font-weight: 700;
            color: {COLORS['accent']};
            padding: 4px 0;
        """)
        layout.addWidget(app_title)

        # Botón nuevo idioma
        new_lang_btn = QPushButton(UI_TEXT["new_language"])
        new_lang_btn.setProperty("cssClass", "primary")
        new_lang_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        new_lang_btn.clicked.connect(self.new_language_requested.emit)
        layout.addWidget(new_lang_btn)

        # Separador visual
        separator = QLabel()
        separator.setFixedHeight(1)
        separator.setStyleSheet(f"background-color: {COLORS['border']};")
        layout.addWidget(separator)

        # Encabezado de idiomas
        header = QLabel(UI_TEXT["languages_header"])
        header.setStyleSheet(f"""
            font-size: 11px;
            font-weight: 600;
            color: {COLORS['text_dim']};
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 4px 0;
        """)
        layout.addWidget(header)

        # Lista de idiomas
        self.language_list = QListWidget()
        self.language_list.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.language_list.currentItemChanged.connect(self._on_selection_changed)
        layout.addWidget(self.language_list)

        # Mensaje cuando no hay idiomas
        self.empty_label = QLabel(UI_TEXT["no_languages"])
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_label.setStyleSheet(f"""
            color: {COLORS['text_dim']};
            font-size: 12px;
            padding: 20px;
        """)
        self.empty_label.setWordWrap(True)
        layout.addWidget(self.empty_label)

        # Estilo del panel
        self.setStyleSheet(f"""
            LanguagePanel {{
                background-color: {COLORS['bg_sidebar']};
                border-right: 1px solid {COLORS['border']};
            }}
        """)

    def set_languages(self, languages: list[str]):
        """Actualiza la lista de idiomas."""
        current_selection = self.get_selected_language()

        self.language_list.clear()

        for lang in languages:
            flag = get_flag(lang)
            item = QListWidgetItem(f"{flag}  {lang}")
            item.setData(Qt.ItemDataRole.UserRole, lang)
            self.language_list.addItem(item)

        # Mostrar/ocultar mensaje vacío
        has_languages = len(languages) > 0
        self.language_list.setVisible(has_languages)
        self.empty_label.setVisible(not has_languages)

        # Restaurar selección si existía
        if current_selection:
            self.select_language(current_selection)

    def select_language(self, name: str):
        """Selecciona un idioma por nombre."""
        for i in range(self.language_list.count()):
            item = self.language_list.item(i)
            if item.data(Qt.ItemDataRole.UserRole) == name:
                self.language_list.setCurrentItem(item)
                return

    def get_selected_language(self) -> str | None:
        """Devuelve el nombre del idioma seleccionado, o None."""
        item = self.language_list.currentItem()
        if item:
            return item.data(Qt.ItemDataRole.UserRole)
        return None

    def _on_selection_changed(self, current: QListWidgetItem, _previous):
        if current:
            lang_name = current.data(Qt.ItemDataRole.UserRole)
            self.language_selected.emit(lang_name)
