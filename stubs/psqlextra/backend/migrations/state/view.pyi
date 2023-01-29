from _typeshed import Incomplete

from .model import PostgresModelState

class PostgresViewModelState(PostgresModelState):
    view_options: Incomplete
    def __init__(self, *args, view_options=..., **kwargs) -> None: ...
