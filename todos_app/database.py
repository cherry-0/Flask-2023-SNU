"""
데이터베이스 연결 및 초기화와 관련된 코드를 모아놓은 모듈
"""

import os
import sqlite3

from flask import g


def get_db():
    """
    매 요청마다, 새로운 데이터베이스 연결을 반환합니다.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(str(os.getenv("DATABASE_PATH")), isolation_level=None)
    return db


def create_tables():
    """ 
    데이터베이스에 테이블(엑셀 시트와 비슷한 개념)을 생성합니다.
    """
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        completed BOOLEAN NOT NULL DEFAULT FALSE,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """)
