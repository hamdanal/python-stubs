from _typeshed import Incomplete
from collections import UserString
from typing_extensions import Literal

from pandas import Series as Series

class VarType(UserString):
    allowed: Incomplete
    def __init__(self, data) -> None: ...
    def __eq__(self, other): ...

def variable_type(
    vector: Series, boolean_type: Literal["numeric", "categorical", "boolean"] = "numeric", strict_boolean: bool = False
) -> VarType: ...
def categorical_order(vector: Series, order: list | None = None) -> list: ...
