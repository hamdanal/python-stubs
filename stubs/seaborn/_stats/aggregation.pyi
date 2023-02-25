from collections.abc import Callable
from typing import ClassVar

from pandas import DataFrame as DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from seaborn._core.typing import Vector as Vector
from seaborn._statistics import EstimateAggregator as EstimateAggregator
from seaborn._stats.base import Stat as Stat

class Agg(Stat):
    func: str | Callable[[Vector], float]
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, func) -> None: ...

class Est(Stat):
    func: str | Callable[[Vector], float]
    errorbar: str | tuple[str, float]
    n_boot: int
    seed: int | None
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, func, errorbar, n_boot, seed) -> None: ...

class Rolling(Stat):
    def __call__(self, data, groupby, orient, scales) -> None: ...
