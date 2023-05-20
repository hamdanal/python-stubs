from _typeshed import Incomplete

from .algorithms import bootstrap as bootstrap
from .external.kde import gaussian_kde as gaussian_kde

class KDE:
    bw_method: Incomplete
    bw_adjust: Incomplete
    gridsize: Incomplete
    cut: Incomplete
    clip: Incomplete
    cumulative: Incomplete
    support: Incomplete
    def __init__(
        self,
        *,
        bw_method: Incomplete | None = None,
        bw_adjust: int = 1,
        gridsize: int = 200,
        cut: int = 3,
        clip: Incomplete | None = None,
        cumulative: bool = False,
    ) -> None: ...
    def define_support(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None, cache: bool = True): ...
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None): ...

class Histogram:
    stat: Incomplete
    bins: Incomplete
    binwidth: Incomplete
    binrange: Incomplete
    discrete: Incomplete
    cumulative: Incomplete
    bin_kws: Incomplete
    def __init__(
        self,
        stat: str = "count",
        bins: str = "auto",
        binwidth: Incomplete | None = None,
        binrange: Incomplete | None = None,
        discrete: bool = False,
        cumulative: bool = False,
    ) -> None: ...
    def define_bin_params(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None, cache: bool = True): ...
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None): ...

class ECDF:
    stat: Incomplete
    complementary: Incomplete
    def __init__(self, stat: str = "proportion", complementary: bool = False) -> None: ...
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None): ...

class EstimateAggregator:
    estimator: Incomplete
    error_method: Incomplete
    error_level: Incomplete
    boot_kws: Incomplete
    def __init__(self, estimator, errorbar: Incomplete | None = None, **boot_kws) -> None: ...
    def __call__(self, data, var): ...
