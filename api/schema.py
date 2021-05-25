from typing import Any, Optional

import strawberry
from strawberry.types import Info

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


schema = strawberry.Schema(Query)
