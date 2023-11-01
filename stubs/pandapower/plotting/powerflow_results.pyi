from _typeshed import Incomplete
from collections.abc import Sequence

import pandas as pd
from matplotlib.axes import Axes

from pandapower.auxiliary import pandapowerNet

MATPLOTLIB_INSTALLED: bool

def plot_voltage_profile(
    net: pandapowerNet,
    ax: Axes | None = None,
    plot_transformers: bool = True,
    xlabel: str = "Distance from Slack [km]",
    ylabel: str = "Voltage [pu]",
    x0: int = 0,
    line_color: str = "grey",
    trafo_color: str = "r",
    bus_colors: str = "b",
    line_loading_weight: bool = False,
    bus_size: int = 3,
    lines: Sequence[int] | pd.Index | None = None,
    **kwargs: Incomplete,
) -> Axes: ...
def plot_loading(
    net: pandapowerNet,
    ax: Axes | None = None,
    element_type: str = "line",
    box_color: str = "b",
    median_color: str = "r",
    whisker_color: str = "k",
    index_subset: Sequence[int] | pd.Index | None = None,
    **kwargs: Incomplete,
) -> Axes: ...
def voltage_profile_to_bus_geodata(net: pandapowerNet, voltages: pd.Series[float] | None = None) -> pd.DataFrame: ...
