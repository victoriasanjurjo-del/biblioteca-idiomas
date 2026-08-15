"""
Language Library — Punto de entrada de la aplicación.

Aplicación de escritorio personal para guardar y explorar
contenido lingüístico en diferentes idiomas.
Los datos se almacenan como archivos Markdown en una carpeta local.
"""

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

from ui.main_window import MainWindow
from ui.theme import build_stylesheet


def main():
    app = QApplication(sys.argv)

    # Tipografía base
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # Aplicar tema oscuro
    app.setStyleSheet(build_stylesheet())

    # Crear y mostrar la ventana principal
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
