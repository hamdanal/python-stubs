from _typeshed import Incomplete

from .axisgrid import Grid

class _HeatMapper:
    xticks: Incomplete
    xticklabels: Incomplete
    yticks: Incomplete
    yticklabels: Incomplete
    xlabel: Incomplete
    ylabel: Incomplete
    data: Incomplete
    plot_data: Incomplete
    annot: Incomplete
    annot_data: Incomplete
    fmt: Incomplete
    annot_kws: Incomplete
    cbar: Incomplete
    cbar_kws: Incomplete
    def __init__(
        self,
        data,
        vmin,
        vmax,
        cmap,
        center,
        robust,
        annot,
        fmt,
        annot_kws,
        cbar,
        cbar_kws,
        xticklabels: bool = ...,
        yticklabels: bool = ...,
        mask: Incomplete | None = ...,
    ) -> None: ...
    def plot(self, ax, cax, kws) -> None: ...

def heatmap(
    data,
    *,
    vmin: Incomplete | None = ...,
    vmax: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    center: Incomplete | None = ...,
    robust: bool = ...,
    annot: Incomplete | None = ...,
    fmt: str = ...,
    annot_kws: Incomplete | None = ...,
    linewidths: int = ...,
    linecolor: str = ...,
    cbar: bool = ...,
    cbar_kws: Incomplete | None = ...,
    cbar_ax: Incomplete | None = ...,
    square: bool = ...,
    xticklabels: str = ...,
    yticklabels: str = ...,
    mask: Incomplete | None = ...,
    ax: Incomplete | None = ...,
    **kwargs,
): ...

class _DendrogramPlotter:
    axis: Incomplete
    array: Incomplete
    data: Incomplete
    shape: Incomplete
    metric: Incomplete
    method: Incomplete
    label: Incomplete
    rotate: Incomplete
    linkage: Incomplete
    dendrogram: Incomplete
    xticks: Incomplete
    yticks: Incomplete
    xticklabels: Incomplete
    yticklabels: Incomplete
    ylabel: Incomplete
    xlabel: str
    dependent_coord: Incomplete
    independent_coord: Incomplete
    def __init__(self, data, linkage, metric, method, axis, label, rotate) -> None: ...
    @property
    def calculated_linkage(self): ...
    def calculate_dendrogram(self): ...
    @property
    def reordered_ind(self): ...
    def plot(self, ax, tree_kws): ...

class ClusterGrid(Grid):
    data: Incomplete
    data2d: Incomplete
    mask: Incomplete
    gs: Incomplete
    ax_row_dendrogram: Incomplete
    ax_col_dendrogram: Incomplete
    ax_row_colors: Incomplete
    ax_col_colors: Incomplete
    ax_heatmap: Incomplete
    ax_cbar: Incomplete
    cax: Incomplete
    cbar_pos: Incomplete
    dendrogram_row: Incomplete
    dendrogram_col: Incomplete
    def __init__(
        self,
        data,
        pivot_kws: Incomplete | None = ...,
        z_score: Incomplete | None = ...,
        standard_scale: Incomplete | None = ...,
        figsize: Incomplete | None = ...,
        row_colors: Incomplete | None = ...,
        col_colors: Incomplete | None = ...,
        mask: Incomplete | None = ...,
        dendrogram_ratio: Incomplete | None = ...,
        colors_ratio: Incomplete | None = ...,
        cbar_pos: Incomplete | None = ...,
    ) -> None: ...
    def format_data(self, data, pivot_kws, z_score: Incomplete | None = ..., standard_scale: Incomplete | None = ...): ...
    @staticmethod
    def z_score(data2d, axis: int = ...): ...
    @staticmethod
    def standard_scale(data2d, axis: int = ...): ...
    def dim_ratios(self, colors, dendrogram_ratio, colors_ratio): ...
    @staticmethod
    def color_list_to_matrix_and_cmap(colors, ind, axis: int = ...): ...
    def plot_dendrograms(self, row_cluster, col_cluster, metric, method, row_linkage, col_linkage, tree_kws) -> None: ...
    def plot_colors(self, xind, yind, **kws) -> None: ...
    def plot_matrix(self, colorbar_kws, xind, yind, **kws) -> None: ...
    def plot(self, metric, method, colorbar_kws, row_cluster, col_cluster, row_linkage, col_linkage, tree_kws, **kws): ...

def clustermap(
    data,
    *,
    pivot_kws: Incomplete | None = ...,
    method: str = ...,
    metric: str = ...,
    z_score: Incomplete | None = ...,
    standard_scale: Incomplete | None = ...,
    figsize=...,
    cbar_kws: Incomplete | None = ...,
    row_cluster: bool = ...,
    col_cluster: bool = ...,
    row_linkage: Incomplete | None = ...,
    col_linkage: Incomplete | None = ...,
    row_colors: Incomplete | None = ...,
    col_colors: Incomplete | None = ...,
    mask: Incomplete | None = ...,
    dendrogram_ratio: float = ...,
    colors_ratio: float = ...,
    cbar_pos=...,
    tree_kws: Incomplete | None = ...,
    **kwargs,
): ...
