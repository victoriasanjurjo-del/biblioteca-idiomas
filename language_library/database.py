import sqlite3
import os
from datetime import datetime
from typing import List, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'language_library.db')


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _column_exists(cursor: sqlite3.Cursor, table: str, column: str) -> bool:
    """Helper: check if a column already exists in a table."""
    cursor.execute(f"PRAGMA table_info({table})")
    return any(row["name"] == column for row in cursor.fetchall())


def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    # --- word_families table (global, not tied to any language) ---
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS word_families (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # --- languages table ---
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS languages (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            name            TEXT NOT NULL UNIQUE,
            language_family TEXT
        )
    ''')
    # Migration: add language_family if upgrading an existing DB
    if not _column_exists(cursor, "languages", "language_family"):
        cursor.execute("ALTER TABLE languages ADD COLUMN language_family TEXT")

    # --- entries table ---
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            language_id     INTEGER NOT NULL,
            text            TEXT NOT NULL,
            pronunciation   TEXT,
            translation     TEXT,
            definition      TEXT,
            word_family_id  INTEGER,
            created_at      TEXT NOT NULL,
            updated_at      TEXT NOT NULL,
            FOREIGN KEY(language_id)    REFERENCES languages(id)     ON DELETE CASCADE,
            FOREIGN KEY(word_family_id) REFERENCES word_families(id) ON DELETE SET NULL
        )
    ''')
    # Migrations: add new columns if upgrading an existing DB
    for col in ("pronunciation", "translation", "definition", "word_family_id"):
        if not _column_exists(cursor, "entries", col):
            cursor.execute(f"ALTER TABLE entries ADD COLUMN {col} TEXT")

    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Word Families
# ---------------------------------------------------------------------------

def get_word_families() -> List[sqlite3.Row]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name FROM word_families ORDER BY name"
    ).fetchall()
    conn.close()
    return rows


def add_word_family(name: str) -> Optional[int]:
    name = name.strip()
    if not name:
        return None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO word_families (name) VALUES (?)", (name,))
        conn.commit()
        family_id = cursor.lastrowid
        conn.close()
        return family_id
    except sqlite3.IntegrityError:
        conn.close()
        return None


# ---------------------------------------------------------------------------
# Languages
# ---------------------------------------------------------------------------

def get_languages() -> List[sqlite3.Row]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name, language_family FROM languages ORDER BY name"
    ).fetchall()
    conn.close()
    return rows


def add_language(name: str, language_family: str = "") -> Optional[int]:
    name = name.strip()
    if not name:
        return None
    language_family = language_family.strip() or None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO languages (name, language_family) VALUES (?, ?)",
            (name, language_family),
        )
        conn.commit()
        lang_id = cursor.lastrowid
        conn.close()
        return lang_id
    except sqlite3.IntegrityError:
        conn.close()
        return None


# ---------------------------------------------------------------------------
# Entries
# ---------------------------------------------------------------------------

def get_entries(language_id: int) -> List[sqlite3.Row]:
    conn = get_connection()
    rows = conn.execute(
        '''
        SELECT e.id, e.text, e.pronunciation, e.translation, e.definition,
               e.word_family_id, wf.name AS word_family_name,
               e.created_at, e.updated_at
        FROM entries e
        LEFT JOIN word_families wf ON wf.id = e.word_family_id
        WHERE e.language_id = ?
        ORDER BY e.created_at
        ''',
        (language_id,),
    ).fetchall()
    conn.close()
    return rows


def get_entry(entry_id: int) -> Optional[sqlite3.Row]:
    conn = get_connection()
    row = conn.execute(
        '''
        SELECT e.id, e.language_id, e.text, e.pronunciation, e.translation,
               e.definition, e.word_family_id, wf.name AS word_family_name,
               e.created_at, e.updated_at
        FROM entries e
        LEFT JOIN word_families wf ON wf.id = e.word_family_id
        WHERE e.id = ?
        ''',
        (entry_id,),
    ).fetchone()
    conn.close()
    return row


def add_entry(
    language_id: int,
    text: str,
    pronunciation: str = "",
    translation: str = "",
    definition: str = "",
    word_family_id: Optional[int] = None,
) -> Optional[int]:
    text = text.strip()
    if not text:
        return None
    now = datetime.utcnow().isoformat(timespec="seconds")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO entries
            (language_id, text, pronunciation, translation, definition,
             word_family_id, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            language_id,
            text,
            pronunciation.strip() or None,
            translation.strip() or None,
            definition.strip() or None,
            word_family_id,
            now,
            now,
        ),
    )
    conn.commit()
    entry_id = cursor.lastrowid
    conn.close()
    return entry_id


def update_entry(
    entry_id: int,
    new_text: str,
    pronunciation: str = "",
    translation: str = "",
    definition: str = "",
    word_family_id: Optional[int] = None,
) -> bool:
    new_text = new_text.strip()
    if not new_text:
        return False
    now = datetime.utcnow().isoformat(timespec="seconds")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        UPDATE entries
        SET text = ?, pronunciation = ?, translation = ?, definition = ?,
            word_family_id = ?, updated_at = ?
        WHERE id = ?
        ''',
        (
            new_text,
            pronunciation.strip() or None,
            translation.strip() or None,
            definition.strip() or None,
            word_family_id,
            now,
            entry_id,
        ),
    )
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated
