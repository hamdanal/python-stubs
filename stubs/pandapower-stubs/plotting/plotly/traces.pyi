from _typeshed import Incomplete
from collections.abc import Collection, Iterable, Mapping
from typing import Any, Literal
from typing_extensions import TypeAlias

import pandas as pd
from plotly.graph_objs import Figure  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]

from pandapower._typing import Float, Int
from pandapower.auxiliary import pandapowerNet

_MapStyle: TypeAlias = Literal["basic", "streets", "bright", "light", "dark", "satellite"]

def sum_line_length(pts: Incomplete) -> float: ...
def get_line_neutral(coord: Incomplete) -> list[Incomplete]: ...
def create_edge_center_trace(
    line_trace,
    size: Int = 1,
    patch_type: str = "circle",
    color: str = "white",
    infofunc: pd.Series[Incomplete] | None = None,
    trace_name: str = "edge_center",
    use_line_geo: bool = False,
    showlegend: bool = False,
    legendgroup: str | None = None,
    hoverlabel: str | None = None,
) -> dict[str, Incomplete]: ...
def create_bus_trace(
    net: pandapowerNet,
    buses: Iterable[Int] | None = None,
    size: Int = 5,
    patch_type: str = "circle",
    color: str = "blue",
    infofunc: pd.Series[Incomplete] | Collection[Incomplete] | None = None,
    trace_name: str = "buses",
    legendgroup: str | None = None,
    cmap: str | None = None,
    cmap_vals: Collection[Float] | None = None,
    cbar_title: str | None = None,
    cmin: Float | None = None,
    cmax: Float | None = None,
    cpos: Float = 1.0,
    colormap_column: str = "vm_pu",
) -> list[dict[str, Incomplete]]: ...
def create_line_trace(
    net: pandapowerNet,
    lines: Iterable[Int] | None = None,
    use_line_geo: bool = True,
    respect_switches: bool = False,
    width: Float = 1.0,
    color: str = "grey",
    infofunc: pd.Series[Incomplete] | Collection[Incomplete] | None = None,
    trace_name: str = "lines",
    legendgroup: str | None = "lines",
    cmap: str | None = None,
    cbar_title: str | None = None,
    show_colorbar: bool = True,
    cmap_vals: Collection[Float] | None = None,
    cmin: Float | None = None,
    cmax: Float | None = None,
    cpos: Float = 1.1,
    cmap_vals_category: str = "loading_percent",
    hoverlabel: str | None = None,
    dash: str = "solid",
) -> list[dict[str, Incomplete]]: ...
def create_dcline_trace(
    net: pandapowerNet,
    dclines: Iterable[Int] | None = None,
    width: Float = 1.0,
    color: str = "grey",
    infofunc: pd.Series[Incomplete] | Collection[Incomplete] | None = None,
    trace_name: str = "hvdc lines",
    legendgroup: str | None = "dclines",
    cmap: str | None = None,
    cbar_title: str | None = None,
    show_colorbar: bool = True,
    cmap_vals: Collection[Float] | None = None,
    cmin: Float | None = None,
    cmax: Float | None = None,
    cpos: Float = 1.1,
    cmap_vals_category: str = "loading_percent",
    hoverlabel: str | None = None,
): ...
def create_trafo_trace(
    net: pandapowerNet,
    trafos: Iterable[Int] | None = None,
    color: str = "green",
    trafotype: str = "2W",
    width: Int = 5,
    infofunc: pd.Series[Incomplete] | Collection[Incomplete] | None = None,
    cmap: str | None = None,
    trace_name: str = "2W transformers",
    cmin: Float | None = None,
    cmax: Float | None = None,
    cmap_vals: Collection[Float] | None = None,
    matching_params: Incomplete | None = None,
    use_line_geo: bool | None = None,
) -> list[dict[str, Incomplete]]: ...
def create_weighted_marker_trace(
    net: pandapowerNet,
    elm_type: str = "load",
    elm_ids: Iterable[Int] | None = None,
    column_to_plot: str = "p_mw",
    sizemode: Literal["area", "diameter"] = "area",
    color: str = "red",
    patch_type: str = "circle",
    marker_scaling: Float = 1.0,
    trace_name: str = "",
    infofunc: pd.Series[Incomplete] | Collection[Incomplete] | None = None,
    node_element: str = "bus",
    show_scale_legend: bool = True,
    scale_marker_size: Float | None = None,
    scale_marker_color: str | None = None,
    scale_legend_unit: str | None = None,
    trace_kwargs: Mapping[str, Any] | None = None,
) -> dict[str, Incomplete]: ...
def create_scale_trace(
    net: pandapowerNet, weighted_trace: Mapping[str, Mapping[str, Any]], down_shift: Int = 0
) -> dict[str, Incomplete]: ...
def draw_traces(
    traces: Collection[dict[str, Incomplete]],
    on_map: bool = False,
    map_style: _MapStyle = "basic",
    showlegend: bool = True,
    figsize: Float = 1,
    aspectratio: tuple[Float, Float] | Literal["auto"] = "auto",
    filename: str = "temp-plot.html",
    auto_open: bool = True,
    **kwargs,
) -> Figure: ...
