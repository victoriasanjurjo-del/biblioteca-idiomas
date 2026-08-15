import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

# Ensure root project directory is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from language_library.database import init_db
from language_library.ui.main_window import LanguageLibraryWindow


def main():
    # 1. Initialize SQLite Database & Tables
    init_db()

    # 2. Start Qt Application
    app = QApplication(sys.argv)
    window = LanguageLibraryWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
