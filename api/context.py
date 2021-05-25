from dataclasses import dataclass

from app.events.repository import AbstractEventRepository


@dataclass
class Context:
    event_repository: AbstractEventRepository
