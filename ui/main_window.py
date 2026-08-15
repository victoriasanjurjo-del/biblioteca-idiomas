"""
main_window.py — Ventana principal de Language Library.

Ensambla el panel de idiomas, la lista de contenido y el editor
en un layout con QSplitter y QStackedWidget.
"""

from PySide6.QtWidgets import (
    QMainWindow, QSplitter, QStackedWidget,
    QStatusBar, QMessageBox,
)
from PySide6.QtCore import Qt

from core import library_manager, content_manager
from ui.language_panel import LanguagePanel
from ui.content_list import ContentList
from ui.editor import Editor
from ui.dialogs import (
    NewLanguageDialog, NewWordDialog, NewPhraseDialog, NewTextDialog,
)
from ui.resources import UI_TEXT, CATEGORY_WORDS, CATEGORY_PHRASES, CATEGORY_TEXTS


class MainWindow(QMainWindow):
    """Ventana principal de Language Library."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle(UI_TEXT["app_title"])
        self.setMinimumSize(900, 600)
        self.resize(1000, 700)

        # Asegurar que la biblioteca existe
        library_manager.ensure_library()

        self._setup_ui()
        self._connect_signals()
        self._refresh_languages()

    def _setup_ui(self):
        # --- Panel izquierdo: Idiomas ---
        self.language_panel = LanguagePanel()

        # --- Panel derecho: Contenido (stacked entre lista y editor) ---
        self.right_stack = QStackedWidget()

        # Página 0: Lista de contenido
        self.content_list = ContentList()
        self.right_stack.addWidget(self.content_list)

        # Página 1: Editor
        self.editor = Editor()
        self.right_stack.addWidget(self.editor)

        # Empezar mostrando la lista de contenido
        self.right_stack.setCurrentIndex(0)

        # --- Splitter principal ---
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.language_panel)
        splitter.addWidget(self.right_stack)
        splitter.setStretchFactor(0, 0)  # Panel izquierdo: tamaño fijo
        splitter.setStretchFactor(1, 1)  # Panel derecho: se expande

        self.setCentralWidget(splitter)

        # --- Barra de estado ---
        status_bar = QStatusBar()
        library_path = library_manager.get_library_path()
        status_bar.showMessage(f"{UI_TEXT['status_library']} {library_path}")
        self.setStatusBar(status_bar)

    def _connect_signals(self):
        # Panel de idiomas
        self.language_panel.language_selected.connect(self._on_language_selected)
        self.language_panel.new_language_requested.connect(self._on_new_language)

        # Lista de contenido
        self.content_list.entry_selected.connect(self._on_entry_selected)
        self.content_list.new_word_requested.connect(self._on_new_word)
        self.content_list.new_phrase_requested.connect(self._on_new_phrase)
        self.content_list.new_text_requested.connect(self._on_new_text)

        # Editor
        self.editor.back_requested.connect(self._on_editor_back)

    # ─── Eventos: Idiomas ───

    def _on_language_selected(self, language: str):
        """Se seleccionó un idioma en el panel lateral."""
        self._show_language_content(language)
        self.right_stack.setCurrentIndex(0)

    def _on_new_language(self):
        """El usuario quiere crear un idioma nuevo."""
        dialog = NewLanguageDialog(self)
        if dialog.exec():
            name = dialog.get_name()
            if name:
                library_manager.create_language(name)
                self._refresh_languages()
                self.language_panel.select_language(name)

    # ─── Eventos: Contenido ───

    def _on_entry_selected(self, language: str, category: str, entry: dict):
        """Se seleccionó una entrada para abrirla en el editor."""
        self.editor.open_entry(language, category, entry)
        self.right_stack.setCurrentIndex(1)

    def _on_new_word(self):
        """El usuario quiere crear una palabra nueva."""
        languages = library_manager.list_languages()
        if not languages:
            self._show_no_languages_message()
            return

        preselected = self.content_list.get_current_language() or ""
        dialog = NewWordDialog(self, languages, preselected)

        if dialog.exec():
            language = dialog.get_language()
            word = dialog.get_word()
            if language and word:
                content_manager.save_word(language, word)
                self._show_language_content(language)

    def _on_new_phrase(self):
        """El usuario quiere crear una frase nueva."""
        languages = library_manager.list_languages()
        if not languages:
            self._show_no_languages_message()
            return

        preselected = self.content_list.get_current_language() or ""
        dialog = NewPhraseDialog(self, languages, preselected)

        if dialog.exec():
            language = dialog.get_language()
            phrase = dialog.get_phrase()
            if language and phrase:
                content_manager.save_phrase(language, phrase)
                self._show_language_content(language)

    def _on_new_text(self):
        """El usuario quiere crear un texto nuevo."""
        languages = library_manager.list_languages()
        if not languages:
            self._show_no_languages_message()
            return

        preselected = self.content_list.get_current_language() or ""
        dialog = NewTextDialog(self, languages, preselected)

        if dialog.exec():
            language = dialog.get_language()
            title = dialog.get_title()
            body = dialog.get_body()
            if language and title and body:
                content_manager.save_text(language, title, body)
                self._show_language_content(language)

    # ─── Eventos: Editor ───

    def _on_editor_back(self):
        """El usuario quiere volver del editor a la lista."""
        # Refrescar la lista del idioma actual
        info = self.editor.get_current_info()
        if info:
            language, _category = info
            self._show_language_content(language)

        self.right_stack.setCurrentIndex(0)

    # ─── Helpers ───

    def _refresh_languages(self):
        """Recarga la lista de idiomas desde el sistema de archivos."""
        languages = library_manager.list_languages()
        self.language_panel.set_languages(languages)

    def _show_language_content(self, language: str):
        """Carga y muestra el contenido de un idioma."""
        entries = {
            CATEGORY_WORDS: content_manager.list_entries(language, CATEGORY_WORDS),
            CATEGORY_PHRASES: content_manager.list_entries(language, CATEGORY_PHRASES),
            CATEGORY_TEXTS: content_manager.list_entries(language, CATEGORY_TEXTS),
        }
        self.content_list.show_language(language, entries)

    def _show_no_languages_message(self):
        """Muestra un mensaje cuando no hay idiomas creados."""
        QMessageBox.information(
            self,
            "Sin idiomas",
            "Primero crea un idioma para poder agregar contenido.",
        )
