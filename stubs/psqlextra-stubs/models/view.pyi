from _typeshed import Incomplete
from collections.abc import Callable

from django.db.models.base import ModelBase
from django.db.models.query import QuerySet

from psqlextra.models.base import PostgresModel
from psqlextra.types import SQL, SQLWithParams

type ViewQueryValue = QuerySet[Incomplete] | SQLWithParams | SQL
type ViewQuery = ViewQueryValue | Callable[[], ViewQueryValue] | None

class PostgresViewModelMeta(ModelBase): ...
class PostgresViewModel(PostgresModel, metaclass=PostgresViewModelMeta): ...

class PostgresMaterializedViewModel(PostgresViewModel, metaclass=PostgresViewModelMeta):
    @classmethod
    def refresh(cls, concurrently: bool = False, using: str | None = None) -> None: ...
