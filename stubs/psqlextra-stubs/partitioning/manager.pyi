from typing_extensions import TypeAlias

from psqlextra.models import PostgresPartitionedModel
from psqlextra.partitioning.config import PostgresPartitioningConfig
from psqlextra.partitioning.partition import PostgresPartition
from psqlextra.partitioning.plan import PostgresPartitioningPlan

PartitionList: TypeAlias = list[tuple[PostgresPartitionedModel, list[PostgresPartition]]]

class PostgresPartitioningManager:
    configs: list[PostgresPartitioningConfig]
    def __init__(self, configs: list[PostgresPartitioningConfig]) -> None: ...
    def plan(
        self, skip_create: bool = False, skip_delete: bool = False, using: str | None = None
    ) -> PostgresPartitioningPlan: ...
    def find_config_for_model(self, model: PostgresPartitionedModel) -> PostgresPartitioningConfig | None: ...
