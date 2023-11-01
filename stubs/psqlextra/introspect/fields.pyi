from typing import Any

from django.db.models import Field, Model

def inspect_model_local_concrete_fields(model: type[Model]) -> list[Field[Any, Any]]: ...
