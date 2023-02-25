from typing import ClassVar

from pandas import DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from seaborn._stats.base import Stat as Stat
from seaborn.external.version import Version as Version

class Perc(Stat):
    k: int | list[float]
    method: str
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, k, method) -> None: ...
