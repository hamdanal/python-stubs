from typing import Literal

from pandapower._typing import Float, Int
from pandapower.auxiliary import pandapowerNet

def runpp_3ph(
    net: pandapowerNet,
    calculate_voltage_angles: bool = True,
    init: Literal["auto", "flat", "dc", "results"] = "auto",
    max_iteration: Int | Literal["auto"] = "auto",
    tolerance_mva: Float = 1e-08,
    trafo_model: Literal["t", "pi"] = "t",  # "pi" is not supported in 3ph
    trafo_loading: Literal["current", "power"] = "current",
    enforce_q_lims: bool = False,
    numba: bool = True,
    recycle: dict[str, bool] | None = None,
    check_connectivity: bool = True,
    switch_rx_ratio: Float = 2.0,
    delta_q: Float = 0,
    v_debug: bool = False,
    **kwargs,
) -> None: ...
