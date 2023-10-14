from _typeshed import Incomplete
from collections import UserDict

ZERO_INJECTION_STD_DEV: float
BR_SIDE: Incomplete
BR_MEAS_PPCI_IX: Incomplete
BUS_MEAS_PPCI_IX: Incomplete

def pp2eppci(
    net,
    v_start: Incomplete | None = None,
    delta_start: Incomplete | None = None,
    calculate_voltage_angles: bool = True,
    zero_injection: str = "aux_bus",
    ppc: Incomplete | None = None,
    eppci: Incomplete | None = None,
): ...

class ExtendedPPCI(UserDict):
    data: Incomplete
    z: Incomplete
    r_cov: Incomplete
    pp_meas_indices: Incomplete
    non_nan_meas_mask: Incomplete
    non_nan_meas_selector: Incomplete
    any_i_meas: bool
    any_degree_meas: bool
    non_slack_buses: Incomplete
    non_slack_bus_mask: Incomplete
    num_non_slack_bus: Incomplete
    delta_v_bus_mask: Incomplete
    delta_v_bus_selector: Incomplete
    v_init: Incomplete
    delta_init: Incomplete
    E_init: Incomplete
    v: Incomplete
    delta: Incomplete
    E: Incomplete
    def __init__(self, ppci) -> None: ...
    def update_meas(self) -> None: ...
    @property
    def V(self): ...
    def reset(self) -> None: ...
    def update_E(self, E) -> None: ...
    def E2V(self, E): ...
    def get_Y(self): ...
