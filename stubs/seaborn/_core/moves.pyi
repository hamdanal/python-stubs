from collections.abc import Callable
from dataclasses import dataclass
from typing import ClassVar

from pandas import DataFrame
from seaborn._core.groupby import GroupBy
from seaborn._core.scales import Scale
from seaborn._core.typing import Default

default: Default

@dataclass
class Move:
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...

@dataclass
class Jitter(Move):
    width: float | Default = ...
    x: float = 0
    y: float = 0
    seed: int | None = ...  # None # pytype parse error

@dataclass
class Dodge(Move):
    empty: str = "keep"
    gap: float = 0
    by: list[str] | None = ...  # None # pytype parse error

@dataclass
class Stack(Move): ...

@dataclass
class Shift(Move):
    x: float = 0
    y: float = 0

@dataclass
class Norm(Move):
    func: Callable | str = "max"
    where: str | None = ...  # None # pytype parse error
    by: list[str] | None = ...  # None # pytype parse error
    percent: bool = False
