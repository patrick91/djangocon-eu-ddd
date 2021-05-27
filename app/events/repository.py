from typing import Optional, Protocol

from .entities import Event

from db import models


class AbstractEventRepository(Protocol):
    def get(self, id: str) -> Optional[Event]:
        ...

    def save(self, event: Event) -> Event:
        ...


class DjangoEventRepository:
    def get(self, id: str) -> Optional[Event]:
        db_event = models.Event.objects.filter(id=id).first()

        if db_event:
            return self._convert_instance(db_event)

        return None

    def save(self, event: Event) -> Event:
        db_event, _ = models.Event.objects.update_or_create(
            id=event.id,
            defaults={"title": event.title, "start_date": event.start_date},
        )

        return self._convert_instance(db_event)

    @staticmethod
    def _convert_instance(instance: models.Event) -> Event:
        return Event(
            id=instance.id, title=instance.title, start_date=instance.start_date
        )
