from django.db.models import Manager, Model

from psqlextra.query import PostgresQuerySet

class PostgresManager[M: Model](Manager[M], PostgresQuerySet[M]):
    def truncate(self, cascade: bool = False, using: str | None = None) -> None: ...
    def get_queryset(self) -> PostgresQuerySet[M]: ...
