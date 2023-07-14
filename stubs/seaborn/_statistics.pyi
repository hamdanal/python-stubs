from _typeshed import Incomplete

import pandas as pd

from .algorithms import bootstrap as bootstrap
from .external.kde import gaussian_kde as gaussian_kde

class KDE:
    bw_method: Incomplete
    bw_adjust: float
    gridsize: int
    cut: float
    clip: tuple[Incomplete, Incomplete]
    cumulative: bool
    support: Incomplete
    def __init__(
        self,
        *,
        bw_method: Incomplete | None = None,
        bw_adjust: float = 1,
        gridsize: int = 200,
        cut: float = 3,
        clip: tuple[Incomplete, Incomplete] | None = None,
        cumulative: bool = False,
    ) -> None: ...
    def define_support(
        self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None, cache: bool = True
    ) -> Incomplete: ...
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None) -> tuple[Incomplete, Incomplete]: ...

class Histogram:
    stat: str
    bins: Incomplete
    binwidth: float | tuple[float, float] | None
    binrange: tuple[Incomplete, Incomplete] | None
    discrete: bool | tuple[bool, bool]
    cumulative: bool
    bin_kws: Incomplete
    def __init__(
        self,
        stat: str = "count",
        bins: str | float | Incomplete = "auto",
        binwidth: float | tuple[float, float] | None = None,
        binrange: tuple[Incomplete, Incomplete] | None = None,
        discrete: bool | tuple[bool, bool] = False,
        cumulative: bool = False,
    ) -> None: ...
    def define_bin_params(
        self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None, cache: bool = True
    ) -> dict[str, Incomplete]: ...
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None) -> tuple[Incomplete, Incomplete]: ...

class ECDF:
    stat: str
    complementary: bool
    def __init__(self, stat: str = "proportion", complementary: bool = False) -> None: ...
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None) -> tuple[Incomplete, Incomplete]: ...

class EstimateAggregator:
    estimator: Incomplete
    error_method: Incomplete
    error_level: Incomplete
    boot_kws: Incomplete
    def __init__(self, estimator, errorbar: Incomplete | None = None, **boot_kws) -> None: ...
    def __call__(self, data, var) -> pd.Series: ...
