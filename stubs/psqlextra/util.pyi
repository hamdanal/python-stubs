from collections.abc import Generator
from contextlib import contextmanager
from typing import TypeVar

from django.db.models import Model
from psqlextra.manager import PostgresManager

_T = TypeVar("_T", bound=Model)

@contextmanager
def postgres_manager(model: _T) -> Generator[PostgresManager[_T], None, None]: ...
