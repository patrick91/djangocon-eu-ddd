from datetime import date, timedelta

import pytest
from app.events.entities import Event
from app.events.exceptions import InvalidEventDateError
from app.events.services import create_event


class EventTestRepository:
    def save(self, event: Event) -> Event:
        return event


def test_create_event():
    start_date = date.today() + timedelta(days=7)

    event = create_event(
        title="DjangoCon Europe",
        start_date=start_date,
        repository=EventTestRepository(),
    )

    assert event.id
    assert event.title == "DjangoCon Europe"
    assert event.start_date == start_date


def test_fails_if_date_is_past():
    start_date = date.today() - timedelta(days=7)

    with pytest.raises(InvalidEventDateError):
        create_event(
            title="DjangoCon Europe",
            start_date=start_date,
            repository=EventTestRepository(),
        )
