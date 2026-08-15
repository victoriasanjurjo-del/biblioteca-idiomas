"""
Styles and Theme Configuration for Language Library UI.
Earthy tones, deep sage/forest greens, and warm pearl/sand backgrounds.
"""

APP_STYLESHEET = """
/* Global Window and Base Styles */
QMainWindow, QWidget#centralWidget {
    background-color: #F6F4EE;
    color: #2D2A26;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Inter', Roboto, sans-serif;
    font-size: 14px;
}

QWidget {
    background-color: transparent;
    color: #2D2A26;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Inter', Roboto, sans-serif;
}

/* Headers & Labels */
QLabel#headerTitle {
    font-size: 22px;
    font-weight: 700;
    color: #1E382B;
    margin-bottom: 2px;
}

QLabel#headerSubtitle {
    font-size: 13px;
    color: #7A7265;
    margin-bottom: 10px;
}

QLabel#sectionTitle {
    font-size: 16px;
    font-weight: 600;
    color: #2D5A43;
    padding-bottom: 4px;
}

QLabel#emptyStateLabel {
    font-size: 14px;
    color: #8C857B;
    font-style: italic;
    padding: 24px;
}

/* Card Containers */
QFrame#cardFrame {
    background-color: #FFFFFF;
    border: 1px solid #E3DDD2;
    border-radius: 12px;
}

/* -----------------------------------------------------------------------
   Info Cards (Vista Detalle de Palabra) — 4 tarjetas superiores
   ----------------------------------------------------------------------- */
QFrame#infoCard {
    background-color: #FFFFFF;
    border: 1px solid #E0DAD0;
    border-radius: 14px;
    padding: 4px;
}

QLabel#cardIcon {
    font-size: 22px;
    color: #2D5A43;
    background-color: transparent;
}

QLabel#cardLabel {
    font-size: 11px;
    font-weight: 600;
    color: #9E9589;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    background-color: transparent;
}

QLabel#cardValue {
    font-size: 14px;
    font-weight: 700;
    color: #1E382B;
    background-color: transparent;
}

/* Word Detail — centro de la pantalla */
QLabel#wordMain {
    font-size: 42px;
    font-weight: 800;
    color: #1A3326;
    letter-spacing: -0.5px;
}

QLabel#wordPronunciation {
    font-size: 17px;
    color: #6B7C74;
    font-style: italic;
    letter-spacing: 0.3px;
}

QLabel#wordTranslationLabel {
    font-size: 11px;
    font-weight: 700;
    color: #9E9589;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

QLabel#wordTranslation {
    font-size: 20px;
    font-weight: 600;
    color: #2D5A43;
}

QLabel#wordDefinitionLabel {
    font-size: 11px;
    font-weight: 700;
    color: #9E9589;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

QLabel#wordDefinition {
    font-size: 15px;
    color: #4A443A;
    line-height: 1.6;
    max-width: 600px;
}

QWidget#transparentSpacer {
    background-color: transparent;
}

/* Divider line */
QFrame#dividerLine {
    background-color: #E3DDD2;
    border: none;
    max-height: 1px;
}

/* Mini decorative divider in word detail center */
QFrame#miniDivider {
    background-color: #C8BFB0;
    border: none;
    max-height: 1px;
}

/* Search / Filter Input */
QLineEdit#searchBar {
    background-color: #FFFFFF;
    border: 1px solid #D6CEBF;
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 13px;
    color: #2D2A26;
    selection-background-color: #38664B;
    selection-color: #FFFFFF;
}

QLineEdit#searchBar:focus {
    border: 1px solid #2D5A43;
    background-color: #FFFEFB;
}

/* Lists */
QListWidget {
    background-color: #FFFFFF;
    border: 1px solid #E3DDD2;
    border-radius: 10px;
    padding: 6px;
    outline: none;
}

QListWidget::item {
    background-color: #FAF9F5;
    border: 1px solid #EDE7DC;
    border-radius: 8px;
    padding: 12px 14px;
    margin: 4px 2px;
    color: #2D2A26;
    font-size: 14px;
}

QListWidget::item:hover {
    background-color: #F1EFE8;
    border: 1px solid #DDD6C8;
    color: #1E382B;
}

QListWidget::item:selected {
    background-color: #E2ECE5;
    border: 1px solid #38664B;
    color: #173826;
    font-weight: 600;
}

/* ScrollBars */
QScrollBar:vertical {
    border: none;
    background: #F6F4EE;
    width: 8px;
    border-radius: 4px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #D4CCBD;
    min-height: 24px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background: #B3A996;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Buttons */
QPushButton {
    font-size: 13px;
    font-weight: 600;
    border-radius: 8px;
    padding: 9px 18px;
    min-height: 20px;
}

/* Primary Button (Forest / Sage Green) */
QPushButton#primaryBtn {
    background-color: #2D5A43;
    color: #FFFFFF;
    border: 1px solid #234835;
}

QPushButton#primaryBtn:hover {
    background-color: #386E52;
}

QPushButton#primaryBtn:pressed {
    background-color: #1E3E2E;
}

QPushButton#primaryBtn:disabled {
    background-color: #B5C4BC;
    border: 1px solid #A5B6AC;
    color: #E6EBE8;
}

/* Secondary Button (Warm Pearl / Neutral Outline) */
QPushButton#secondaryBtn {
    background-color: #FFFFFF;
    color: #4A443A;
    border: 1px solid #D6CEBF;
}

QPushButton#secondaryBtn:hover {
    background-color: #EDE8DD;
    border-color: #C2B8A4;
    color: #2D2A26;
}

QPushButton#secondaryBtn:pressed {
    background-color: #E2DBD0;
}

/* Earth / Terracotta Button */
QPushButton#earthBtn {
    background-color: #8C6239;
    color: #FFFFFF;
    border: 1px solid #754F2B;
}

QPushButton#earthBtn:hover {
    background-color: #9E7043;
}

QPushButton#earthBtn:pressed {
    background-color: #694420;
}

/* Dialogs & Input fields inside dialogs */
QDialog {
    background-color: #F6F4EE;
}

QDialog QLabel {
    color: #2D2A26;
    font-size: 13px;
}

QDialog QLineEdit, QDialog QTextEdit, QDialog QPlainTextEdit {
    background-color: #FFFFFF;
    border: 1px solid #D6CEBF;
    border-radius: 8px;
    padding: 8px;
    font-size: 13px;
    color: #2D2A26;
}

QDialog QLineEdit:focus, QDialog QTextEdit:focus, QDialog QPlainTextEdit:focus {
    border: 1px solid #2D5A43;
}

QDialog QComboBox {
    background-color: #FFFFFF;
    border: 1px solid #D6CEBF;
    border-radius: 8px;
    padding: 7px 12px;
    font-size: 13px;
    color: #2D2A26;
}

QDialog QComboBox:focus {
    border: 1px solid #2D5A43;
}

QDialog QComboBox::drop-down {
    border: none;
    width: 24px;
}

QDialog QComboBox QAbstractItemView {
    background-color: #FFFFFF;
    border: 1px solid #D6CEBF;
    border-radius: 6px;
    selection-background-color: #E2ECE5;
    selection-color: #173826;
    padding: 4px;
}

QMessageBox {
    background-color: #F6F4EE;
}

QMessageBox QPushButton {
    min-width: 75px;
    background-color: #2D5A43;
    color: #FFFFFF;
    border-radius: 6px;
    padding: 6px 14px;
}

QMessageBox QPushButton:hover {
    background-color: #386E52;
}
"""
