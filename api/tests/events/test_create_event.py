from typing import Optional

from api.context import Context
from api.schema import schema
from app.events.entities import Event


class Repository:
    def get(self, id: str) -> Optional[Event]:
        return None

    def save(self, event: Event) -> Event:
        return event


def test_create_event():
    query = """mutation CreateEvent($title: String!, $startDate: Date!) {
        createEvent(title: $title, startDate: $startDate) {
            id
            title
            startDate
        }
    }"""

    result = schema.execute_sync(
        query,
        variable_values={"title": "PyFest", "startDate": "2021-06-16"},
        context_value=Context(event_repository=Repository()),
    )

    assert result.data["createEvent"]["id"]
    assert result.data["createEvent"]["title"] == "PyFest"
    assert result.data["createEvent"]["startDate"] == "2021-06-16"
