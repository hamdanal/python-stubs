from _typeshed import Incomplete
from collections.abc import Callable
from typing import ClassVar

from pandas import DataFrame as DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from seaborn._core.typing import Default as Default

default: Incomplete

class Move:
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...

class Jitter(Move):
    width: float | Default
    x: float
    y: float
    seed: int | None
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, width, x, y, seed) -> None: ...

class Dodge(Move):
    empty: str
    gap: float
    by: list[str] | None
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, empty, gap, by) -> None: ...

class Stack(Move):
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...

class Shift(Move):
    x: float
    y: float
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, x, y) -> None: ...

class Norm(Move):
    func: Callable | str
    where: str | None
    by: list[str] | None
    percent: bool
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, func, where, by, percent) -> None: ...
