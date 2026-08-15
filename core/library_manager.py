"""
library_manager.py — Gestión de la biblioteca de idiomas.

Se encarga de crear y listar la estructura de carpetas:
    library/
    ├── <idioma>/
    │   ├── palabras/
    │   ├── frases/
    │   └── textos/
"""

from pathlib import Path


# Subcarpetas que se crean para cada idioma
CATEGORIES = ("palabras", "frases", "textos")


def get_library_path() -> Path:
    """Devuelve la ruta absoluta de la carpeta library/ (relativa al proyecto)."""
    project_root = Path(__file__).resolve().parent.parent
    return project_root / "library"


def ensure_library() -> Path:
    """Crea la carpeta library/ si no existe. Devuelve su ruta."""
    library_path = get_library_path()
    library_path.mkdir(exist_ok=True)
    return library_path


def list_languages() -> list[str]:
    """
    Lista los idiomas disponibles (subcarpetas de library/).
    Devuelve una lista ordenada de nombres.
    """
    library_path = get_library_path()
    if not library_path.exists():
        return []

    languages = []
    for item in sorted(library_path.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            languages.append(item.name)
    return languages


def create_language(name: str) -> Path:
    """
    Crea un idioma nuevo con sus subcarpetas (palabras, frases, textos).
    Devuelve la ruta de la carpeta del idioma.
    """
    library_path = ensure_library()
    language_path = library_path / name

    for category in CATEGORIES:
        (language_path / category).mkdir(parents=True, exist_ok=True)

    return language_path


def get_language_path(name: str) -> Path:
    """Devuelve la ruta de la carpeta de un idioma."""
    return get_library_path() / name
