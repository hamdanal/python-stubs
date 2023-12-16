from _typeshed import Incomplete
from datetime import datetime

from dateutil.relativedelta import relativedelta as relativedelta

from psqlextra.partitioning.current_time_strategy import PostgresCurrentTimePartitioningStrategy
from psqlextra.partitioning.time_partition_size import PostgresTimePartitionSize

class PostgresTimePartitioningStrategy(PostgresCurrentTimePartitioningStrategy):
    start_datetime: Incomplete
    def __init__(
        self, start_datetime: datetime, size: PostgresTimePartitionSize, count: int, max_age: relativedelta | None = ...
    ) -> None: ...
    def get_start_datetime(self) -> datetime: ...
