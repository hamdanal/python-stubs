from psqlextra.backend.migrations.operations.partition import PostgresPartitionOperation

class PostgresDeletePartition(PostgresPartitionOperation):
    def state_forwards(self, app_label, state) -> None: ...
