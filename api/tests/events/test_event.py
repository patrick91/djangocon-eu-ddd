from typing import Optional
from datetime import date

from api.context import Context
from api.schema import schema
from app.events.entities import Event


def test_get_event_returns_none():
    class Repository:
        def get(self, id: str) -> Optional[Event]:
            return None

        def save(self, event: Event) -> Event:
            return event

    query = """query GetEvent($id: ID!) {
        event(id: $id) {
            id
        }
    }"""

    result = schema.execute_sync(
        query,
        variable_values={"id": "123"},
        context_value=Context(event_repository=Repository()),
    )

    assert result.data["event"] is None


def test_get_event_returns_event():
    class Repository:
        def get(self, id: str) -> Optional[Event]:
            return Event(
                id=id,
                title="Example Event",
                start_date=date(2021, 6, 16),
            )

        def save(self, event: Event) -> Event:
            return event

    query = """query GetEvent($id: ID!) {
        event(id: $id) {
            id
            title
            startDate
        }
    }"""

    result = schema.execute_sync(
        query,
        variable_values={"id": "123"},
        context_value=Context(event_repository=Repository()),
    )

    assert result.data["event"] == {
        "id": "123",
        "title": "Example Event",
        "startDate": "2021-06-16",
    }
