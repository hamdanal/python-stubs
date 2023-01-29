from abc import ABCMeta, abstractmethod
from collections.abc import Generator

from .partition import PostgresPartition

class PostgresPartitioningStrategy(metaclass=ABCMeta):
    @abstractmethod
    def to_create(self) -> Generator[PostgresPartition, None, None]: ...
    @abstractmethod
    def to_delete(self) -> Generator[PostgresPartition, None, None]: ...
