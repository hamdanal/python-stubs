from _typeshed import Incomplete
from collections.abc import Callable
from typing_extensions import TypeAlias

from django.db.models.base import ModelBase
from django.db.models.query import QuerySet
from psqlextra.models.base import PostgresModel
from psqlextra.types import SQL, SQLWithParams

ViewQueryValue: TypeAlias = QuerySet[Incomplete] | SQLWithParams | SQL
ViewQuery: TypeAlias = ViewQueryValue | Callable[[], ViewQueryValue] | None

class PostgresViewModelMeta(ModelBase): ...
class PostgresViewModel(PostgresModel, metaclass=PostgresViewModelMeta): ...

class PostgresMaterializedViewModel(PostgresViewModel, metaclass=PostgresViewModelMeta):
    @classmethod
    def refresh(cls, concurrently: bool = False, using: str | None = None) -> None: ...
