from _typeshed import Incomplete

from django.db.models import Combinable, Index

class CaseInsensitiveUniqueIndex(Index):
    sql_create_unique_index: str
    def deconstruct(self) -> tuple[str, tuple[Combinable, ...], dict[str, Incomplete]]: ...
