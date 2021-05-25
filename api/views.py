from app.events.repository import DjangoEventRepository
from django.http import HttpRequest, HttpResponse
from strawberry.django.views import GraphQLView as BaseGraphQLView

from .context import Context
from .schema import schema


class GraphQLView(BaseGraphQLView):
    def __init__(self):
        super().__init__(schema, True)

    def get_context(self, request: HttpRequest, response: HttpResponse) -> Context:
        return Context(event_repository=DjangoEventRepository())
