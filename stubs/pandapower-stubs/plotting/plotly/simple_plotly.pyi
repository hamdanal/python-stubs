from collections.abc import Iterable, Mapping
from typing import Any, Literal, overload

import pandas as pd
from plotly.graph_objs import Figure  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]

from pandapower.auxiliary import pandapowerNet
from pandapower.plotting.plotly.mapbox_plot import *
from pandapower.plotting.plotly.traces import _MapStyle

@overload
def get_hoverinfo(
    net: pandapowerNet,
    element: Literal["bus", "line", "trafo", "trafo3w", "ext_grid"],
    precision: int = 3,
    sub_index: Iterable[int] | None = None,
) -> pd.Series[str]: ...
@overload
def get_hoverinfo(
    net: pandapowerNet, element: str, precision: int = 3, sub_index: Iterable[int] | None = None
) -> pd.Series[str] | None: ...
@overload  # auto_draw_traces=True
def simple_plotly(
    net: pandapowerNet,
    respect_switches: bool = True,
    use_line_geo: bool | None = None,
    on_map: bool = False,
    map_style: _MapStyle = "basic",
    figsize: float = 1.0,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    line_width: float = 1.0,
    bus_size: float = 10.0,
    ext_grid_size: float = 20.0,
    bus_color: str = "blue",
    line_color: str = "grey",
    trafo_color: str = "green",
    trafo3w_color: str = "green",
    ext_grid_color: str = "yellow",
    filename: str = "temp-plot.html",
    auto_open: bool = True,
    showlegend: bool = True,
    additional_traces: dict[str, Mapping[str, Any]] | Iterable[Mapping[str, Mapping[str, Any]]] | None = None,
    zoomlevel: int = 11,
    auto_draw_traces: Literal[True] = True,
    hvdc_color: str = "cyan",
) -> Figure: ...
@overload  # auto_draw_traces=False positional
def simple_plotly(
    net: pandapowerNet,
    respect_switches: bool,
    use_line_geo: bool | None,
    on_map: bool,
    map_style: _MapStyle,
    figsize: float,
    aspectratio: tuple[float, float] | Literal["auto"],
    line_width: float,
    bus_size: float,
    ext_grid_size: float,
    bus_color: str,
    line_color: str,
    trafo_color: str,
    trafo3w_color: str,
    ext_grid_color: str,
    filename: str,
    auto_open: bool,
    showlegend: bool,
    additional_traces: dict[str, Mapping[str, Any]] | Iterable[Mapping[str, Mapping[str, Any]]] | None,
    zoomlevel: int,
    auto_draw_traces: Literal[False],
    hvdc_color: str = "cyan",
) -> tuple[list[dict[str, Any]], dict[str, Any]]: ...
@overload  # auto_draw_traces=False keyword
def simple_plotly(
    net: pandapowerNet,
    respect_switches: bool = True,
    use_line_geo: bool | None = None,
    on_map: bool = False,
    map_style: _MapStyle = "basic",
    figsize: float = 1.0,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    line_width: float = 1.0,
    bus_size: float = 10.0,
    ext_grid_size: float = 20.0,
    bus_color: str = "blue",
    line_color: str = "grey",
    trafo_color: str = "green",
    trafo3w_color: str = "green",
    ext_grid_color: str = "yellow",
    filename: str = "temp-plot.html",
    auto_open: bool = True,
    showlegend: bool = True,
    additional_traces: dict[str, Mapping[str, Any]] | Iterable[Mapping[str, Mapping[str, Any]]] | None = None,
    zoomlevel: int = 11,
    *,
    auto_draw_traces: Literal[False],
    hvdc_color: str = "cyan",
) -> tuple[list[dict[str, Any]], dict[str, Any]]: ...
