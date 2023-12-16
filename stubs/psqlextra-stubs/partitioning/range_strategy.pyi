import abc

from psqlextra.partitioning.strategy import PostgresPartitioningStrategy

class PostgresRangePartitioningStrategy(PostgresPartitioningStrategy, metaclass=abc.ABCMeta): ...
