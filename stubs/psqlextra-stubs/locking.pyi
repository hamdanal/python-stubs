from enum import Enum

from django.db import models

class PostgresTableLockMode(Enum):
    ACCESS_SHARE: str
    ROW_SHARE: str
    ROW_EXCLUSIVE: str
    SHARE_UPDATE_EXCLUSIVE: str
    SHARE: str
    SHARE_ROW_EXCLUSIVE: str
    EXCLUSIVE: str
    ACCESS_EXCLUSIVE: str

    @property
    def alias(self) -> str: ...

def postgres_lock_table(
    table_name: str, lock_mode: PostgresTableLockMode, *, schema_name: str | None = None, using: str = "default"
) -> None: ...
def postgres_lock_model(
    model: type[models.Model], lock_mode: PostgresTableLockMode, *, using: str = "default", schema_name: str | None = None
) -> None: ...
