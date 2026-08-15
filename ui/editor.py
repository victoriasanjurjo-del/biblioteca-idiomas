"""
editor.py — Editor/visor de contenido Markdown.

Permite leer y editar el contenido de un archivo .md como texto plano.
"""

from pathlib import Path

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QTextEdit, QPushButton,
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont

from ui.resources import UI_TEXT
from ui.theme import COLORS
from core.content_manager import read_entry, update_entry


class Editor(QWidget):
    """
    Editor de texto plano para contenido Markdown.
    Muestra el contenido de un archivo .md y permite editarlo.
    """

    # Señales
    back_requested = Signal()  # Emite cuando se pulsa "Volver"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_filepath: Path | None = None
        self._current_language: str = ""
        self._current_category: str = ""

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # --- Barra superior ---
        toolbar = QHBoxLayout()

        back_btn = QPushButton(UI_TEXT["back"])
        back_btn.setProperty("cssClass", "ghost")
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.clicked.connect(self.back_requested.emit)
        toolbar.addWidget(back_btn)

        toolbar.addStretch()

        # Indicador de guardado
        self.save_status = QLabel()
        self.save_status.setStyleSheet(f"""
            color: {COLORS['success']};
            font-size: 12px;
        """)
        toolbar.addWidget(self.save_status)

        save_btn = QPushButton(UI_TEXT["save"])
        save_btn.setProperty("cssClass", "primary")
        save_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        save_btn.clicked.connect(self._save)
        toolbar.addWidget(save_btn)

        layout.addLayout(toolbar)

        # --- Encabezado ---
        self.header_label = QLabel()
        self.header_label.setStyleSheet(f"""
            font-size: 13px;
            color: {COLORS['text_dim']};
            padding: 4px 0;
        """)
        layout.addWidget(self.header_label)

        # Título del contenido
        self.title_label = QLabel()
        self.title_label.setStyleSheet(f"""
            font-size: 20px;
            font-weight: 700;
            color: {COLORS['text']};
            padding: 4px 0;
        """)
        self.title_label.setWordWrap(True)
        layout.addWidget(self.title_label)

        # Separador
        separator = QLabel()
        separator.setFixedHeight(1)
        separator.setStyleSheet(f"background-color: {COLORS['border']};")
        layout.addWidget(separator)

        # --- Editor de texto ---
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Consolas", 13))
        self.text_edit.setPlaceholderText("Contenido Markdown...")
        self.text_edit.setStyleSheet(f"""
            QTextEdit {{
                background-color: {COLORS['bg_input']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 8px;
                padding: 16px;
                font-size: 14px;
                line-height: 1.6;
            }}
            QTextEdit:focus {{
                border-color: {COLORS['border_focus']};
            }}
        """)
        layout.addWidget(self.text_edit)

        # Limpiar estado de guardado cuando el usuario edita
        self.text_edit.textChanged.connect(self._on_text_changed)

    def open_entry(self, language: str, category: str, entry: dict):
        """
        Abre una entrada para edición.

        Args:
            language: Nombre del idioma.
            category: Categoría (palabras, frases, textos).
            entry: Diccionario con title, path y filename.
        """
        self._current_filepath = entry["path"]
        self._current_language = language
        self._current_category = category

        # Encabezado: idioma > categoría
        self.header_label.setText(f"{language}  ›  {category}")

        # Título
        self.title_label.setText(entry["title"])

        # Contenido
        content = read_entry(entry["path"])
        self.text_edit.setPlainText(content)

        # Limpiar estado
        self.save_status.clear()

    def _save(self):
        """Guarda el contenido editado al archivo."""
        if not self._current_filepath:
            return

        content = self.text_edit.toPlainText()

        # Asegurar que termina con un salto de línea
        if content and not content.endswith('\n'):
            content += '\n'

        update_entry(self._current_filepath, content)

        # Actualizar título si cambió
        lines = content.strip().split('\n')
        for line in lines:
            if line.startswith('# '):
                self.title_label.setText(line[2:].strip())
                break

        self.save_status.setText(UI_TEXT["editor_saved"])

    def _on_text_changed(self):
        """Limpia el indicador de guardado cuando el texto cambia."""
        self.save_status.clear()

    def get_current_info(self) -> tuple[str, str] | None:
        """Devuelve (idioma, categoría) del contenido actual, o None."""
        if self._current_filepath:
            return (self._current_language, self._current_category)
        return None
