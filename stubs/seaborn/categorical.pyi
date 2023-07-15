from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import Any, TypeVar
from typing_extensions import Literal

import numpy as np
from matplotlib.axes import Axes
from seaborn.axisgrid import FacetGrid
from seaborn.relational import _RelationalPlotter

from .external.kde import gaussian_kde

__all__ = ["catplot", "stripplot", "swarmplot", "boxplot", "violinplot", "boxenplot", "pointplot", "barplot", "countplot"]

_T = TypeVar("_T")

class _CategoricalPlotterNew(_RelationalPlotter):
    orient: Literal["v", "h"]
    legend: Incomplete
    def __init__(
        self,
        data: Incomplete | None = None,
        variables={},
        order: Incomplete | None = None,
        orient: Incomplete | None = None,
        require_numeric: bool = False,
        legend: Incomplete = "auto",
    ) -> None: ...
    @property
    def cat_axis(self) -> Literal["x", "y"]: ...
    def plot_strips(self, jitter, dodge, color, edgecolor, plot_kws) -> None: ...
    def plot_swarms(self, dodge, color, edgecolor, warn_thresh, plot_kws) -> None: ...

class _CategoricalFacetPlotter(_CategoricalPlotterNew): ...

class _CategoricalPlotter:
    width: float
    default_palette: str
    require_numeric: bool
    orient: Literal["v", "h"]
    plot_data: Incomplete
    group_label: Incomplete
    value_label: Incomplete
    group_names: Incomplete
    plot_hues: list[Incomplete] | None
    hue_title: Incomplete
    hue_names: list[Incomplete] | None
    plot_units: Incomplete
    def establish_variables(
        self,
        x: Incomplete | None = None,
        y: Incomplete | None = None,
        hue: Incomplete | None = None,
        data: Incomplete | None = None,
        orient: Incomplete | None = None,
        order: Incomplete | None = None,
        hue_order: Incomplete | None = None,
        units: Incomplete | None = None,
    ) -> None: ...
    colors: Incomplete
    gray: Incomplete
    def establish_colors(self, color, palette, saturation) -> None: ...
    @property
    def hue_offsets(self) -> np.ndarray: ...
    @property
    def nested_width(self) -> float: ...
    def annotate_axes(self, ax: Axes) -> None: ...
    def add_legend_data(self, ax: Axes, color, label) -> None: ...

class _BoxPlotter(_CategoricalPlotter):
    dodge: Incomplete
    fliersize: Incomplete
    linewidth: Incomplete
    def __init__(
        self, x, y, hue, data, order, hue_order, orient, color, palette, saturation, width, dodge, fliersize, linewidth
    ) -> None: ...
    def draw_boxplot(self, ax, kws) -> None: ...
    def restyle_boxplot(self, artist_dict, color, props) -> None: ...
    def plot(self, ax, boxplot_kws) -> None: ...

class _ViolinPlotter(_CategoricalPlotter):
    gridsize: Incomplete
    dodge: Incomplete
    inner: Incomplete
    split: Incomplete
    linewidth: Incomplete
    def __init__(
        self,
        x,
        y,
        hue,
        data,
        order,
        hue_order,
        bw,
        cut,
        scale,
        scale_hue,
        gridsize,
        width,
        inner: str | None,
        split,
        dodge,
        orient,
        linewidth,
        color,
        palette,
        saturation,
    ) -> None: ...
    support: Incomplete
    density: Incomplete
    def estimate_densities(self, bw, cut, scale, scale_hue, gridsize) -> None: ...
    def fit_kde(self, x, bw) -> tuple[gaussian_kde, Incomplete]: ...
    def kde_support(self, x, bw, cut, gridsize) -> np.ndarray: ...
    def scale_area(self, density, max_density, scale_hue) -> None: ...
    def scale_width(self, density) -> None: ...
    def scale_count(self, density, counts, scale_hue) -> None: ...
    @property
    def dwidth(self) -> Incomplete: ...
    def draw_violins(self, ax: Axes) -> None: ...
    def draw_single_observation(self, ax: Axes, at_group, at_quant, density) -> None: ...
    def draw_box_lines(self, ax: Axes, data, center) -> None: ...
    def draw_quartiles(self, ax: Axes, data, support, density, center, split: bool = False) -> None: ...
    def draw_points(self, ax: Axes, data, center) -> None: ...
    def draw_stick_lines(self, ax: Axes, data, support, density, center, split: bool = False) -> None: ...
    def draw_to_density(self, ax: Axes, center, val, support, density, split, **kws) -> None: ...
    def plot(self, ax: Axes) -> None: ...

class _CategoricalStatPlotter(_CategoricalPlotter):
    require_numeric: bool
    statistic: np.ndarray
    confint: np.ndarray
    @property
    def nested_width(self) -> float: ...
    def estimate_statistic(self, estimator, errorbar, n_boot, seed) -> None: ...
    def draw_confints(
        self, ax, at_group, confint, colors, errwidth: Incomplete | None = None, capsize: Incomplete | None = None, **kws
    ) -> None: ...

class _BarPlotter(_CategoricalStatPlotter):
    dodge: Incomplete
    errcolor: Incomplete
    errwidth: Incomplete
    capsize: Incomplete
    def __init__(
        self,
        x,
        y,
        hue,
        data,
        order,
        hue_order,
        estimator,
        errorbar: str | tuple[str, float] | Callable,
        n_boot: int,
        units,
        seed,
        orient,
        color,
        palette,
        saturation,
        width,
        errcolor,
        errwidth,
        capsize,
        dodge,
    ) -> None: ...
    def draw_bars(self, ax, kws) -> None: ...
    def plot(self, ax, bar_kws) -> None: ...

