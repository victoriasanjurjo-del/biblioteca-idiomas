"""
resources.py — Constantes de UI: banderas emoji, textos de la interfaz.
"""

# Mapeo de nombres de idioma a emoji de bandera.
# Fallback: 📚
LANGUAGE_FLAGS: dict[str, str] = {
    "Español":    "🇪🇸",
    "español":    "🇪🇸",
    "English":    "🇬🇧",
    "english":    "🇬🇧",
    "Italiano":   "🇮🇹",
    "italiano":   "🇮🇹",
    "Deutsch":    "🇩🇪",
    "deutsch":    "🇩🇪",
    "Français":   "🇫🇷",
    "français":   "🇫🇷",
    "Português":  "🇵🇹",
    "português":  "🇵🇹",
    "日本語":      "🇯🇵",
    "中文":        "🇨🇳",
    "한국어":      "🇰🇷",
    "Русский":    "🇷🇺",
    "русский":    "🇷🇺",
    "العربية":    "🇸🇦",
    "Ελληνικά":   "🇬🇷",
    "ελληνικά":   "🇬🇷",
    "Nederlands": "🇳🇱",
    "Svenska":    "🇸🇪",
    "Norsk":      "🇳🇴",
    "Dansk":      "🇩🇰",
    "Suomi":      "🇫🇮",
    "Polski":     "🇵🇱",
    "Čeština":    "🇨🇿",
    "Türkçe":     "🇹🇷",
    "हिन्दी":       "🇮🇳",
    "Català":     "🔶",
    "Euskara":    "🔶",
    "Galego":     "🔶",
}

DEFAULT_FLAG = "📚"


def get_flag(language_name: str) -> str:
    """Devuelve el emoji de bandera para un idioma, o el fallback 📚."""
    return LANGUAGE_FLAGS.get(language_name, DEFAULT_FLAG)


# Textos de la interfaz (español)
UI_TEXT = {
    "app_title":        "Language Library",
    "new_language":     "＋ Nuevo idioma",
    "new_word":         "＋ Nueva palabra",
    "new_phrase":       "＋ Nueva frase",
    "new_text":         "＋ Nuevo texto",

    "tab_words":        "Palabras",
    "tab_phrases":      "Frases",
    "tab_texts":        "Textos",

    "languages_header": "Idiomas",
    "no_languages":     "No hay idiomas todavía.\nCrea uno para empezar.",
    "no_entries":       "No hay entradas todavía.",

    "select_language":  "Selecciona un idioma para ver su contenido.",

    "save":             "Guardar",
    "back":             "← Volver",
    "cancel":           "Cancelar",

    "dialog_language_title":  "Nuevo idioma",
    "dialog_language_prompt": "Nombre del idioma:",
    "dialog_language_placeholder": "Ej: Español, English, 日本語...",

    "dialog_word_title":    "Nueva palabra",
    "dialog_word_prompt":   "Palabra:",
    "dialog_word_language": "Idioma:",

    "dialog_phrase_title":    "Nueva frase",
    "dialog_phrase_prompt":   "Frase:",
    "dialog_phrase_language": "Idioma:",

    "dialog_text_title":    "Nuevo texto",
    "dialog_text_title_field": "Título:",
    "dialog_text_body":     "Texto:",
    "dialog_text_language": "Idioma:",

    "editor_saved":     "✓ Guardado",

    "status_library":   "Biblioteca:",
}

# Nombres de categorías (para las carpetas)
CATEGORY_WORDS = "palabras"
CATEGORY_PHRASES = "frases"
CATEGORY_TEXTS = "textos"
