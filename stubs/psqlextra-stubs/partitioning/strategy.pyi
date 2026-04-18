from abc import ABCMeta, abstractmethod
from collections.abc import Generator

from psqlextra.partitioning.partition import PostgresPartition

class PostgresPartitioningStrategy(metaclass=ABCMeta):
    @abstractmethod
    def to_create(self) -> Generator[PostgresPartition]: ...
    @abstractmethod
    def to_delete(self) -> Generator[PostgresPartition]: ...
