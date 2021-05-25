from __future__ import annotations

from datetime import date

import strawberry
from app.events import entities


@strawberry.type
class Event:
    id: strawberry.ID
    title: str
    start_date: date

    @classmethod
    def from_domain(cls, entity: entities.Event) -> Event:
        return cls(
            id=entity.id,
            title=entity.title,
            start_date=entity.start_date,
        )
