from typing import TypeVar

from django.db import models

from psqlextra.query import PostgresQuerySet

_ModelT = TypeVar("_ModelT", bound=models.Model)

class PostgresManager(models.Manager[_ModelT], PostgresQuerySet[_ModelT]):
    def truncate(self, cascade: bool = False, using: str | None = None) -> None: ...
    def get_queryset(self) -> PostgresQuerySet[_ModelT]: ...
