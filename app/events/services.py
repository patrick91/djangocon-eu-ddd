from datetime import date
from uuid import uuid4

from .entities import Event
from .exceptions import InvalidEventDateError
from .repository import AbstractEventRepository


def create_event(title: str, start_date: date, repository: AbstractEventRepository):
    if start_date < start_date.today():
        raise InvalidEventDateError()

    event = Event(id=uuid4(), title=title, start_date=start_date)

    return repository.save(event)
