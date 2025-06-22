from dateutil.relativedelta import relativedelta

from psqlextra.models import PostgresPartitionedModel
from psqlextra.partitioning.config import PostgresPartitioningConfig

__all__ = ["partition_by_current_time"]

def partition_by_current_time(
    model: PostgresPartitionedModel,
    count: int,
    years: int | None = None,
    months: int | None = None,
    weeks: int | None = None,
    days: int | None = None,
    max_age: relativedelta | None = None,
) -> PostgresPartitioningConfig: ...
