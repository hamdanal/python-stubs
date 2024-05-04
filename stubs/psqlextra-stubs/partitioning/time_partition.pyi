from datetime import datetime
from typing import Any

from psqlextra.partitioning.range_partition import PostgresRangePartition
from psqlextra.partitioning.time_partition_size import PostgresTimePartitionSize

class PostgresTimePartition(PostgresRangePartition):
    size: PostgresTimePartitionSize
    start_datetime: datetime
    end_datetime: datetime
    def __init__(self, size: PostgresTimePartitionSize, start_datetime: datetime) -> None: ...
    def name(self) -> str: ...
    def deconstruct(self) -> dict[str, Any]: ...
