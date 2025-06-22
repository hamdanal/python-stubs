from collections.abc import Collection, Mapping

import pandas as pd
from matplotlib.axes import Axes
from matplotlib.typing import ColorType

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet

def plot_voltage_profile(
    net: pandapowerNet,
    ax: Axes | None = None,
    plot_transformers: Bool = True,
    xlabel: str = "Distance from Slack [km]",
    ylabel: str = "Voltage [pu]",
    x0: Float = 0,
    line_color: ColorType = "grey",
    trafo_color: ColorType = "r",
    bus_colors: str | Mapping[int, ColorType] = "b",
    line_loading_weight: Bool = False,
    voltage_column: str | None = None,
    bus_size: Float = 3,
    lines: Collection[int] | None = None,
    **kwargs,
) -> Axes: ...
def plot_loading(
    net: pandapowerNet,
    ax: Axes | None = None,
    element_type: str = "line",
    box_color: ColorType = "b",
    median_color: ColorType = "r",
    whisker_color: ColorType = "k",
    index_subset: Collection[int] | None = None,
    **kwargs,
) -> Axes: ...
def voltage_profile_to_bus_geodata(
    net: pandapowerNet, voltages: pd.Series[float] | None = None, root_bus: Int | None = None
) -> pd.DataFrame: ...
