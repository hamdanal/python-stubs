from collections.abc import Mapping
from typing import Any

from psqlextra.backend.migrations.state.model import PostgresModelState

class PostgresViewModelState(PostgresModelState):
    view_options: dict[str, Any]
    def __init__(self, *args, view_options: Mapping[str, Any] = {}, **kwargs) -> None: ...
