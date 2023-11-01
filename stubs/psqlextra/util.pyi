from collections.abc import Generator
from contextlib import contextmanager
from typing import TypeVar

from django.db.models import Model

from .manager import PostgresManager

_ModelT = TypeVar("_ModelT", bound=Model)

@contextmanager
def postgres_manager(model: type[_ModelT]) -> Generator[PostgresManager[_ModelT], None, None]: ...
