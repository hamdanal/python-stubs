from enum import Enum

from django.db import models

class PostgresTableLockMode(Enum):
    ACCESS_SHARE = "ACCESS SHARE"
    ROW_SHARE = "ROW SHARE"
    ROW_EXCLUSIVE = "ROW EXCLUSIVE"
    SHARE_UPDATE_EXCLUSIVE = "SHARE UPDATE EXCLUSIVE"
    SHARE = "SHARE"
    SHARE_ROW_EXCLUSIVE = "SHARE ROW EXCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"
    ACCESS_EXCLUSIVE = "ACCESS EXCLUSIVE"

    @property
    def alias(self) -> str: ...

def postgres_lock_table(
    table_name: str, lock_mode: PostgresTableLockMode, *, schema_name: str | None = None, using: str = "default"
) -> None: ...
def postgres_lock_model(
    model: type[models.Model], lock_mode: PostgresTableLockMode, *, using: str = "default", schema_name: str | None = None
) -> None: ...
