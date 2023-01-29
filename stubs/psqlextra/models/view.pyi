from _typeshed import Incomplete
from collections.abc import Callable
from typing_extensions import TypeAlias

from django.db.models import Model as Model
from django.db.models.base import ModelBase
from django.db.models.query import QuerySet
from psqlextra.types import SQL, SQLWithParams

from .base import PostgresModel

ViewQueryValue: TypeAlias = QuerySet[Incomplete] | SQLWithParams | SQL
ViewQuery: TypeAlias = ViewQueryValue | Callable[[], ViewQueryValue] | None

class PostgresViewModelMeta(ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs): ...

class PostgresViewModel(PostgresModel, metaclass=PostgresViewModelMeta):
    class Meta:
        abstract: bool
        base_manager_name: str

class PostgresMaterializedViewModel(PostgresViewModel, metaclass=PostgresViewModelMeta):
    class Meta:
        abstract: bool
        base_manager_name: str
    @classmethod
    def refresh(cls, concurrently: bool = ..., using: str | None = ...) -> None: ...
