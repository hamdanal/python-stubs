import datetime as dt
from collections.abc import Generator

from dateutil.relativedelta import relativedelta

from psqlextra.partitioning.range_strategy import PostgresRangePartitioningStrategy
from psqlextra.partitioning.time_partition import PostgresTimePartition
from psqlextra.partitioning.time_partition_size import PostgresTimePartitionSize

class PostgresCurrentTimePartitioningStrategy(PostgresRangePartitioningStrategy):
    size: PostgresTimePartitionSize
    count: int
    max_age: relativedelta | None
    def __init__(self, size: PostgresTimePartitionSize, count: int, max_age: relativedelta | None = None) -> None: ...
    def to_create(self) -> Generator[PostgresTimePartition]: ...
    def to_delete(self) -> Generator[PostgresTimePartition]: ...
    def get_start_datetime(self) -> dt.datetime: ...
