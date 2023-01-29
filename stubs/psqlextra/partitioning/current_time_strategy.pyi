from _typeshed import Incomplete
from collections.abc import Generator
from datetime import datetime

from dateutil.relativedelta import relativedelta as relativedelta

from .range_strategy import PostgresRangePartitioningStrategy
from .time_partition import PostgresTimePartition
from .time_partition_size import PostgresTimePartitionSize

class PostgresCurrentTimePartitioningStrategy(PostgresRangePartitioningStrategy):
    size: Incomplete
    count: Incomplete
    max_age: Incomplete
    def __init__(self, size: PostgresTimePartitionSize, count: int, max_age: relativedelta | None = ...) -> None: ...
    def to_create(self) -> Generator[PostgresTimePartition, None, None]: ...
    def to_delete(self) -> Generator[PostgresTimePartition, None, None]: ...
    def get_start_datetime(self) -> datetime: ...
