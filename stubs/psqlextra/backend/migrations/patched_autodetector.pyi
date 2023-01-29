from _typeshed import Incomplete
from collections.abc import Generator

from django.db.migrations import AddField, AlterField, CreateModel, DeleteModel, RemoveField, RenameField
from django.db.migrations.operations.base import Operation as Operation

add_operation: Incomplete

class AddOperationHandler:
    autodetector: Incomplete
    app_label: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, autodetector, app_label, args, kwargs) -> None: ...
    def add(self, operation): ...
    def add_field(self, operation: AddField): ...
    def remove_field(self, operation: RemoveField): ...
    def alter_field(self, operation: AlterField): ...
    def rename_field(self, operation: RenameField): ...
    def add_create_model(self, operation: CreateModel): ...
    def add_delete_model(self, operation: DeleteModel): ...
    def add_create_partitioned_model(self, operation: CreateModel): ...
    def add_delete_partitioned_model(self, operation: DeleteModel): ...
    def add_create_view_model(self, operation: CreateModel): ...
    def add_delete_view_model(self, operation: DeleteModel): ...
    def add_create_materialized_view_model(self, operation: CreateModel): ...
    def add_delete_materialized_view_model(self, operation: DeleteModel): ...

def patched_autodetector() -> Generator[None, None, Incomplete]: ...
