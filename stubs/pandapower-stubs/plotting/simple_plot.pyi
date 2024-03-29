from typing import Literal

from matplotlib.axes import Axes
from matplotlib.typing import ColorType

from pandapower.auxiliary import pandapowerNet

MATPLOTLIB_INSTALLED: bool

def simple_plot(
    net: pandapowerNet,
    respect_switches: bool = False,
    line_width: float = 1.0,
    bus_size: float = 1.0,
    ext_grid_size: float = 1.0,
    trafo_size: float = 1.0,
    plot_loads: bool = False,
    plot_gens: bool = False,
    plot_sgens: bool = False,
    load_size: float = 1.0,
    gen_size: float = 1.0,
    sgen_size: float = 1.0,
    switch_size: float = 2.0,
    switch_distance: float = 1.0,
    plot_line_switches: bool = False,
    scale_size: bool = True,
    bus_color: ColorType = "b",
    line_color: ColorType = "grey",
    dcline_color: ColorType = "c",
    trafo_color: ColorType = "k",
    ext_grid_color: ColorType = "y",
    switch_color: ColorType = "k",
    library: Literal["igraph", "networkx"] = "igraph",
    show_plot: bool = True,
    ax: Axes | None = None,
) -> Axes: ...
