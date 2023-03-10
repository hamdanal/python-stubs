from _typeshed import Incomplete

from seaborn.relational import _RelationalPlotter

class _CategoricalPlotterNew(_RelationalPlotter):
    semantics: Incomplete
    wide_structure: Incomplete
    flat_structure: Incomplete
    plot_data: Incomplete
    orient: Incomplete
    legend: Incomplete
    def __init__(
        self,
        data: Incomplete | None = ...,
        variables=...,
        order: Incomplete | None = ...,
        orient: Incomplete | None = ...,
        require_numeric: bool = ...,
        legend: str = ...,
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
        x: Incomplete | None = ...,
        y: Incomplete | None = ...,
        hue: Incomplete | None = ...,
        data: Incomplete | None = ...,
        orient: Incomplete | None = ...,
        order: Incomplete | None = ...,
        hue_order: Incomplete | None = ...,
        units: Incomplete | None = ...,
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
    def draw_quartiles(self, ax, data, support, density, center, split: bool = ...) -> None: ...
    def draw_points(self, ax, data, center) -> None: ...
    def draw_stick_lines(self, ax, data, support, density, center, split: bool = ...) -> None: ...
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
        self, ax, at_group, confint, colors, errwidth: Incomplete | None = ..., capsize: Incomplete | None = ..., **kws
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
        showfliers: bool = ...,
    ) -> None: ...
    def draw_letter_value_plot(
        self, ax, box_kws: Incomplete | None = ..., flier_kws: Incomplete | None = ..., line_kws: Incomplete | None = ...
    ) -> None: ...
    def plot(self, ax, box_kws, flier_kws, line_kws) -> None: ...

def boxplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    saturation: float = ...,
    width: float = ...,
    dodge: bool = ...,
    fliersize: int = ...,
    linewidth: Incomplete | None = ...,
    whis: float = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def violinplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    bw: str = ...,
    cut: int = ...,
    scale: str = ...,
    scale_hue: bool = ...,
    gridsize: int = ...,
    width: float = ...,
    inner: str = ...,
    split: bool = ...,
    dodge: bool = ...,
    orient: Incomplete | None = ...,
    linewidth: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    saturation: float = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def boxenplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    saturation: float = ...,
    width: float = ...,
    dodge: bool = ...,
    k_depth: str = ...,
    linewidth: Incomplete | None = ...,
    scale: str = ...,
    outlier_prop: float = ...,
    trust_alpha: float = ...,
    showfliers: bool = ...,
    ax: Incomplete | None = ...,
    box_kws: Incomplete | None = ...,
    flier_kws: Incomplete | None = ...,
    line_kws: Incomplete | None = ...,
): ...
def stripplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    jitter: bool = ...,
    dodge: bool = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    size: int = ...,
    edgecolor: str = ...,
    linewidth: int = ...,
    hue_norm: Incomplete | None = ...,
    native_scale: bool = ...,
    formatter: Incomplete | None = ...,
    legend: str = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def swarmplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    dodge: bool = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    size: int = ...,
    edgecolor: str = ...,
    linewidth: int = ...,
    hue_norm: Incomplete | None = ...,
    native_scale: bool = ...,
    formatter: Incomplete | None = ...,
    legend: str = ...,
    warn_thresh: float = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def barplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    estimator: str = ...,
    errorbar=...,
    n_boot: int = ...,
    units: Incomplete | None = ...,
    seed: Incomplete | None = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    saturation: float = ...,
    width: float = ...,
    errcolor: str = ...,
    errwidth: Incomplete | None = ...,
    capsize: Incomplete | None = ...,
    dodge: bool = ...,
    ci: str = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def pointplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    estimator: str = ...,
    errorbar=...,
    n_boot: int = ...,
    units: Incomplete | None = ...,
    seed: Incomplete | None = ...,
    markers: str = ...,
    linestyles: str = ...,
    dodge: bool = ...,
    join: bool = ...,
    scale: int = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    errwidth: Incomplete | None = ...,
    ci: str = ...,
    capsize: Incomplete | None = ...,
    label: Incomplete | None = ...,
    ax: Incomplete | None = ...,
): ...
def countplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    saturation: float = ...,
    width: float = ...,
    dodge: bool = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def catplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    row: Incomplete | None = ...,
    col: Incomplete | None = ...,
    col_wrap: Incomplete | None = ...,
    estimator: str = ...,
    errorbar=...,
    n_boot: int = ...,
    units: Incomplete | None = ...,
    seed: Incomplete | None = ...,
    order: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    row_order: Incomplete | None = ...,
    col_order: Incomplete | None = ...,
    height: int = ...,
    aspect: int = ...,
    kind: str = ...,
    native_scale: bool = ...,
    formatter: Incomplete | None = ...,
    orient: Incomplete | None = ...,
    color: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    legend: str = ...,
    legend_out: bool = ...,
    sharex: bool = ...,
    sharey: bool = ...,
    margin_titles: bool = ...,
    facet_kws: Incomplete | None = ...,
    ci: str = ...,
    **kwargs,
): ...

class Beeswarm:
    orient: Incomplete
    width: Incomplete
    warn_thresh: Incomplete
    def __init__(self, orient: str = ..., width: float = ..., warn_thresh: float = ...) -> None: ...
    def __call__(self, points, center) -> None: ...
    def beeswarm(self, orig_xyr): ...
    def could_overlap(self, xyr_i, swarm): ...
    def position_candidates(self, xyr_i, neighbors): ...
    def first_non_overlapping_candidate(self, candidates, neighbors): ...
    def add_gutters(self, points, center, log_scale: bool = ...): ...
