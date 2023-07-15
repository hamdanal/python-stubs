from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import Literal

import numpy as np
import pandas as pd
from matplotlib.axes import Axes

from .axisgrid import FacetGrid

__all__ = ["lmplot", "regplot", "residplot"]

class _LinearPlotter:
    data: Incomplete
    def establish_variables(self, data, **kws) -> None: ...
    def dropna(self, *vars) -> None: ...
    def plot(self, ax: Axes) -> None: ...

class _RegressionPlotter(_LinearPlotter):
    x_estimator: Incomplete
    ci: Incomplete
    x_ci: Incomplete
    n_boot: Incomplete
    seed: Incomplete
    scatter: Incomplete
    fit_reg: Incomplete
    order: Incomplete
    logistic: Incomplete
    lowess: Incomplete
    robust: Incomplete
    logx: Incomplete
    truncate: Incomplete
    x_jitter: Incomplete
    y_jitter: Incomplete
    color: Incomplete
    label: Incomplete
    x: Incomplete
    y: Incomplete
    x_discrete: Incomplete
    x_range: Incomplete
    def __init__(
        self,
        x,
        y,
        data: Incomplete | None = None,
        x_estimator: Incomplete | None = None,
        x_bins: Incomplete | None = None,
        x_ci: str = "ci",
        scatter: bool = True,
        fit_reg: bool = True,
        ci: int | None = 95,
        n_boot: int = 1000,
        units: Incomplete | None = None,
        seed: Incomplete | None = None,
        order: int = 1,
        logistic: bool = False,
        lowess: bool = False,
        robust: bool = False,
        logx: bool = False,
        x_partial: Incomplete | None = None,
        y_partial: Incomplete | None = None,
        truncate: bool = False,
        dropna: bool = True,
        x_jitter: Incomplete | None = None,
        y_jitter: Incomplete | None = None,
        color: Incomplete | None = None,
        label: Incomplete | None = None,
    ) -> None: ...
    @property
    def scatter_data(self) -> tuple[Incomplete, Incomplete]: ...
    @property
    def estimate_data(self) -> tuple[list[Incomplete], list[Incomplete], list[Incomplete]]: ...
    def fit_regression(
        self, ax: Axes | None = None, x_range: Incomplete | None = None, grid: Incomplete | None = None
    ) -> tuple[Incomplete, Incomplete, Incomplete]: ...
    def fit_fast(self, grid) -> tuple[Incomplete, Incomplete]: ...
    def fit_poly(self, grid, order: int) -> tuple[Incomplete, Incomplete]: ...
    def fit_statsmodels(self, grid, model, **kwargs) -> tuple[Incomplete, Incomplete]: ...
    def fit_lowess(self) -> tuple[Incomplete, Incomplete]: ...
    def fit_logx(self, grid) -> tuple[Incomplete, Incomplete]: ...
    def bin_predictor(self, bins) -> tuple[Incomplete, Incomplete]: ...
    def regress_out(self, a, b) -> np.ndarray: ...
    def plot(self, ax: Axes, scatter_kws: dict[str, Incomplete] | None, line_kws: dict[str, Incomplete] | None) -> None: ...  # type: ignore[override]
    def scatterplot(self, ax: Axes, kws: dict[str, Incomplete]) -> None: ...
    def lineplot(self, ax: Axes, kws: dict[str, Incomplete]) -> None: ...

def lmplot(
    data: Incomplete | None = None,
    *,
    x: str | None = None,
    y: str | None = None,
    hue: str | None = None,
    col: str | None = None,
    row: str | None = None,
    palette: Incomplete | None = None,
    col_wrap: int | None = None,
    height: float = 5,
    aspect: float = 1,
    markers: str = "o",
    sharex: bool | Literal["col", "row"] | None = None,
    sharey: bool | Literal["col", "row"] | None = None,
    hue_order: Iterable[str] | None = None,
    col_order: Iterable[str] | None = None,
    row_order: Iterable[str] | None = None,
    legend: bool = True,
    legend_out: Incomplete | None = None,
    x_estimator: Incomplete | None = None,
    x_bins: Incomplete | None = None,
    x_ci: Literal["ci", "sd"] | int | None = "ci",
    scatter: bool = True,
    fit_reg: bool = True,
    ci: int | None = 95,
    n_boot: int = 1000,
    units: str | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    order: int = 1,
    logistic: bool = False,
    lowess: bool = False,
    robust: bool = False,
    logx: bool = False,
    x_partial: str | None = None,
    y_partial: str | None = None,
    truncate: bool = True,
    x_jitter: float | None = None,
    y_jitter: float | None = None,
    scatter_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
    facet_kws: dict[str, Any] | None = None,
) -> FacetGrid: ...
def regplot(
    data: pd.DataFrame | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    x_estimator: Incomplete | None = None,
    x_bins: Incomplete | None = None,
    x_ci: Literal["ci", "sd"] | int | None = "ci",
    scatter: bool = True,
    fit_reg: bool = True,
    ci: int | None = 95,
    n_boot: int = 1000,
    units: str | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    order: int = 1,
    logistic: bool = False,
    lowess: bool = False,
    robust: bool = False,
    logx: bool = False,
    x_partial: str | None = None,
    y_partial: str | None = None,
    truncate: bool = True,
    dropna: bool = True,
    x_jitter: float | None = None,
    y_jitter: float | None = None,
    label: str | None = None,
    color: Incomplete | None = None,
    marker: str = "o",
    scatter_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
    ax: Axes | None = None,
) -> Axes: ...
def residplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    x_partial: Incomplete | None = None,
    y_partial: Incomplete | None = None,
    lowess: bool = False,
    order: int = 1,
    robust: bool = False,
    dropna: bool = True,
    label: str | None = None,
    color: Incomplete | None = None,
    scatter_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
    ax: Axes | None = None,
) -> Axes: ...
