import abc

from .strategy import PostgresPartitioningStrategy

class PostgresRangePartitioningStrategy(PostgresPartitioningStrategy, metaclass=abc.ABCMeta): ...
