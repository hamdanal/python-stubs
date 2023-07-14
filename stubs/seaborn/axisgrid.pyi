from _typeshed import Incomplete
from collections.abc import Callable, Generator, Iterable, Mapping
from typing import Protocol, TypeVar
from typing_extensions import Concatenate, Literal, ParamSpec, Self

from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.legend import Legend
from numpy.typing import NDArray
from pandas import DataFrame, Series

__all__ = ["FacetGrid", "PairGrid", "JointGrid", "pairplot", "jointplot"]

_P = ParamSpec("_P")
_R = TypeVar("_R")

class _BaseGrid:
    def set(self, **kwargs) -> Self: ...
    @property
    def fig(self) -> Figure: ...
    @property
    def figure(self) -> Figure: ...
    def apply(self, func: Callable[Concatenate[Self, _P], object], *args: _P.args, **kwargs: _P.kwargs) -> Self: ...
    def pipe(self, func: Callable[Concatenate[Self, _P], _R], *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
    def savefig(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class Grid(_BaseGrid):
    def __init__(self) -> None: ...
    def tight_layout(self, *args: Incomplete, **kwargs: Incomplete) -> Self: ...
    def add_legend(
        self,
        legend_data: Mapping[str | tuple[Incomplete, str], Artist] | None = None,
        title: str | None = None,
        label_order: list[str] | None = None,
        adjust_subtitles: bool = False,
        **kwargs: Incomplete,
    ) -> Self: ...
    @property
    def legend(self) -> Legend | None: ...
    def tick_params(self, axis: str = "both", **kwargs: Incomplete) -> Self: ...

class _FacetGridPlotFunc(Protocol):
    def __call__(self, *args: Incomplete, color: Incomplete, label: Incomplete = ..., **kwargs: Incomplete) -> object: ...

class FacetGrid(Grid):
    data: DataFrame
    row_names: list[str]
    col_names: list[str]
    hue_names: list[str] | None
    hue_kws: dict[str, Incomplete]
    def __init__(
        self,
        data: DataFrame,
        *,
        row: str | None = None,
        col: str | None = None,
        hue: str | None = None,
        col_wrap: int | None = None,
        sharex: bool | Literal["col", "row"] = True,
        sharey: bool | Literal["col", "row"] = True,
        height: float = 3,
        aspect: float = 1,
        palette: Incomplete | None = None,
        row_order: Iterable[str] | None = None,
        col_order: Iterable[str] | None = None,
        hue_order: Iterable[str] | None = None,
        hue_kws: dict[str, Incomplete] | None = None,
        dropna: bool = False,
        legend_out: bool = True,
        despine: bool = True,
        margin_titles: bool = False,
        xlim: tuple[Incomplete, ...] | None = None,
        ylim: tuple[Incomplete, ...] | None = None,
        subplot_kws: Incomplete | None = None,
        gridspec_kws: Incomplete | None = None,
    ) -> None: ...
    def facet_data(self) -> Generator[tuple[tuple[int, int, int], DataFrame], None, None]: ...
    def map(self, func: _FacetGridPlotFunc, *args: Incomplete, **kwargs: Incomplete) -> Self: ...
    def map_dataframe(self, func: _FacetGridPlotFunc, *args: Incomplete, **kwargs: Incomplete) -> Self: ...
    def facet_axis(self, row_i: int, col_j: int, modify_state: bool = True) -> Axes: ...
    def despine(self, **kwargs: Incomplete) -> Self: ...
    def set_axis_labels(
        self, x_var: Incomplete | None = None, y_var: Incomplete | None = None, clear_inner: bool = True, **kwargs: Incomplete
    ) -> Self: ...
    def set_xlabels(self, label: Incomplete | None = None, clear_inner: bool = True, **kwargs: Incomplete) -> Self: ...
    def set_ylabels(self, label: Incomplete | None = None, clear_inner: bool = True, **kwargs: Incomplete) -> Self: ...
    def set_xticklabels(self, labels: Incomplete | None = None, step: Incomplete | None = None, **kwargs: Incomplete) -> Self: ...
    def set_yticklabels(self, labels: Incomplete | None = None, **kwargs: Incomplete) -> Self: ...
    def set_titles(
        self, template: str | None = None, row_template: str | None = None, col_template: str | None = None, **kwargs: Incomplete
    ) -> Self: ...
    def refline(
        self,
        *,
        x: float | None = None,
        y: float | None = None,
        color: str | tuple[float, float, float] = ".5",
        linestyle: str = "--",
        **line_kws: Incomplete,
    ) -> Self: ...
    @property
    def axes(self) -> NDArray[Incomplete]: ...  # array of `Axes`
    @property
    def ax(self) -> Axes: ...
    @property
    def axes_dict(self) -> dict[Incomplete, Axes]: ...

class _PairGridPlotFunc(Protocol):
    def __call__(
        self,
        x: NDArray[Incomplete],
        y: NDArray[Incomplete],
        *args: Incomplete,
        color: Incomplete,
        label: Incomplete,
        **kwargs: Incomplete,
    ) -> object: ...

class PairGrid(Grid):
    x_vars: list[str]
    y_vars: list[str]
    square_grid: bool
    axes: NDArray[Incomplete]  # two-dimensional array of `Axes`
    data: DataFrame
    diag_sharey: bool
    diag_vars: NDArray[Incomplete] | None  # array of `str`
    diag_axes: NDArray[Incomplete] | None  # array of `Axes`
    hue_names: list[str]
    hue_vals: Series[Incomplete]
    hue_kws: dict[str, Incomplete]
    palette: Incomplete
    def __init__(
        self,
        data: DataFrame,
        *,
        hue: str | None = None,
        vars: Iterable[str] | None = None,
        x_vars: Iterable[str] | None = None,
        y_vars: Iterable[str] | None = None,
        hue_order: Iterable[str] | None = None,
        palette: Incomplete | None = None,
        hue_kws: dict[str, Incomplete] | None = None,
        corner: bool = False,
        diag_sharey: bool = True,
        height: float = 2.5,
        aspect: float = 1,
        layout_pad: float = 0.5,
        despine: bool = True,
        dropna: bool = False,
    ) -> None: ...
    def map(self, func: _PairGridPlotFunc, **kwargs: Incomplete) -> Self: ...
    def map_lower(self, func: _PairGridPlotFunc, **kwargs: Incomplete) -> Self: ...
    def map_upper(self, func: _PairGridPlotFunc, **kwargs: Incomplete) -> Self: ...
    def map_offdiag(self, func: _PairGridPlotFunc, **kwargs: Incomplete) -> Self: ...
    def map_diag(self, func: _PairGridPlotFunc, **kwargs: Incomplete) -> Self: ...

class JointGrid(_BaseGrid):
    ax_joint: Axes
    ax_marg_x: Axes
    ax_marg_y: Axes
    x: Series[Incomplete]
    y: Series[Incomplete]
    hue: Series[Incomplete]
    def __init__(
        self,
        data: Incomplete | None = None,
        *,
        x: Incomplete | None = None,
        y: Incomplete | None = None,
        hue: Incomplete | None = None,
        height: float = 6,
        ratio: float = 5,
        space: float = 0.2,
        palette: Incomplete | None = None,
        hue_order: Iterable[str] | None = None,
        hue_norm: Incomplete | None = None,
        dropna: bool = False,
        xlim: Incomplete | None = None,
        ylim: Incomplete | None = None,
        marginal_ticks: bool = False,
    ) -> None: ...
    def plot(self, joint_func: Callable[..., object], marginal_func: Callable[..., object], **kwargs: Incomplete) -> Self: ...
    def plot_joint(self, func: Callable[..., object], **kwargs: Incomplete) -> Self: ...
    def plot_marginals(self, func: Callable[..., object], **kwargs: Incomplete) -> Self: ...
    def refline(
        self,
        *,
        x: float | None = None,
        y: float | None = None,
        joint: bool = True,
        marginal: bool = True,
        color: str | tuple[float, float, float] = ".5",
        linestyle: str = "--",
        **line_kws: Incomplete,
    ) -> Self: ...
    def set_axis_labels(self, xlabel: str = "", ylabel: str = "", **kwargs: Incomplete) -> Self: ...

def pairplot(
    data: DataFrame,
    *,
    hue: str | None = None,
    hue_order: Iterable[str] | None = None,
    palette: Incomplete | None = None,
    vars: Iterable[str] | None = None,
    x_vars: Iterable[str] | None = None,
    y_vars: Iterable[str] | None = None,
    kind: Literal["scatter", "kde", "hist", "reg"] = "scatter",
    diag_kind: Literal["auto", "hist", "kde"] | None = "auto",
    markers: Incomplete | None = None,
    height: float = 2.5,
    aspect: float = 1,
    corner: bool = False,
    dropna: bool = False,
    plot_kws: dict[str, Incomplete] | None = None,
    diag_kws: dict[str, Incomplete] | None = None,
    grid_kws: dict[str, Incomplete] | None = None,
    size: float | None = None,
) -> PairGrid: ...
def jointplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    kind: Literal["scatter", "kde", "hist", "hex", "reg", "resid"] = "scatter",
    height: float = 6,
    ratio: float = 5,
    space: float = 0.2,
    dropna: bool = False,
    xlim: Incomplete | None = None,
    ylim: Incomplete | None = None,
    color: str | tuple[float, float, float] | None = None,
    palette: Incomplete | None = None,
    hue_order: Iterable[str] | None = None,
    hue_norm: Incomplete | None = None,
    marginal_ticks: bool = False,
    joint_kws: dict[str, Incomplete] | None = None,
    marginal_kws: dict[str, Incomplete] | None = None,
    **kwargs: Incomplete,
) -> JointGrid: ...
