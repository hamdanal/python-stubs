from _typeshed import Incomplete

from seaborn.axisgrid import FacetGrid
from seaborn.relational import _RelationalPlotter

__all__ = ["catplot", "stripplot", "swarmplot", "boxplot", "violinplot", "boxenplot", "pointplot", "barplot", "countplot"]

class _CategoricalPlotterNew(_RelationalPlotter):
    semantics: Incomplete
    wide_structure: Incomplete
    flat_structure: Incomplete
    plot_data: Incomplete
    orient: Incomplete
    legend: Incomplete
    def __init__(
        self,
        data: Incomplete | None = None,
        variables={},
        order: Incomplete | None = None,
        orient: Incomplete | None = None,
        require_numeric: bool = False,
        legend: str = "auto",
    ) -> None: ...
    @property
    def cat_axis(self): ...
    def plot_strips(self, jitter, dodge, color, edgecolor, plot_kws) -> None: ...
    def plot_swarms(self, dodge, color, edgecolor, warn_thresh, plot_kws) -> None: ...

class _CategoricalFacetPlotter(_CategoricalPlotterNew):
    semantics: Incomplete

class _CategoricalPlotter:
    width: float
    default_palette: str
    require_numeric: bool
    orient: Incomplete
    plot_data: Incomplete
    group_label: Incomplete
    value_label: Incomplete
    group_names: Incomplete
    plot_hues: Incomplete
    hue_title: Incomplete
    hue_names: Incomplete
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
    def hue_offsets(self): ...
    @property
    def nested_width(self): ...
    def annotate_axes(self, ax) -> None: ...
    def add_legend_data(self, ax, color, label) -> None: ...

class _BoxPlotter(_CategoricalPlotter):
    dodge: Incomplete
    width: Incomplete
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
    width: Incomplete
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
        inner,
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
    def fit_kde(self, x, bw): ...
    def kde_support(self, x, bw, cut, gridsize): ...
    def scale_area(self, density, max_density, scale_hue) -> None: ...
    def scale_width(self, density) -> None: ...
    def scale_count(self, density, counts, scale_hue) -> None: ...
    @property
    def dwidth(self): ...
    def draw_violins(self, ax) -> None: ...
    def draw_single_observation(self, ax, at_group, at_quant, density) -> None: ...
    def draw_box_lines(self, ax, data, center) -> None: ...
    def draw_quartiles(self, ax, data, support, density, center, split: bool = False) -> None: ...
    def draw_points(self, ax, data, center) -> None: ...
    def draw_stick_lines(self, ax, data, support, density, center, split: bool = False) -> None: ...
    def draw_to_density(self, ax, center, val, support, density, split, **kws) -> None: ...
    def plot(self, ax) -> None: ...

class _CategoricalStatPlotter(_CategoricalPlotter):
    require_numeric: bool
    @property
    def nested_width(self): ...
    statistic: Incomplete
    confint: Incomplete
    def estimate_statistic(self, estimator, errorbar, n_boot, seed) -> None: ...
    def draw_confints(
        self, ax, at_group, confint, colors, errwidth: Incomplete | None = None, capsize: Incomplete | None = None, **kws
    ) -> None: ...

class _BarPlotter(_CategoricalStatPlotter):
    dodge: Incomplete
    width: Incomplete
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
        errorbar,
        n_boot,
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
    def hue_offsets(self): ...
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
    fliersize: int = 5,
    linewidth: Incomplete | None = None,
    whis: float = 1.5,
    ax: Incomplete | None = None,
    **kwargs,
): ...
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
    ax: Incomplete | None = None,
    **kwargs,
): ...
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
    ax: Incomplete | None = None,
    box_kws: Incomplete | None = None,
    flier_kws: Incomplete | None = None,
    line_kws: Incomplete | None = None,
): ...
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
    size: int = 5,
    edgecolor: str = "gray",
    linewidth: int = 0,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    legend: str = "auto",
    ax: Incomplete | None = None,
    **kwargs,
): ...
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
    size: int = 5,
    edgecolor: str = "gray",
    linewidth: int = 0,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    legend: str = "auto",
    warn_thresh: float = 0.05,
    ax: Incomplete | None = None,
    **kwargs,
): ...
def barplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    estimator: str = "mean",
    errorbar=("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: Incomplete | None = None,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    errcolor: str = ".26",
    errwidth: Incomplete | None = None,
    capsize: Incomplete | None = None,
    dodge: bool = True,
    ci: str = "deprecated",
    ax: Incomplete | None = None,
    **kwargs,
): ...
def pointplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    estimator: str = "mean",
    errorbar=("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: Incomplete | None = None,
    markers: str = "o",
    linestyles: str = "-",
    dodge: bool = False,
    join: bool = True,
    scale: int = 1,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    errwidth: Incomplete | None = None,
    ci: str = "deprecated",
    capsize: Incomplete | None = None,
    label: Incomplete | None = None,
    ax: Incomplete | None = None,
): ...
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
    ax: Incomplete | None = None,
    **kwargs,
): ...
def catplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    col_wrap: Incomplete | None = None,
    estimator: str = "mean",
    errorbar=("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    row_order: Incomplete | None = None,
    col_order: Incomplete | None = None,
    height: int = 5,
    aspect: int = 1,
    kind: str = "strip",
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    orient: Incomplete | None = None,
    color: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    legend: str = "auto",
    legend_out: bool = True,
    sharex: bool = True,
    sharey: bool = True,
    margin_titles: bool = False,
    facet_kws: Incomplete | None = None,
    ci: str = "deprecated",
    **kwargs,
) -> FacetGrid: ...

class Beeswarm:
    orient: Incomplete
    width: Incomplete
    warn_thresh: Incomplete
    def __init__(self, orient: str = "v", width: float = 0.8, warn_thresh: float = 0.05) -> None: ...
    def __call__(self, points, center) -> None: ...
    def beeswarm(self, orig_xyr): ...
    def could_overlap(self, xyr_i, swarm): ...
    def position_candidates(self, xyr_i, neighbors): ...
    def first_non_overlapping_candidate(self, candidates, neighbors): ...
    def add_gutters(self, points, center, log_scale: bool = False): ...
