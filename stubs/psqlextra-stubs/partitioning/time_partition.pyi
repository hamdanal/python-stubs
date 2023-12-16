from _typeshed import Incomplete
from datetime import datetime

from psqlextra.partitioning.range_partition import PostgresRangePartition
from psqlextra.partitioning.time_partition_size import PostgresTimePartitionSize

class PostgresTimePartition(PostgresRangePartition):
    size: Incomplete
    start_datetime: Incomplete
    end_datetime: Incomplete
    def __init__(self, size: PostgresTimePartitionSize, start_datetime: datetime) -> None: ...
    def name(self) -> str: ...
    def deconstruct(self) -> dict: ...
