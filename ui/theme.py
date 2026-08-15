"""
theme.py — Paleta de colores y estilos globales para Language Library.

Tema oscuro cálido con acentos en ámbar/dorado.
"""


# Paleta de colores
COLORS = {
    "bg_primary":    "#1a1a2e",   # Fondo principal
    "bg_sidebar":    "#16213e",   # Fondo panel lateral
    "bg_card":       "#0f3460",   # Fondo de tarjetas e items
    "bg_input":      "#1c2541",   # Fondo de campos de texto
    "bg_hover":      "#1a3a6a",   # Fondo al pasar el ratón
    "bg_selected":   "#0f3460",   # Fondo del item seleccionado
    "bg_tab":        "#16213e",   # Fondo de pestaña inactiva
    "bg_tab_active": "#1a1a2e",   # Fondo de pestaña activa

    "accent":        "#e2b714",   # Acento primario (ámbar)
    "accent_hover":  "#f0a500",   # Acento al pasar el ratón
    "accent_soft":   "#3a2f0a",   # Acento suave para fondos

    "text":          "#e0e0e0",   # Texto principal
    "text_secondary":"#a0a0b0",   # Texto secundario
    "text_dim":      "#6a6a8a",   # Texto tenue
    "text_accent":   "#e2b714",   # Texto con color de acento

    "border":        "#2a2a4a",   # Bordes sutiles
    "border_focus":  "#e2b714",   # Borde al enfocar

    "success":       "#4ade80",   # Verde para confirmaciones
    "error":         "#f87171",   # Rojo para errores
}


def build_stylesheet() -> str:
    """Genera la hoja de estilos QSS completa para la aplicación."""
    c = COLORS
    return f"""
    /* === Base === */
    QMainWindow, QDialog {{
        background-color: {c['bg_primary']};
        color: {c['text']};
    }}

    /* === Labels === */
    QLabel {{
        color: {c['text']};
        font-size: 13px;
    }}

    /* === Botones === */
    QPushButton {{
        background-color: {c['bg_card']};
        color: {c['text']};
        border: 1px solid {c['border']};
        border-radius: 6px;
        padding: 8px 16px;
        font-size: 13px;
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: {c['bg_hover']};
        border-color: {c['accent']};
    }}
    QPushButton:pressed {{
        background-color: {c['accent_soft']};
    }}

    /* Botón primario (acento) */
    QPushButton[cssClass="primary"] {{
        background-color: {c['accent']};
        color: #1a1a2e;
        border: none;
        font-weight: 600;
    }}
    QPushButton[cssClass="primary"]:hover {{
        background-color: {c['accent_hover']};
    }}

    /* Botón fantasma (solo texto) */
    QPushButton[cssClass="ghost"] {{
        background-color: transparent;
        border: none;
        color: {c['text_secondary']};
    }}
    QPushButton[cssClass="ghost"]:hover {{
        color: {c['accent']};
    }}

    /* === Campos de texto === */
    QLineEdit, QTextEdit, QPlainTextEdit {{
        background-color: {c['bg_input']};
        color: {c['text']};
        border: 1px solid {c['border']};
        border-radius: 6px;
        padding: 8px;
        font-size: 14px;
        selection-background-color: {c['accent_soft']};
        selection-color: {c['text']};
    }}
    QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
        border-color: {c['border_focus']};
    }}

    /* === Listas === */
    QListWidget {{
        background-color: transparent;
        border: none;
        outline: none;
        font-size: 14px;
    }}
    QListWidget::item {{
        color: {c['text']};
        padding: 10px 12px;
        border-radius: 6px;
        margin: 2px 4px;
    }}
    QListWidget::item:hover {{
        background-color: {c['bg_hover']};
    }}
    QListWidget::item:selected {{
        background-color: {c['bg_selected']};
        color: {c['accent']};
    }}

    /* === Pestañas === */
    QTabWidget::pane {{
        border: none;
        background-color: {c['bg_primary']};
    }}
    QTabBar::tab {{
        background-color: {c['bg_tab']};
        color: {c['text_secondary']};
        padding: 10px 20px;
        margin-right: 2px;
        border: none;
        border-bottom: 2px solid transparent;
        font-size: 13px;
        font-weight: 500;
    }}
    QTabBar::tab:selected {{
        background-color: {c['bg_tab_active']};
        color: {c['accent']};
        border-bottom: 2px solid {c['accent']};
    }}
    QTabBar::tab:hover:!selected {{
        color: {c['text']};
        background-color: {c['bg_hover']};
    }}

    /* === Splitter === */
    QSplitter::handle {{
        background-color: {c['border']};
        width: 1px;
    }}

    /* === ScrollBar === */
    QScrollBar:vertical {{
        background-color: transparent;
        width: 8px;
        margin: 0;
    }}
    QScrollBar::handle:vertical {{
        background-color: {c['border']};
        border-radius: 4px;
        min-height: 30px;
    }}
    QScrollBar::handle:vertical:hover {{
        background-color: {c['text_dim']};
    }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
        height: 0;
    }}
    QScrollBar:horizontal {{
        background-color: transparent;
        height: 8px;
        margin: 0;
    }}
    QScrollBar::handle:horizontal {{
        background-color: {c['border']};
        border-radius: 4px;
        min-width: 30px;
    }}
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
        width: 0;
    }}

    /* === ComboBox === */
    QComboBox {{
        background-color: {c['bg_input']};
        color: {c['text']};
        border: 1px solid {c['border']};
        border-radius: 6px;
        padding: 8px 12px;
        font-size: 13px;
    }}
    QComboBox:hover {{
        border-color: {c['accent']};
    }}
    QComboBox::drop-down {{
        border: none;
        width: 24px;
    }}
    QComboBox QAbstractItemView {{
        background-color: {c['bg_sidebar']};
        color: {c['text']};
        border: 1px solid {c['border']};
        selection-background-color: {c['bg_selected']};
        selection-color: {c['accent']};
        outline: none;
    }}

    /* === Diálogos === */
    QDialog {{
        background-color: {c['bg_sidebar']};
    }}

    /* === StatusBar === */
    QStatusBar {{
        background-color: {c['bg_sidebar']};
        color: {c['text_dim']};
        font-size: 11px;
        border-top: 1px solid {c['border']};
    }}

    /* === MessageBox === */
    QMessageBox {{
        background-color: {c['bg_sidebar']};
    }}
    QMessageBox QLabel {{
        color: {c['text']};
    }}
    """
