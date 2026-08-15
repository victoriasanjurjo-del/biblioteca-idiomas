"""
slug.py — Generación de nombres de archivo seguros.

Convierte texto arbitrario (incluido Unicode) en nombres de archivo
válidos para Windows, preservando la legibilidad.
"""

import re
import time


# Caracteres prohibidos en nombres de archivo de Windows
_WINDOWS_FORBIDDEN = re.compile(r'[<>:"/\\|?*]')

# Espacios y guiones múltiples
_MULTI_HYPHENS = re.compile(r'-{2,}')
_WHITESPACE = re.compile(r'\s+')

# Nombres reservados en Windows
_WINDOWS_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
}

MAX_SLUG_LENGTH = 80


def make_slug(text: str) -> str:
    """
    Convierte texto en un nombre de archivo seguro para Windows.

    - Reemplaza espacios por guiones.
    - Elimina caracteres prohibidos en Windows.
    - Preserva caracteres Unicode (japonés, griego, cirílico, etc.).
    - Limita la longitud a MAX_SLUG_LENGTH caracteres.
    - Si el resultado está vacío, genera un nombre basado en timestamp.

    Ejemplos:
        "Non ho voglia di uscire." → "non-ho-voglia-di-uscire"
        "perspicaz"                → "perspicaz"
        "日本語のテスト"             → "日本語のテスト"
        "Why I Like Programming"   → "why-i-like-programming"
    """
    slug = text.strip().lower()

    # Reemplazar espacios por guiones
    slug = _WHITESPACE.sub('-', slug)

    # Eliminar caracteres prohibidos en Windows
    slug = _WINDOWS_FORBIDDEN.sub('', slug)

    # Eliminar puntos al inicio y al final (problemáticos en Windows)
    slug = slug.strip('.')

    # Eliminar guiones múltiples
    slug = _MULTI_HYPHENS.sub('-', slug)

    # Eliminar guiones al inicio y al final
    slug = slug.strip('-')

    # Limitar longitud
    if len(slug) > MAX_SLUG_LENGTH:
        slug = slug[:MAX_SLUG_LENGTH].rstrip('-')

    # Si el slug es un nombre reservado de Windows, agregar sufijo
    if slug.upper() in _WINDOWS_RESERVED:
        slug = f"{slug}-file"

    # Si está vacío después de toda la limpieza, usar timestamp
    if not slug:
        slug = f"entry-{int(time.time())}"

    return slug
