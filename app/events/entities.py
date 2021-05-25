from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class Event:
    id: UUID
    title: str
    start_date: date
