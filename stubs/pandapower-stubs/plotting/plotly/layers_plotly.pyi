from _typeshed import SupportsGetItem
from typing import Literal

import plotly.graph_objs as go  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]

from pandapower.auxiliary import pandapowerNet

def layers_plotly(
    net: pandapowerNet,
    bus_groups,
    respect_switches: bool = True,
    use_line_geo: bool | None = None,
    colors_dict: SupportsGetItem[float, str] | None = None,
    on_map: bool = False,
    map_style: str = "basic",
    figsize: float = 1,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    line_width: float = 2,
    bus_size: float = 10,
    auto_open: bool = True,
) -> go.Figure: ...
