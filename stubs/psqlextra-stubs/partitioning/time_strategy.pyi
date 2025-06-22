import datetime as dt

from dateutil.relativedelta import relativedelta

from psqlextra.partitioning.current_time_strategy import PostgresCurrentTimePartitioningStrategy
from psqlextra.partitioning.time_partition_size import PostgresTimePartitionSize

class PostgresTimePartitioningStrategy(PostgresCurrentTimePartitioningStrategy):
    start_datetime: dt.datetime
    def __init__(
        self, start_datetime: dt.datetime, size: PostgresTimePartitionSize, count: int, max_age: relativedelta | None = None
    ) -> None: ...
    def get_start_datetime(self) -> dt.datetime: ...
