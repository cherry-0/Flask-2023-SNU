"""
"할 일 목록" 데이터베이스에 접근하는 함수들을 모아놓은 모듈
"""

from typing import Optional

from .todo import Todo


class TodoRepository:
    """
    todos 테이블에 접근하는 함수들을 모아놓은 클래스
    """

    def __init__(self, db):
        self.db = db

    def get_todos(self) -> list[Todo]:
        """
        todos 테이블의 전체 레코드를 가져오기
        """
        cursor = self.db.execute("""
            SELECT pk, title, completed, updated_at
            FROM todos;
        """)
        return [
            Todo.from_tuple(pk, title, completed, updated_at)
            for pk, title, completed, updated_at
            in cursor
        ]

    def get_todo(self, pk: int) -> Optional[Todo]:
        """
        todos 테이블의 레코드 중 pk가 일치하는 단일 레코드를 가져오기
        """
        cursor = self.db.execute("""
            SELECT pk, title, completed, updated_at
            FROM todos
            WHERE pk = ?;
        """, [pk])
        if row := cursor.fetchone():
            pk, title, completed, updated_at = row
            return Todo.from_tuple(pk, title, completed, updated_at)
        else:
            return None

    def create_todo(self, title: str) -> Todo:
        """
        todos 테이블에 새로운 레코드 생성하기
        """
        cursor = self.db.execute("""
            INSERT INTO todos(title) values (?);
        """, [title])
        return self.get_todo(cursor.lastrowid)

    def toggle_todo(self, pk: int):
        """
        todos 레코드의 completed를 반대로 바꿔서 저장하기
        """
        self.db.execute("""
            UPDATE todos
            SET
                updated_at = CURRENT_TIMESTAMP,
                completed = NOT completed
            WHERE pk = ?;
        """, [pk])

    def delete_todo(self, pk: int):
        """
        todos 레코드를 삭제하기
        """
        self.db.execute("""
            DELETE FROM todos
            WHERE pk = ?;
        """, [pk])
