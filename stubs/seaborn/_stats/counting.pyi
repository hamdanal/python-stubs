from typing import ClassVar

from numpy.typing import ArrayLike as ArrayLike
from pandas import DataFrame as DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from seaborn._stats.base import Stat as Stat

class Count(Stat):
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...

class Hist(Stat):
    stat: str
    bins: str | int | ArrayLike
    binwidth: float | None
    binrange: tuple[float, float] | None
    common_norm: bool | list[str]
    common_bins: bool | list[str]
    cumulative: bool
    discrete: bool
    def __post_init__(self) -> None: ...
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, stat, bins, binwidth, binrange, common_norm, common_bins, cumulative, discrete) -> None: ...
