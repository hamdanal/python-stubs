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
        bw_method: Incomplete | None = ...,
        bw_adjust: int = ...,
        gridsize: int = ...,
        cut: int = ...,
        clip: Incomplete | None = ...,
        cumulative: bool = ...,
    ) -> None: ...
    def define_support(self, x1, x2: Incomplete | None = ..., weights: Incomplete | None = ..., cache: bool = ...): ...
    def __call__(self, x1, x2: Incomplete | None = ..., weights: Incomplete | None = ...): ...

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
        stat: str = ...,
        bins: str = ...,
        binwidth: Incomplete | None = ...,
        binrange: Incomplete | None = ...,
        discrete: bool = ...,
        cumulative: bool = ...,
    ) -> None: ...
    def define_bin_params(self, x1, x2: Incomplete | None = ..., weights: Incomplete | None = ..., cache: bool = ...): ...
    def __call__(self, x1, x2: Incomplete | None = ..., weights: Incomplete | None = ...): ...

class ECDF:
    stat: Incomplete
    complementary: Incomplete
    def __init__(self, stat: str = ..., complementary: bool = ...) -> None: ...
    def __call__(self, x1, x2: Incomplete | None = ..., weights: Incomplete | None = ...): ...

class EstimateAggregator:
    estimator: Incomplete
    error_method: Incomplete
    error_level: Incomplete
    boot_kws: Incomplete
    def __init__(self, estimator, errorbar: Incomplete | None = ..., **boot_kws) -> None: ...
    def __call__(self, data, var): ...
