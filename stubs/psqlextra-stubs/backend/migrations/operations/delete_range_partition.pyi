from psqlextra.backend.migrations.operations.delete_partition import PostgresDeletePartition

class PostgresDeleteRangePartition(PostgresDeletePartition):
    def database_backwards(self, app_label, schema_editor, from_state, to_state) -> None: ...
    def describe(self) -> str: ...
