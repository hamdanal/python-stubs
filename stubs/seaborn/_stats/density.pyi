from collections.abc import Callable

from pandas import DataFrame as DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from seaborn._stats.base import Stat as Stat
from seaborn.external.kde import gaussian_kde as gaussian_kde

class KDE(Stat):
    bw_adjust: float
    bw_method: str | float | Callable[[gaussian_kde], float]
    common_norm: bool | list[str]
    common_grid: bool | list[str]
    gridsize: int | None
    cut: float
    cumulative: bool
    def __post_init__(self) -> None: ...
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, bw_adjust, bw_method, common_norm, common_grid, gridsize, cut, cumulative) -> None: ...
