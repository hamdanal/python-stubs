from django.db.migrations.state import ModelState

from psqlextra.models import PostgresModel

class PostgresModelState(ModelState):
    @classmethod
    def from_model(cls, model: PostgresModel, *args, **kwargs) -> PostgresModelState: ...  # type: ignore[override]
    def clone(self) -> PostgresModelState: ...
    def render(self, apps): ...
