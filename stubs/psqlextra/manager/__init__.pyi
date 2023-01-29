# this (PostgresQuerySet) should not be here, but there are users depending on this being here, so
# let's leave it here so we don't break them
from psqlextra.manager.manager import PostgresManager
from psqlextra.query import PostgresQuerySet

__all__ = ["PostgresManager", "PostgresQuerySet"]
