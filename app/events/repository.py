from typing import Optional, Protocol

from .entities import Event


class AbstractEventRepository(Protocol):
    def get(self, id: str) -> Optional[Event]:
        ...

    def save(self, event: Event) -> Event:
        ...


class DjangoEventRepository:
    ...