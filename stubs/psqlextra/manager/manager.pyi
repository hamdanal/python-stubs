from typing import TypeVar

from django.db import models
from psqlextra.query import PostgresQuerySet

_T = TypeVar("_T", bound=models.Model)

class PostgresManager(models.Manager[_T], PostgresQuerySet[_T]):
    def truncate(self, cascade: bool = False, using: str | None = None) -> None: ...
