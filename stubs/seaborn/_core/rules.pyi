from collections import UserString
from typing_extensions import Literal

from pandas import Series

class VarType(UserString):
    allowed: tuple[str, ...]
    def __init__(self, data: str) -> None: ...
    def __eq__(self, other: str) -> bool: ...  # type: ignore[override]

def variable_type(
    vector: Series, boolean_type: Literal["numeric", "categorical", "boolean"] = "numeric", strict_boolean: bool = False
) -> VarType: ...
def categorical_order(vector: Series, order: list | None = None) -> list: ...
