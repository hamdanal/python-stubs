from typing import Literal

from plotly.graph_objs import Figure  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]

from pandapower.auxiliary import pandapowerNet
from pandapower.plotting.plotly.mapbox_plot import *
from pandapower.plotting.plotly.traces import _MapStyle

def pf_res_plotly(
    net: pandapowerNet,
    cmap: str = "Jet",
    use_line_geodata: bool | None = None,
    on_map: bool = False,
    projection: str | None = None,
    map_style: _MapStyle = "basic",
    figsize: float = 1,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    line_width: float = 2,
    bus_size: float = 10,
    climits_volt: tuple[float, float] = (0.9, 1.1),
    climits_load: tuple[float, float] = (0, 100),
    cpos_volt: float = 1.0,
    cpos_load: float = 1.1,
    filename: str = "temp-plot.html",
    auto_open: bool = True,
) -> Figure: ...
