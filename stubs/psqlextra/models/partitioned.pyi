from collections.abc import Iterable

from django.db.models.base import ModelBase
from psqlextra.models.base import PostgresModel
from psqlextra.types import PostgresPartitioningMethod

class PostgresPartitionedModelMeta(ModelBase):
    default_method: PostgresPartitioningMethod
    default_key: Iterable[str]

class PostgresPartitionedModel(PostgresModel, metaclass=PostgresPartitionedModelMeta): ...
