from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Literal
from typing_extensions import TypeAlias

import pandas as pd
from plotly.graph_objs import Figure  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]

from pandapower.auxiliary import pandapowerNet

_MapStyle: TypeAlias = Literal["basic", "streets", "bright", "light", "dark", "satellite"]

def version_check() -> None: ...
def sum_line_length(pts: Incomplete) -> float: ...
def get_line_neutral(coord: Incomplete) -> list[Incomplete]: ...
def create_edge_center_trace(
    line_trace,
    size: int = 1,
    patch_type: str = "circle",
    color: str = "white",
    infofunc: pd.Series[Incomplete] | None = None,
    trace_name: str = "edge_center",
    use_line_geodata: bool = False,
    showlegend: bool = False,
    legendgroup: str | None = None,
    hoverlabel: Incomplete | None = None,
) -> dict[str, Incomplete]: ...
def create_bus_trace(
    net: pandapowerNet,
    buses: Iterable[int] | pd.Index[int] | None = None,
    size: int = 5,
    patch_type: str = "circle",
    color: str = "blue",
    infofunc: pd.Series[Incomplete] | Iterable[Incomplete] | None = None,
    trace_name: str = "buses",
    legendgroup: str | None = None,
    cmap: str | None = None,
    cmap_vals: Incomplete | None = None,
    cbar_title: str | None = None,
    cmin: float | None = None,
    cmax: float | None = None,
    cpos: float = 1.0,
    colormap_column: str = "vm_pu",
) -> list[dict[str, Incomplete]]: ...
def create_line_trace(
    net: pandapowerNet,
    lines: Iterable[int] | pd.Index[int] | None = None,
    use_line_geodata: bool = True,
    respect_switches: bool = False,
    width: float = 1.0,
    color: str = "grey",
    infofunc: pd.Series[Incomplete] | Iterable[Incomplete] | None = None,
    trace_name: str = "lines",
    legendgroup: str | None = "lines",
    cmap: str | None = None,
    cbar_title: str | None = None,
    show_colorbar: bool = True,
    cmap_vals: Incomplete | None = None,
    cmin: float | None = None,
    cmax: float | None = None,
    cpos: float = 1.1,
    cmap_vals_category: str = "loading_percent",
    hoverlabel: Incomplete | None = None,
) -> list[dict[str, Incomplete]]: ...
def create_trafo_trace(
    net: pandapowerNet,
    trafos: Iterable[int] | None = None,
    color: str = "green",
    trafotype: str = "2W",
    width: int = 5,
    infofunc: pd.Series[Incomplete] | Iterable[Incomplete] | None = None,
    cmap: str | None = None,
    trace_name: str = "2W transformers",
    cmin: float | None = None,
    cmax: float | None = None,
    cmap_vals: Incomplete | None = None,
    matching_params: Incomplete | None = None,
    use_line_geodata: bool | None = None,
) -> list[dict[str, Incomplete]]: ...
def create_weighted_marker_trace(
    net: pandapowerNet,
    elm_type: str = "load",
    elm_ids: Iterable[Incomplete] | None = None,
    column_to_plot: str = "p_mw",
    sizemode: Literal["area", "diameter"] = "area",
    color: str = "red",
    patch_type: str = "circle",
    marker_scaling: float = 1.0,
    trace_name: str = "",
    infofunc: pd.Series[Incomplete] | Iterable[Incomplete] | None = None,
    node_element: str = "bus",
    show_scale_legend: bool = True,
    scale_marker_size: float | None = None,
) -> dict[str, Incomplete]: ...
def create_scale_trace(
    net: pandapowerNet, weighted_trace: dict[str, Incomplete], down_shift: int = 0
) -> dict[str, Incomplete]: ...
def draw_traces(
    traces: list[dict[str, Incomplete]],
    on_map: bool = False,
    map_style: _MapStyle = "basic",
    showlegend: bool = True,
    figsize: float = 1,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    filename: str = "temp-plot.html",
    auto_open: bool = True,
    **kwargs,
) -> Figure: ...
