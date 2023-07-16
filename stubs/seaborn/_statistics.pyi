from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any

import pandas as pd

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
    bin_kws: dict[str, Any] | None
    def __init__(
        self,
        stat: str = "count",
        bins: Incomplete = "auto",
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
    estimator: str | Callable
    error_method: str | Callable | None
    error_level: float | None
    boot_kws: dict[str, Any]
    def __init__(
        self, estimator: str | Callable, errorbar: str | tuple[str, float] | Callable | None = None, **boot_kws: Any
    ) -> None: ...
    def __call__(self, data, var) -> pd.Series: ...
