from collections.abc import Generator
from contextlib import contextmanager

from django.db.models import Model

from psqlextra.manager import PostgresManager

@contextmanager
def postgres_manager[M: Model](model: type[M]) -> Generator[PostgresManager[M]]: ...
