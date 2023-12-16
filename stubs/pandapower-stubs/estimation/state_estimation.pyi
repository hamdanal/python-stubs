from _typeshed import Incomplete

ALGORITHM_MAPPING: Incomplete
ALLOWED_OPT_VAR: Incomplete

def estimate(
    net,
    algorithm: str = "wls",
    init: str = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 10,
    calculate_voltage_angles: bool = True,
    zero_injection: str = "aux_bus",
    fuse_buses_with_bb_switch: str = "all",
    **opt_vars,
): ...
def remove_bad_data(
    net,
    init: str = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 10,
    calculate_voltage_angles: bool = True,
    rn_max_threshold: float = 3.0,
): ...
def chi2_analysis(
    net,
    init: str = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 10,
    calculate_voltage_angles: bool = True,
    chi2_prob_false: float = 0.05,
): ...

class StateEstimation:
    net: Incomplete
    solver: Incomplete
    ppc: Incomplete
    eppci: Incomplete
    recycle: Incomplete
    delta: Incomplete
    bad_data_present: Incomplete
    def __init__(
        self,
        net,
        tolerance: float = 1e-06,
        maximum_iterations: int = 10,
        algorithm: str = "wls",
        logger: Incomplete | None = None,
        recycle: bool = False,
    ) -> None: ...
    def estimate(
        self,
        v_start: str = "flat",
        delta_start: str = "flat",
        calculate_voltage_angles: bool = True,
        zero_injection: Incomplete | None = None,
        fuse_buses_with_bb_switch: str = "all",
        **opt_vars,
    ): ...
    def perform_chi2_test(
        self,
        v_in_out: Incomplete | None = None,
        delta_in_out: Incomplete | None = None,
        calculate_voltage_angles: bool = True,
        chi2_prob_false: float = 0.05,
    ): ...
    def perform_rn_max_test(
        self,
        v_in_out: Incomplete | None = None,
        delta_in_out: Incomplete | None = None,
        calculate_voltage_angles: bool = True,
        rn_max_threshold: float = 3.0,
    ): ...
