from typing import Literal, SupportsIndex

import numpy as np
from numpy.typing import NDArray

from pandapower.auxiliary import pandapowerNet

def detect_power_station_unit(
    net: pandapowerNet, mode: Literal["auto", "trafo"] = "auto", max_gen_voltage_kv: float = 80, max_distance_km: float = 0.01
) -> None: ...
def calc_sc_on_line(
    net: pandapowerNet, line_ix: SupportsIndex, distance_to_bus0: float, **kwargs
) -> tuple[pandapowerNet, int]: ...
def adjust_V0_for_trafo_tap(ppci, V0, bus_idx) -> None: ...
def adjacency(ppci) -> NDArray[np.float64]: ...
