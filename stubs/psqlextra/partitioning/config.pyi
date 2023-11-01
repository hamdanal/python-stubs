from _typeshed import Incomplete

from ..models import PostgresPartitionedModel
from .strategy import PostgresPartitioningStrategy

class PostgresPartitioningConfig:
    model: Incomplete
    strategy: Incomplete
    def __init__(self, model: PostgresPartitionedModel, strategy: PostgresPartitioningStrategy) -> None: ...
