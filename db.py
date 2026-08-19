from datetime import datetime
import sqlite3
from config import DATABASE


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

def init_database():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            filepath TEXT NOT NULL,
            pages INTEGER DEFAULT 0,
            upload_date TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            page INTEGER,
            chunk TEXT,
            FOREIGN KEY(document_id)
            REFERENCES documents(id)
            ON DELETE CASCADE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clauses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            clause_type TEXT,
            clause TEXT,
            page INTEGER,
            FOREIGN KEY(document_id)
            REFERENCES documents(id)
            ON DELETE CASCADE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS risks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            severity TEXT,
            reason TEXT,
            page INTEGER,
            FOREIGN KEY(document_id)
            REFERENCES documents(id)
            ON DELETE CASCADE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            confidence REAL,
            document_id INTEGER,
            created_at TEXT
        )
        """)


# ==========================================================
# DATABASE CLASS
# ==========================================================

class Database:

    def __init__(self):
        init_database()

    def connection(self):
        return get_connection()

    # ======================================================
    # DOCUMENT METHODS
    # ======================================================

    def add_document(self, filename, filepath, pages, upload_date):

        conn = self.connection()

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO documents
        (filename, filepath, pages, upload_date)
        VALUES (?, ?, ?, ?)
    """, (
        filename,
        filepath,
        pages,
        upload_date
    ))

        conn.commit()

        document_id = cursor.lastrowid

        conn.close()

        return document_id

    def get_documents(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM documents
                ORDER BY id DESC
                """
            ).fetchall()

    def get_document(self, document_id):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM documents
                WHERE id=?
                """,
                (document_id,)
            ).fetchone()

    def total_documents(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT COUNT(*)
                FROM documents
                """
            ).fetchone()[0]

    # ======================================================
    # CHUNK METHODS
    # ======================================================

    def add_chunk(self, document_id, page, chunk):
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO chunks (document_id, page, chunk)
                VALUES (?, ?, ?)
                """,
                (document_id, page, chunk)
            )

    def add_chunks(self, document_id, chunks):
        data = [(document_id, item["page"], item["text"]) for item in chunks]

        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                """
                INSERT INTO chunks (document_id, page, chunk)
                VALUES (?, ?, ?)
                """,
                data
            )

    def get_document_chunks(self, document_id):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM chunks
                WHERE document_id=?
                ORDER BY page, id
                """,
                (document_id,)
            ).fetchall()

    def get_chunk_count(self, document_id):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT COUNT(*)
                FROM chunks
                WHERE document_id=?
                """,
                (document_id,)
            ).fetchone()[0]

    def delete_chunks(self, document_id):
        with self.connection() as conn:
            conn.execute(
                """
                DELETE FROM chunks
                WHERE document_id=?
                """,
                (document_id,)
            )

    # ======================================================
    # CLAUSE METHODS
    # ======================================================

    def add_clause(self, document_id, clause_type, clause, page):
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO clauses (document_id, clause_type, clause, page)
                VALUES (?, ?, ?, ?)
                """,
                (document_id, clause_type, clause, page)
            )

    def add_clauses(self, document_id, clauses):
        data = [
            (document_id, item["type"], item["text"], item["page"])
            for item in clauses
        ]

        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                """
                INSERT INTO clauses (document_id, clause_type, clause, page)
                VALUES (?, ?, ?, ?)
                """,
                data
            )

    def get_clauses(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM clauses
                ORDER BY id DESC
                """
            ).fetchall()

    def get_document_clauses(self, document_id):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT id, document_id, clause_type, clause, page
                FROM clauses
                WHERE document_id=?
                ORDER BY page, id
                """,
                (document_id,)
            ).fetchall()

    def clause_count(self, document_id=None):
        with self.connection() as conn:
            if document_id is None:
                return conn.execute(
                    """
                    SELECT COUNT(*)
                    FROM clauses
                    """
                ).fetchone()[0]
            else:
                return conn.execute(
                    """
                    SELECT COUNT(*)
                    FROM clauses
                    WHERE document_id=?
                    """,
                    (document_id,)
                ).fetchone()[0]

    # ======================================================
    # RISK METHODS
    # ======================================================

    def add_risk(self, document_id, severity, reason, page):
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO risks (document_id, severity, reason, page)
                VALUES (?, ?, ?, ?)
                """,
                (document_id, severity, reason, page)
            )

    def add_risks(self, document_id, risks):
        data = [
            (document_id, item["severity"], item["reason"], item["page"])
            for item in risks
        ]

        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                """
                INSERT INTO risks (document_id, severity, reason, page)
                VALUES (?, ?, ?, ?)
                """,
                data
            )

    def get_risks(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM risks
                ORDER BY id DESC
                """
            ).fetchall()

    def get_document_risks(self, document_id):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM risks
                WHERE document_id=?
                ORDER BY page
                """,
                (document_id,)
            ).fetchall()

    def high_risk_count(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT COUNT(*)
                FROM risks
                WHERE severity='HIGH'
                """
            ).fetchone()[0]

    def risk_count(self, document_id=None):
        with self.connection() as conn:
            if document_id is None:
                return conn.execute(
                    """
                    SELECT COUNT(*)
                    FROM risks
                    """
                ).fetchone()[0]
            else:
                return conn.execute(
                    """
                    SELECT COUNT(*)
                    FROM risks
                    WHERE document_id=?
                    """,
                    (document_id,)
                ).fetchone()[0]

    # ======================================================
    # HISTORY METHODS
    # ======================================================

    def add_question(self, question, answer, confidence, document_id=None):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO history (question, answer, confidence, document_id, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (question, answer, confidence, document_id, created_at)
            )

    def get_history(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT *
                FROM history
                ORDER BY id DESC
                """
            ).fetchall()

    def history_count(self):
        with self.connection() as conn:
            return conn.execute(
                """
                SELECT COUNT(*)
                FROM history
                """
            ).fetchone()[0]

    # ======================================================
    # DELETE METHODS
    # ======================================================

    def delete_document(self, document_id):
        with self.connection() as conn:
            conn.execute(
                """
                DELETE FROM documents
                WHERE id=?
                """,
                (document_id,)
            )

    def clear_history(self):
        with self.connection() as conn:
            conn.execute(
                """
                DELETE FROM history
                """
            )

    # ======================================================
    # DASHBOARD STATISTICS
    # ======================================================

    def dashboard_statistics(self):
        return {
            "documents": self.total_documents(),
            "clauses": self.clause_count(),
            "risks": self.risk_count(),
            "high_risks": self.high_risk_count(),
            "questions": self.history_count(),
        }


# ==========================================================
# DATABASE OBJECT
# ==========================================================

db = Database()


# ==========================================================
# MAIN TEST
# ==========================================================

if __name__ == "__main__":
    print("Database initialized successfully")
    print(db.dashboard_statistics())