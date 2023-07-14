from _typeshed import Incomplete
from typing_extensions import Literal

from matplotlib.axes import Axes

from ._oldcore import VectorPlotter
from .axisgrid import FacetGrid

__all__ = ["relplot", "scatterplot", "lineplot"]

class _RelationalPlotter(VectorPlotter):
    sort: bool
    legend_title: str
    legend_data: dict[Incomplete, Incomplete]
    legend_order: list[Incomplete]
    def add_legend_data(self, ax: Axes) -> None: ...

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
        data: Incomplete | None = None,
        variables={},
        estimator: Incomplete | None = None,
        n_boot: Incomplete | None = None,
        seed: Incomplete | None = None,
        errorbar: Incomplete | None = None,
        sort: bool = True,
        orient: str = "x",
        err_style: Incomplete | None = None,
        err_kws: Incomplete | None = None,
        legend: Incomplete | None = None,
    ) -> None: ...
    def plot(self, ax: Axes, kws: dict[str, Incomplete]) -> None: ...

class _ScatterPlotter(_RelationalPlotter):
    legend: Incomplete | None
    def __init__(
        self, *, data: Incomplete | None = None, variables: dict[str, Incomplete] = {}, legend: Incomplete | None = None
    ) -> None: ...
    def plot(self, ax: Axes, kws: dict[str, Incomplete]) -> None: ...

def lineplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    size: Incomplete | None = None,
    style: Incomplete | None = None,
    units: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    sizes: Incomplete | None = None,
    size_order: Incomplete | None = None,
    size_norm: Incomplete | None = None,
    dashes: bool = True,
    markers: Incomplete | None = None,
    style_order: Incomplete | None = None,
    estimator: str = "mean",
    errorbar=("ci", 95),
    n_boot: int = 1000,
    seed: Incomplete | None = None,
    orient: str = "x",
    sort: bool = True,
    err_style: str = "band",
    err_kws: Incomplete | None = None,
    legend: Literal["auto", "brief", "full", False] = "auto",
    ci: str = "deprecated",
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def scatterplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    size: Incomplete | None = None,
    style: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    sizes: Incomplete | None = None,
    size_order: Incomplete | None = None,
    size_norm: Incomplete | None = None,
    markers: bool = True,
    style_order: Incomplete | None = None,
    legend: Literal["auto", "brief", "full", False] = "auto",
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def relplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    size: Incomplete | None = None,
    style: Incomplete | None = None,
    units: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    col_wrap: Incomplete | None = None,
    row_order: Incomplete | None = None,
    col_order: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    sizes: Incomplete | None = None,
    size_order: Incomplete | None = None,
    size_norm: Incomplete | None = None,
    markers: Incomplete | None = None,
    dashes: Incomplete | None = None,
    style_order: Incomplete | None = None,
    legend: Literal["auto", "brief", "full", False] = "auto",
    kind: Literal["scatter", "line"] = "scatter",
    height: float = 5,
    aspect: float = 1,
    facet_kws: Incomplete | None = None,
    **kwargs,
) -> FacetGrid: ...
