"""
content_manager.py — CRUD de contenido lingüístico (palabras, frases, textos).

Los archivos Markdown son la fuente de verdad.
Cada entrada es un archivo .md dentro de library/<idioma>/<categoría>/.
"""

from pathlib import Path

from core.library_manager import get_language_path
from core.slug import make_slug


def list_entries(language: str, category: str) -> list[dict]:
    """
    Lista las entradas .md de una categoría de un idioma.

    Devuelve una lista de diccionarios con:
        - "title": título extraído del archivo (encabezado # o nombre del archivo)
        - "path": ruta absoluta al archivo (Path)
        - "filename": nombre del archivo sin extensión
    """
    folder = get_language_path(language) / category

    if not folder.exists():
        return []

    entries = []
    for filepath in sorted(folder.iterdir()):
        if filepath.suffix.lower() == '.md' and filepath.is_file():
            title = get_entry_title(filepath)
            entries.append({
                "title": title,
                "path": filepath,
                "filename": filepath.stem,
            })
    return entries


def get_entry_title(filepath: Path) -> str:
    """
    Extrae el título de un archivo .md.

    Busca la primera línea que empiece con '# '.
    Si no la encuentra, usa el nombre del archivo sin extensión.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
        # Si no hay encabezado, usar el nombre del archivo
        return filepath.stem.replace('-', ' ').title()
    except (OSError, UnicodeDecodeError):
        return filepath.stem


def read_entry(filepath: Path) -> str:
    """Lee y devuelve el contenido completo de un archivo .md."""
    try:
        return filepath.read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError):
        return ""


def save_word(language: str, word: str) -> Path:
    """
    Guarda una palabra como archivo .md.
    Devuelve la ruta del archivo creado.
    """
    slug = make_slug(word)
    folder = get_language_path(language) / "palabras"
    folder.mkdir(parents=True, exist_ok=True)

    filepath = _unique_filepath(folder, slug)

    content = f"# {word}\n\n{word}\n"
    filepath.write_text(content, encoding='utf-8')

    return filepath


def save_phrase(language: str, phrase: str) -> Path:
    """
    Guarda una frase como archivo .md.
    Devuelve la ruta del archivo creado.
    """
    slug = make_slug(phrase)
    folder = get_language_path(language) / "frases"
    folder.mkdir(parents=True, exist_ok=True)

    filepath = _unique_filepath(folder, slug)

    content = f"# {phrase}\n\n{phrase}\n"
    filepath.write_text(content, encoding='utf-8')

    return filepath


def save_text(language: str, title: str, body: str) -> Path:
    """
    Guarda un texto como archivo .md.
    Devuelve la ruta del archivo creado.
    """
    slug = make_slug(title)
    folder = get_language_path(language) / "textos"
    folder.mkdir(parents=True, exist_ok=True)

    filepath = _unique_filepath(folder, slug)

    content = f"# {title}\n\n{body}\n"
    filepath.write_text(content, encoding='utf-8')

    return filepath


def update_entry(filepath: Path, new_content: str) -> None:
    """
    Sobreescribe el contenido de un archivo .md existente.
    No crea un archivo nuevo.
    """
    filepath.write_text(new_content, encoding='utf-8')


def _unique_filepath(folder: Path, slug: str) -> Path:
    """
    Genera una ruta de archivo única dentro de la carpeta.
    Si el archivo ya existe, agrega un sufijo numérico.
    """
    filepath = folder / f"{slug}.md"

    if not filepath.exists():
        return filepath

    counter = 2
    while True:
        filepath = folder / f"{slug}-{counter}.md"
        if not filepath.exists():
            return filepath
        counter += 1
