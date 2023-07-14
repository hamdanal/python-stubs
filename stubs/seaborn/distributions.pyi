from _typeshed import Incomplete

from matplotlib.axes import Axes

from ._oldcore import VectorPlotter
from .axisgrid import FacetGrid

__all__ = ["displot", "histplot", "kdeplot", "ecdfplot", "rugplot", "distplot"]

class _DistributionPlotter(VectorPlotter):
    def __init__(self, data: Incomplete | None = None, variables: dict[str, Incomplete] = {}) -> None: ...
    @property
    def univariate(self) -> bool: ...
    @property
    def data_variable(self) -> str: ...
    @property
    def has_xy_data(self) -> bool: ...
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

class _DistributionFacetPlotter(_DistributionPlotter): ...

def histplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    weights: Incomplete | None = None,
    stat: str = "count",
    bins: str = "auto",
    binwidth: Incomplete | None = None,
    binrange: Incomplete | None = None,
    discrete: Incomplete | None = None,
    cumulative: bool = False,
    common_bins: bool = True,
    common_norm: bool = True,
    multiple: str = "layer",
    element: str = "bars",
    fill: bool = True,
    shrink: float = 1,
    kde: bool = False,
    kde_kws: Incomplete | None = None,
    line_kws: Incomplete | None = None,
    thresh: float = 0,
    pthresh: Incomplete | None = None,
    pmax: Incomplete | None = None,
    cbar: bool = False,
    cbar_ax: Incomplete | None = None,
    cbar_kws: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    color: Incomplete | None = None,
    log_scale: Incomplete | None = None,
    legend: bool = True,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def kdeplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    weights: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    color: Incomplete | None = None,
    fill: Incomplete | None = None,
    multiple: str = "layer",
    common_norm: bool = True,
    common_grid: bool = False,
    cumulative: bool = False,
    bw_method: str = "scott",
    bw_adjust: int = 1,
    warn_singular: bool = True,
    log_scale: Incomplete | None = None,
    levels: int = 10,
    thresh: float = 0.05,
    gridsize: int = 200,
    cut: int = 3,
    clip: Incomplete | None = None,
    legend: bool = True,
    cbar: bool = False,
    cbar_ax: Incomplete | None = None,
    cbar_kws: Incomplete | None = None,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def ecdfplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    weights: Incomplete | None = None,
    stat: str = "proportion",
    complementary: bool = False,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    log_scale: Incomplete | None = None,
    legend: bool = True,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def rugplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    height: float = 0.025,
    expand_margins: bool = True,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    legend: bool = True,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def displot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    weights: Incomplete | None = None,
    kind: str = "hist",
    rug: bool = False,
    rug_kws: Incomplete | None = None,
    log_scale: Incomplete | None = None,
    legend: bool = True,
    palette: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    hue_norm: Incomplete | None = None,
    color: Incomplete | None = None,
    col_wrap: Incomplete | None = None,
    row_order: Incomplete | None = None,
    col_order: Incomplete | None = None,
    height: float = 5,
    aspect: float = 1,
    facet_kws: Incomplete | None = None,
    **kwargs,
) -> FacetGrid: ...
def distplot(
    a: Incomplete | None = None,
    bins: Incomplete | None = None,
    hist: bool = True,
    kde: bool = True,
    rug: bool = False,
    fit: Incomplete | None = None,
    hist_kws: Incomplete | None = None,
    kde_kws: Incomplete | None = None,
    rug_kws: Incomplete | None = None,
    fit_kws: Incomplete | None = None,
    color: Incomplete | None = None,
    vertical: bool = False,
    norm_hist: bool = False,
    axlabel: Incomplete | None = None,
    label: Incomplete | None = None,
    ax: Axes | None = None,
    x: Incomplete | None = None,
) -> Axes: ...
