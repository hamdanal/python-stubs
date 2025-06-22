from typing import Literal, SupportsIndex

import numpy as np

from pandapower._typing import Array2D
from pandapower.auxiliary import pandapowerNet

__all__ = ["detect_power_station_unit", "calc_sc_on_line"]

def detect_power_station_unit(
    net: pandapowerNet, mode: Literal["auto", "trafo"] = "auto", max_gen_voltage_kv: float = 80, max_distance_km: float = 0.01
) -> None: ...
def calc_sc_on_line(
    net: pandapowerNet, line_ix: SupportsIndex, distance_to_bus0: float, **kwargs
) -> tuple[pandapowerNet, np.int64]: ...
def adjust_V0_for_trafo_tap(ppci, V0, bus_idx) -> None: ...
def adjacency(ppci) -> Array2D[np.float64]: ...
