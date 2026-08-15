"""
dialogs.py — Diálogos modales para crear idiomas, palabras, frases y textos.
"""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QComboBox, QPushButton,
)
from PySide6.QtCore import Qt

from ui.resources import UI_TEXT
from ui.theme import COLORS


class _BaseDialog(QDialog):
    """Base para todos los diálogos de creación."""

    def __init__(self, parent, title: str):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(420)
        self.setModal(True)

        # Layout principal
        self.layout_main = QVBoxLayout(self)
        self.layout_main.setSpacing(16)
        self.layout_main.setContentsMargins(24, 24, 24, 24)

        # Título del diálogo
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            font-size: 18px;
            font-weight: 600;
            color: {COLORS['accent']};
            margin-bottom: 8px;
        """)
        self.layout_main.addWidget(title_label)

    def _add_language_selector(self, languages: list[str]) -> QComboBox:
        """Agrega un selector de idioma al diálogo."""
        label = QLabel(UI_TEXT["dialog_word_language"])
        self.layout_main.addWidget(label)

        combo = QComboBox()
        for lang in languages:
            combo.addItem(lang)
        self.layout_main.addWidget(combo)
        return combo

    def _add_buttons(self):
        """Agrega botones Guardar/Cancelar."""
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        cancel_btn = QPushButton(UI_TEXT["cancel"])
        cancel_btn.setProperty("cssClass", "ghost")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        save_btn = QPushButton(UI_TEXT["save"])
        save_btn.setProperty("cssClass", "primary")
        save_btn.clicked.connect(self.accept)
        self.save_btn = save_btn
        button_layout.addWidget(save_btn)

        self.layout_main.addLayout(button_layout)


class NewLanguageDialog(_BaseDialog):
    """Diálogo para crear un idioma nuevo."""

    def __init__(self, parent):
        super().__init__(parent, UI_TEXT["dialog_language_title"])

        label = QLabel(UI_TEXT["dialog_language_prompt"])
        self.layout_main.addWidget(label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText(UI_TEXT["dialog_language_placeholder"])
        self.layout_main.addWidget(self.name_input)

        self.layout_main.addStretch()
        self._add_buttons()

        # Habilitar/deshabilitar el botón según el contenido
        self.save_btn.setEnabled(False)
        self.name_input.textChanged.connect(
            lambda text: self.save_btn.setEnabled(bool(text.strip()))
        )

    def get_name(self) -> str:
        return self.name_input.text().strip()


class NewWordDialog(_BaseDialog):
    """Diálogo para crear una palabra nueva."""

    def __init__(self, parent, languages: list[str], preselected: str = ""):
        super().__init__(parent, UI_TEXT["dialog_word_title"])

        self.language_combo = self._add_language_selector(languages)
        if preselected and preselected in languages:
            self.language_combo.setCurrentText(preselected)

        label = QLabel(UI_TEXT["dialog_word_prompt"])
        self.layout_main.addWidget(label)

        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText("Ej: perspicaz, serendipity, 美しい...")
        self.layout_main.addWidget(self.word_input)

        self.layout_main.addStretch()
        self._add_buttons()

        self.save_btn.setEnabled(False)
        self.word_input.textChanged.connect(
            lambda text: self.save_btn.setEnabled(bool(text.strip()))
        )

    def get_language(self) -> str:
        return self.language_combo.currentText()

    def get_word(self) -> str:
        return self.word_input.text().strip()


class NewPhraseDialog(_BaseDialog):
    """Diálogo para crear una frase nueva."""

    def __init__(self, parent, languages: list[str], preselected: str = ""):
        super().__init__(parent, UI_TEXT["dialog_phrase_title"])

        self.language_combo = self._add_language_selector(languages)
        if preselected and preselected in languages:
            self.language_combo.setCurrentText(preselected)

        label = QLabel(UI_TEXT["dialog_phrase_prompt"])
        self.layout_main.addWidget(label)

        self.phrase_input = QLineEdit()
        self.phrase_input.setPlaceholderText("Ej: Non ho voglia di uscire...")
        self.layout_main.addWidget(self.phrase_input)

        self.layout_main.addStretch()
        self._add_buttons()

        self.save_btn.setEnabled(False)
        self.phrase_input.textChanged.connect(
            lambda text: self.save_btn.setEnabled(bool(text.strip()))
        )

    def get_language(self) -> str:
        return self.language_combo.currentText()

    def get_phrase(self) -> str:
        return self.phrase_input.text().strip()


class NewTextDialog(_BaseDialog):
    """Diálogo para crear un texto nuevo."""

    def __init__(self, parent, languages: list[str], preselected: str = ""):
        super().__init__(parent, UI_TEXT["dialog_text_title"])

        self.language_combo = self._add_language_selector(languages)
        if preselected and preselected in languages:
            self.language_combo.setCurrentText(preselected)

        title_label = QLabel(UI_TEXT["dialog_text_title_field"])
        self.layout_main.addWidget(title_label)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Ej: Why I Like Programming...")
        self.layout_main.addWidget(self.title_input)

        body_label = QLabel(UI_TEXT["dialog_text_body"])
        self.layout_main.addWidget(body_label)

        self.body_input = QTextEdit()
        self.body_input.setMinimumHeight(150)
        self.body_input.setPlaceholderText("Escribe tu texto aquí...")
        self.layout_main.addWidget(self.body_input)

        self._add_buttons()

        self.save_btn.setEnabled(False)
        self.title_input.textChanged.connect(self._check_valid)
        self.body_input.textChanged.connect(self._check_valid)

    def _check_valid(self):
        has_title = bool(self.title_input.text().strip())
        has_body = bool(self.body_input.toPlainText().strip())
        self.save_btn.setEnabled(has_title and has_body)

    def get_language(self) -> str:
        return self.language_combo.currentText()

    def get_title(self) -> str:
        return self.title_input.text().strip()

    def get_body(self) -> str:
        return self.body_input.toPlainText()
