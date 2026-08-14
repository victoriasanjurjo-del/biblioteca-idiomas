import sqlite3
import os
from datetime import datetime
from typing import List, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'language_library.db')

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS languages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(language_id) REFERENCES languages(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

def get_languages() -> List[sqlite3.Row]:
    conn = get_connection()
    rows = conn.execute('SELECT id, name FROM languages ORDER BY name').fetchall()
    conn.close()
    return rows

def add_language(name: str) -> Optional[int]:
    name = name.strip()
    if not name:
        return None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO languages (name) VALUES (?)', (name,))
        conn.commit()
        lang_id = cursor.lastrowid
        conn.close()
        return lang_id
    except sqlite.IntegrityError:
        conn.close()
        return None

def get_entries(language_id: int) -> List[sqlite3.Row]:
    conn = get_connection()
    rows = conn.execute('SELECT id, text, created_at, updated_at FROM entries WHERE language_id = ? ORDER BY created_at', (language_id,)).fetchall()
    conn.close()
    return rows

def add_entry(language_id: int, text: str) -> Optional[int]:
    text = text.strip()
    if not text:
        return None
    now = datetime.utcnow().isoformat(timespec='seconds')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (language_id, text, created_at, updated_at) VALUES (?,?,?,?)', (language_id, text, now, now))
    conn.commit()
    entry_id = cursor.lastrowid
    conn.close()
    return entry_id

def update_entry(entry_id: int, new_text: str) -> bool:
    new_text = new_text.strip()
    if not new_text:
        return False
    now = datetime.utcnow().isoformat(timespec='seconds')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE entries SET text = ?, updated_at = ? WHERE id = ?', (new_text, now, entry_id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated
