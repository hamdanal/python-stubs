from _typeshed import Incomplete
from collections.abc import Callable

from pandas import DataFrame as DataFrame, Index as Index, MultiIndex as MultiIndex
from seaborn._core.rules import categorical_order as categorical_order

class GroupBy:
    order: Incomplete
    def __init__(self, order: list[str] | dict[str, list | None]) -> None: ...
    def agg(self, data: DataFrame, *args, **kwargs) -> DataFrame: ...
    def apply(self, data: DataFrame, func: Callable[..., DataFrame], *args, **kwargs) -> DataFrame: ...
