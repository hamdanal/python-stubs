from _typeshed import Incomplete

from pandapower.estimation.ppc_conversion import ExtendedPPCI

class BaseAlgebra:
    eppci: Incomplete
    fb: Incomplete
    tb: Incomplete
    n_bus: Incomplete
    n_branch: Incomplete
    num_non_slack_bus: Incomplete
    non_slack_buses: Incomplete
    delta_v_bus_mask: Incomplete
    non_nan_meas_mask: Incomplete
    any_i_meas: Incomplete
    any_degree_meas: Incomplete
    delta_v_bus_selector: Incomplete
    non_nan_meas_selector: Incomplete
    z: Incomplete
    sigma: Incomplete
    Ybus: Incomplete
    Yf: Incomplete
    Yt: Incomplete
    def __init__(self, eppci: ExtendedPPCI) -> None: ...
    def initialize_Y(self) -> None: ...
    def create_rx(self, E): ...
    def create_hx(self, E): ...
    def create_hx_jacobian(self, E): ...

class BaseAlgebraZeroInjConstraints(BaseAlgebra):
    def create_cx(self, E, p_zero_inj, q_zero_inj): ...
    def create_cx_jacobian(self, E, p_zero_inj, q_zero_inj): ...
