from _typeshed import Incomplete

from django.db.models.base import ModelBase

from .base import PostgresModel

class PostgresPartitionedModelMeta(ModelBase):
    default_method: Incomplete
    default_key: Incomplete
    def __new__(cls, name, bases, attrs, **kwargs): ...

class PostgresPartitionedModel(PostgresModel, metaclass=PostgresPartitionedModelMeta):
    class Meta:
        abstract: bool
        base_manager_name: str
