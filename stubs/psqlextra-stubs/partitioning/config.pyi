from _typeshed import Incomplete

from psqlextra.models import PostgresPartitionedModel
from psqlextra.partitioning.strategy import PostgresPartitioningStrategy

class PostgresPartitioningConfig:
    model: Incomplete
    strategy: Incomplete
    def __init__(self, model: PostgresPartitionedModel, strategy: PostgresPartitioningStrategy) -> None: ...
