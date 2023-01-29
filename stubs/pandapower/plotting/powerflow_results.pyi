from _typeshed import Incomplete

MATPLOTLIB_INSTALLED: bool

def plot_voltage_profile(
    net,
    ax: Incomplete | None = ...,
    plot_transformers: bool = ...,
    xlabel: str = ...,
    ylabel: str = ...,
    x0: int = ...,
    line_color: str = ...,
    trafo_color: str = ...,
    bus_colors: str = ...,
    line_loading_weight: bool = ...,
    voltage_column: Incomplete | None = ...,
    bus_size: int = ...,
    lines: Incomplete | None = ...,
    **kwargs,
): ...
def plot_loading(
    net,
    ax: Incomplete | None = ...,
    element_type: str = ...,
    box_color: str = ...,
    median_color: str = ...,
    whisker_color: str = ...,
    index_subset: Incomplete | None = ...,
    **kwargs,
): ...
def voltage_profile_to_bus_geodata(net, voltages: Incomplete | None = ...): ...
