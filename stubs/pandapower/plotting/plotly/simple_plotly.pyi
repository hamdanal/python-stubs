from _typeshed import Incomplete

from pandapower.plotting.plotly.mapbox_plot import *

def get_hoverinfo(net, element, precision: int = ..., sub_index: Incomplete | None = ...): ...
def simple_plotly(
    net,
    respect_switches: bool = ...,
    use_line_geodata: Incomplete | None = ...,
    on_map: bool = ...,
    projection: Incomplete | None = ...,
    map_style: str = ...,
    figsize: int = ...,
    aspectratio: str = ...,
    line_width: int = ...,
    bus_size: int = ...,
    ext_grid_size: float = ...,
    bus_color: str = ...,
    line_color: str = ...,
    trafo_color: str = ...,
    trafo3w_color: str = ...,
    ext_grid_color: str = ...,
    filename: str = ...,
    auto_open: bool = ...,
    showlegend: bool = ...,
    additional_traces: Incomplete | None = ...,
): ...
