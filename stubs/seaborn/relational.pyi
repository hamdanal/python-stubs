from _typeshed import Incomplete

from ._oldcore import VectorPlotter

__all__ = ["relplot", "scatterplot", "lineplot"]

class _RelationalPlotter(VectorPlotter):
    wide_structure: Incomplete
    sort: bool
    legend_title: Incomplete
    legend_data: Incomplete
    legend_order: Incomplete
    def add_legend_data(self, ax) -> None: ...

class _LinePlotter(_RelationalPlotter):
    estimator: Incomplete
    errorbar: Incomplete
    n_boot: Incomplete
    seed: Incomplete
    sort: Incomplete
    orient: Incomplete
    err_style: Incomplete
    err_kws: Incomplete
    legend: Incomplete
    def __init__(
        self,
        *,
        data: Incomplete | None = ...,
        variables=...,
        estimator: Incomplete | None = ...,
        n_boot: Incomplete | None = ...,
        seed: Incomplete | None = ...,
        errorbar: Incomplete | None = ...,
        sort: bool = ...,
        orient: str = ...,
        err_style: Incomplete | None = ...,
        err_kws: Incomplete | None = ...,
        legend: Incomplete | None = ...,
    ) -> None: ...
    def plot(self, ax, kws) -> None: ...

class _ScatterPlotter(_RelationalPlotter):
    legend: Incomplete
    def __init__(self, *, data: Incomplete | None = ..., variables=..., legend: Incomplete | None = ...) -> None: ...
    def plot(self, ax, kws) -> None: ...

def lineplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    size: Incomplete | None = ...,
    style: Incomplete | None = ...,
    units: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    sizes: Incomplete | None = ...,
    size_order: Incomplete | None = ...,
    size_norm: Incomplete | None = ...,
    dashes: bool = ...,
    markers: Incomplete | None = ...,
    style_order: Incomplete | None = ...,
    estimator: str = ...,
    errorbar=...,
    n_boot: int = ...,
    seed: Incomplete | None = ...,
    orient: str = ...,
    sort: bool = ...,
    err_style: str = ...,
    err_kws: Incomplete | None = ...,
    legend: str = ...,
    ci: str = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def scatterplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    size: Incomplete | None = ...,
    style: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    sizes: Incomplete | None = ...,
    size_order: Incomplete | None = ...,
    size_norm: Incomplete | None = ...,
    markers: bool = ...,
    style_order: Incomplete | None = ...,
    legend: str = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def relplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    size: Incomplete | None = ...,
    style: Incomplete | None = ...,
    units: Incomplete | None = ...,
    row: Incomplete | None = ...,
    col: Incomplete | None = ...,
    col_wrap: Incomplete | None = ...,
    row_order: Incomplete | None = ...,
    col_order: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    sizes: Incomplete | None = ...,
    size_order: Incomplete | None = ...,
    size_norm: Incomplete | None = ...,
    markers: Incomplete | None = ...,
    dashes: Incomplete | None = ...,
    style_order: Incomplete | None = ...,
    legend: str = ...,
    kind: str = ...,
    height: int = ...,
    aspect: int = ...,
    facet_kws: Incomplete | None = ...,
    **kwargs,
): ...
