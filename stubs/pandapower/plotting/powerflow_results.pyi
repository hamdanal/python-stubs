from _typeshed import Incomplete
from collections.abc import Mapping, Sequence

import pandas as pd
from matplotlib.axes import Axes
from matplotlib.typing import ColorType

from pandapower.auxiliary import pandapowerNet

MATPLOTLIB_INSTALLED: bool

def plot_voltage_profile(
    net: pandapowerNet,
    ax: Axes | None = None,
    plot_transformers: bool = True,
    xlabel: str = "Distance from Slack [km]",
    ylabel: str = "Voltage [pu]",
    x0: float = 0,
    line_color: ColorType = "grey",
    trafo_color: ColorType = "r",
    bus_colors: str | Mapping[int, ColorType] = "b",
    line_loading_weight: bool = False,
    bus_size: float = 3,
    lines: Sequence[int] | pd.Index[int] | None = None,
    **kwargs: Incomplete,
) -> Axes: ...
def plot_loading(
    net: pandapowerNet,
    ax: Axes | None = None,
    element_type: str = "line",
    box_color: ColorType = "b",
    median_color: ColorType = "r",
    whisker_color: ColorType = "k",
    index_subset: Sequence[int] | pd.Index[int] | None = None,
    **kwargs: Incomplete,
) -> Axes: ...
def voltage_profile_to_bus_geodata(net: pandapowerNet, voltages: pd.Series[float] | None = None) -> pd.DataFrame: ...
