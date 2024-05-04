from _typeshed import Incomplete
from typing import Literal

from plotly.graph_objs import Figure  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]

from pandapower.auxiliary import pandapowerNet
from pandapower.plotting.plotly.traces import _MapStyle

def vlevel_plotly(
    net: pandapowerNet,
    respect_switches: bool = True,
    use_line_geodata: bool | None = None,
    colors_dict: dict[float, Incomplete] | None = None,
    on_map: bool = False,
    projection: str | None = None,
    map_style: _MapStyle = "basic",
    figsize: float = 1,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    line_width: float = 2,
    bus_size: float = 10,
    filename: str = "temp-plot.html",
    auto_open: bool = True,
) -> Figure: ...
