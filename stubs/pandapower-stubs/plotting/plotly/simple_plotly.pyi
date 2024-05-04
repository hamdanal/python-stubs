from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Literal, overload

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
def simple_plotly(
    net: pandapowerNet,
    respect_switches: bool = True,
    use_line_geodata: bool | None = None,
    on_map: bool = False,
    projection: str | None = None,
    map_style: _MapStyle = "basic",
    figsize: float = 1,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    line_width: float = 1,
    bus_size: float = 10,
    ext_grid_size: float = 20.0,
    bus_color: str = "blue",
    line_color: str = "grey",
    trafo_color: str = "green",
    trafo3w_color: str = "green",
    ext_grid_color: str = "yellow",
    filename: str = "temp-plot.html",
    auto_open: bool = True,
    showlegend: bool = True,
    additional_traces: Incomplete | None = None,
) -> Figure: ...
