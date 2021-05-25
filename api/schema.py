from datetime import date
from typing import Any, Optional

import strawberry
from strawberry.types import Info

from app.events.services import create_event

from .context import Context
from .events.types import Event


@strawberry.type
class Query:
    @strawberry.field
    def event(self, info: Info[Context, Any], id: strawberry.ID) -> Optional[Event]:
        domain_event = info.context.event_repository.get(id=id)

        if domain_event:
            return Event.from_domain(domain_event)

        return None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_event(self, info: Info[Context, Any], title: str, start_date: date) -> Event:
        domain_event = create_event(
            title=title, start_date=start_date, repository=info.context.event_repository
        )

        return Event.from_domain(domain_event)


schema = strawberry.Schema(Query, Mutation)
