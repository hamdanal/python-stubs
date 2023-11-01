from dateutil.relativedelta import relativedelta as relativedelta

from psqlextra.models import PostgresPartitionedModel

from .config import PostgresPartitioningConfig

def partition_by_current_time(
    model: PostgresPartitionedModel,
    count: int,
    years: int | None = ...,
    months: int | None = ...,
    weeks: int | None = ...,
    days: int | None = ...,
    max_age: relativedelta | None = ...,
) -> PostgresPartitioningConfig: ...
