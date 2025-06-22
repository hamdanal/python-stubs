from typing import Literal

from matplotlib.axes import Axes
from matplotlib.typing import ColorType

from pandapower._typing import Bool, Float
from pandapower.auxiliary import pandapowerNet

def simple_plot(
    net: pandapowerNet,
    respect_switches: Bool = False,
    line_width: Float = 1.0,
    bus_size: Float = 1.0,
    ext_grid_size: Float = 1.0,
    trafo_size: Float = 1.0,
    plot_loads: Bool = False,
    plot_gens: Bool = False,
    plot_sgens: Bool = False,
    load_size: Float = 1.0,
    gen_size: Float = 1.0,
    sgen_size: Float = 1.0,
    switch_size: Float = 2.0,
    switch_distance: Float = 1.0,
    plot_line_switches: Bool = False,
    scale_size: Bool = True,
    bus_color: ColorType = "b",
    line_color: ColorType = "grey",
    dcline_color: ColorType = "c",
    trafo_color: ColorType = "k",
    ext_grid_color: ColorType = "y",
    switch_color: ColorType = "k",
    library: Literal["igraph", "networkx"] = "igraph",
    show_plot: Bool = True,
    ax: Axes | None = None,
    bus_dc_size: Float = 1.0,
    bus_dc_color: ColorType = "m",
    line_dc_color: ColorType = "c",
    vsc_size: Float = 4.0,
    vsc_color: ColorType = "orange",
) -> Axes: ...
