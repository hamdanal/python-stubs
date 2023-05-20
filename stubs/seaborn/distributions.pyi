from _typeshed import Incomplete

from ._oldcore import VectorPlotter

__all__ = ["displot", "histplot", "kdeplot", "ecdfplot", "rugplot", "distplot"]

class _DistributionPlotter(VectorPlotter):
    semantics: Incomplete
    wide_structure: Incomplete
    flat_structure: Incomplete
    def __init__(self, data: Incomplete | None = ..., variables=...) -> None: ...
    @property
    def univariate(self): ...
    @property
    def data_variable(self): ...
    @property
    def has_xy_data(self): ...
    def plot_univariate_histogram(
        self,
        multiple,
        element,
        fill,
        common_norm,
        common_bins,
        shrink,
        kde,
        kde_kws,
        color,
        legend,
        line_kws,
        estimate_kws,
        **plot_kws,
    ) -> None: ...
    def plot_bivariate_histogram(
        self, common_bins, common_norm, thresh, pthresh, pmax, color, legend, cbar, cbar_ax, cbar_kws, estimate_kws, **plot_kws
    ) -> None: ...
    def plot_univariate_density(
        self, multiple, common_norm, common_grid, warn_singular, fill, color, legend, estimate_kws, **plot_kws
    ) -> None: ...
    def plot_bivariate_density(
        self,
        common_norm,
        fill,
        levels,
        thresh,
        color,
        legend,
        cbar,
        warn_singular,
        cbar_ax,
        cbar_kws,
        estimate_kws,
        **contour_kws,
    ) -> None: ...
    def plot_univariate_ecdf(self, estimate_kws, legend, **plot_kws) -> None: ...
    def plot_rug(self, height, expand_margins, legend, **kws) -> None: ...

class _DistributionFacetPlotter(_DistributionPlotter):
    semantics: Incomplete

def histplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    weights: Incomplete | None = ...,
    stat: str = ...,
    bins: str = ...,
    binwidth: Incomplete | None = ...,
    binrange: Incomplete | None = ...,
    discrete: Incomplete | None = ...,
    cumulative: bool = ...,
    common_bins: bool = ...,
    common_norm: bool = ...,
    multiple: str = ...,
    element: str = ...,
    fill: bool = ...,
    shrink: int = ...,
    kde: bool = ...,
    kde_kws: Incomplete | None = ...,
    line_kws: Incomplete | None = ...,
    thresh: int = ...,
    pthresh: Incomplete | None = ...,
    pmax: Incomplete | None = ...,
    cbar: bool = ...,
    cbar_ax: Incomplete | None = ...,
    cbar_kws: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    color: Incomplete | None = ...,
    log_scale: Incomplete | None = ...,
    legend: bool = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def kdeplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    weights: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    color: Incomplete | None = ...,
    fill: Incomplete | None = ...,
    multiple: str = ...,
    common_norm: bool = ...,
    common_grid: bool = ...,
    cumulative: bool = ...,
    bw_method: str = ...,
    bw_adjust: int = ...,
    warn_singular: bool = ...,
    log_scale: Incomplete | None = ...,
    levels: int = ...,
    thresh: float = ...,
    gridsize: int = ...,
    cut: int = ...,
    clip: Incomplete | None = ...,
    legend: bool = ...,
    cbar: bool = ...,
    cbar_ax: Incomplete | None = ...,
    cbar_kws: Incomplete | None = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def ecdfplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    weights: Incomplete | None = ...,
    stat: str = ...,
    complementary: bool = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    log_scale: Incomplete | None = ...,
    legend: bool = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def rugplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    height: float = ...,
    expand_margins: bool = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    legend: bool = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...
def displot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    row: Incomplete | None = ...,
    col: Incomplete | None = ...,
    weights: Incomplete | None = ...,
    kind: str = ...,
    rug: bool = ...,
    rug_kws: Incomplete | None = ...,
    log_scale: Incomplete | None = ...,
    legend: bool = ...,
    palette: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    hue_norm: Incomplete | None = ...,
    color: Incomplete | None = ...,
    col_wrap: Incomplete | None = ...,
    row_order: Incomplete | None = ...,
    col_order: Incomplete | None = ...,
    height: int = ...,
    aspect: int = ...,
    facet_kws: Incomplete | None = ...,
    **kwargs,
): ...
def distplot(
    a: Incomplete | None = ...,
    bins: Incomplete | None = ...,
    hist: bool = ...,
    kde: bool = ...,
    rug: bool = ...,
    fit: Incomplete | None = ...,
    hist_kws: Incomplete | None = ...,
    kde_kws: Incomplete | None = ...,
    rug_kws: Incomplete | None = ...,
    fit_kws: Incomplete | None = ...,
    color: Incomplete | None = ...,
    vertical: bool = ...,
    norm_hist: bool = ...,
    axlabel: Incomplete | None = ...,
    label: Incomplete | None = ...,
    ax: Incomplete | None = ...,
    x: Incomplete | None = ...,
): ...
