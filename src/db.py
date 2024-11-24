import sqlite3


def create_table() -> sqlite3.Connection:
    # データベースをメモリ上に作成（プログラム終了時に消える）
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()

    return conn


def insert_user(conn: sqlite3.Connection, user_id: int, name: str):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()


def fetch_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
