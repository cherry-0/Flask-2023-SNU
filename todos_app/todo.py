"""
DTO 클래스를 모아놓는 모듈
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from dateutil import parser, tz


@dataclass
class Todo:
    """
    Python 측 "할 일 항목"을 나타내는 클래스

    데이터베이스에서 읽어들인 값을 그대로 사용하지 않고,
    Python에서 다루기 자연스러운 형태로 바꿔서 사용합니다.

    이런 목적을 가지는 객체를 DTO(Data Transfer Object)라고 합니다.
    """

    pk: int
    title: str
    completed: bool
    updated_at: datetime

    def to_tuple(self) -> tuple[int, str, int, str]:
        """
        데이터베이스에 저장하기 위해 값 변환
        """
        pk = self.pk
        title = self.title
        completed = int(self.completed)
        updated_at = self.updated_at.timestamp()
        return pk, title, completed, updated_at

    @staticmethod
    def from_tuple(pk: int, title: str, completed: int, updated_at: str) -> 'Todo':
        """
        데이터베이스로부터 읽어들인 값을 Python 에서 사용하기 자연스러운 값으로 변환
        """
        completed = bool(completed)
        parsed = parser.parse(updated_at)
        parsed = parsed.replace(tzinfo=parsed.tzinfo or tz.gettz("UTC")).astimezone(tz=tz.gettz("Asia/Seoul"))
        return Todo(pk, title, completed, parsed)
    
    def as_dict(self):
        """
        객체의 내용을 dict 로 변환 (JSON 변환 등에 활용)
        """
        return asdict(self)