class _PointPlotter(_CategoricalStatPlotter):
    default_palette: str
    colors: Incomplete
    markers: Incomplete
    linestyles: Incomplete
    dodge: Incomplete
    join: Incomplete
    scale: Incomplete
    errwidth: Incomplete
    capsize: Incomplete
    label: Incomplete
    def __init__(
        self,
        x,
        y,
        hue,
        data,
        order,
        hue_order,
        estimator,
        errorbar,
        n_boot,
        units,
        seed,
        markers,
        linestyles,
        dodge,
        join,
        scale,
        orient,
        color,
        palette,
        errwidth,
        capsize,
        label,
    ) -> None: ...
    @property
    def hue_offsets(self) -> np.ndarray: ...
    def draw_points(self, ax) -> None: ...
    def plot(self, ax) -> None: ...

class _CountPlotter(_BarPlotter):
    require_numeric: bool

class _LVPlotter(_CategoricalPlotter):
    width: Incomplete
    dodge: Incomplete
    saturation: Incomplete
    k_depth: Incomplete
    linewidth: Incomplete
    scale: Incomplete
    outlier_prop: Incomplete
    trust_alpha: Incomplete
    showfliers: Incomplete
    def __init__(
        self,
        x,
        y,
        hue,
        data,
        order,
        hue_order,
        orient,
        color,
        palette,
        saturation,
        width,
        dodge,
        k_depth,
        linewidth,
        scale,
        outlier_prop,
        trust_alpha,
        showfliers: bool = True,
    ) -> None: ...
    def draw_letter_value_plot(
        self, ax, box_kws: Incomplete | None = None, flier_kws: Incomplete | None = None, line_kws: Incomplete | None = None
    ) -> None: ...
    def plot(self, ax, box_kws, flier_kws, line_kws) -> None: ...

def boxplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    dodge: bool = True,
    fliersize: float = 5,
    linewidth: Incomplete | None = None,
    whis: float = 1.5,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def violinplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    bw: str = "scott",
    cut: int = 2,
    scale: str = "area",
    scale_hue: bool = True,
    gridsize: int = 100,
    width: float = 0.8,
    inner: str = "box",
    split: bool = False,
    dodge: bool = True,
    orient: Incomplete | None = None,
    linewidth: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    saturation: float = 0.75,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def boxenplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    dodge: bool = True,
    k_depth: str = "tukey",
    linewidth: Incomplete | None = None,
    scale: str = "exponential",
    outlier_prop: float = 0.007,
    trust_alpha: float = 0.05,
    showfliers: bool = True,
    ax: Axes | None = None,
    box_kws: Incomplete | None = None,
    flier_kws: Incomplete | None = None,
    line_kws: Incomplete | None = None,
) -> Axes: ...
def stripplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    jitter: bool = True,
    dodge: bool = False,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    size: float = 5,
    edgecolor: str = "gray",
    linewidth: float = 0,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    legend: str = "auto",
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def swarmplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    dodge: bool = False,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    size: float = 5,
    edgecolor: str = "gray",
    linewidth: float = 0,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    legend: str = "auto",
    warn_thresh: float = 0.05,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def barplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Iterable[str] | None = None,
    hue_order: Iterable[str] | None = None,
    estimator: str | Callable = "mean",
    errorbar: str | tuple[str, float] | Callable = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    errcolor: Incomplete = ".26",
    errwidth: float | None = None,
    capsize: float | None = None,
    dodge: bool = True,
    ci: str = "deprecated",
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def pointplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    estimator: str | Callable = "mean",
    errorbar: str | tuple[str, float] | Callable = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    markers: str = "o",
    linestyles: str = "-",
    dodge: bool = False,
    join: bool = True,
    scale: float = 1,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    errwidth: Incomplete | None = None,
    ci: str = "deprecated",
    capsize: Incomplete | None = None,
    label: Incomplete | None = None,
    ax: Axes | None = None,
) -> Axes: ...
def countplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    dodge: bool = True,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def catplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    col_wrap: int | None = None,
    estimator: str | Callable = "mean",
    errorbar: str | tuple[str, float] | Callable = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    order: Iterable[str] | None = None,
    hue_order: Iterable[str] | None = None,
    row_order: Iterable[str] | None = None,
    col_order: Iterable[str] | None = None,
    height: float = 5,
    aspect: float = 1,
    kind: str = "strip",
    native_scale: bool = False,
    formatter: Callable | None = None,
    orient: Literal["v", "h"] | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    legend: str | bool = "auto",
    legend_out: bool = True,
    sharex: bool = True,
    sharey: bool = True,
    margin_titles: bool = False,
    facet_kws: dict[str, Any] | None = None,
    ci: str = "deprecated",
    **kwargs,
) -> FacetGrid: ...

class Beeswarm:
    orient: Literal["v", "h"]
    width: float
    warn_thresh: float
    def __init__(self, orient: str = "v", width: float = 0.8, warn_thresh: float = 0.05) -> None: ...
    def __call__(self, points, center) -> None: ...
    def beeswarm(self, orig_xyr) -> np.ndarray: ...
    def could_overlap(self, xyr_i, swarm) -> np.ndarray: ...
    def position_candidates(self, xyr_i, neighbors) -> np.ndarray: ...
    def first_non_overlapping_candidate(self, candidates, neighbors) -> Incomplete: ...
    def add_gutters(self, points: _T, center, log_scale: bool = False) -> _T: ...
