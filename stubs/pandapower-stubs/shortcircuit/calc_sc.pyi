from collections.abc import Iterable
from typing import Literal

from pandapower.auxiliary import pandapowerNet

def calc_sc(
    net: pandapowerNet,
    bus: int | Iterable[int] | None = None,
    fault: Literal["1ph", "2ph", "3ph"] = "3ph",
    case: Literal["min", "max"] = "max",
    lv_tol_percent: int = 10,
    topology: Literal["meshed", "radial", "auto"] = "auto",
    ip: bool = False,
    ith: bool = False,
    tk_s: float = 1.0,
    kappa_method: str = "C",
    r_fault_ohm: float = 0.0,
    x_fault_ohm: float = 0.0,
    branch_results: bool = False,
    check_connectivity: bool = True,
    return_all_currents: bool = False,
    inverse_y: bool = True,
    use_pre_fault_voltage: bool = False,
) -> None: ...
