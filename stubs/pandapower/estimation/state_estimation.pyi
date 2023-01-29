from _typeshed import Incomplete

ALGORITHM_MAPPING: Incomplete
ALLOWED_OPT_VAR: Incomplete

def estimate(
    net,
    algorithm: str = ...,
    init: str = ...,
    tolerance: float = ...,
    maximum_iterations: int = ...,
    calculate_voltage_angles: bool = ...,
    zero_injection: str = ...,
    fuse_buses_with_bb_switch: str = ...,
    **opt_vars,
): ...
def remove_bad_data(
    net,
    init: str = ...,
    tolerance: float = ...,
    maximum_iterations: int = ...,
    calculate_voltage_angles: bool = ...,
    rn_max_threshold: float = ...,
): ...
def chi2_analysis(
    net,
    init: str = ...,
    tolerance: float = ...,
    maximum_iterations: int = ...,
    calculate_voltage_angles: bool = ...,
    chi2_prob_false: float = ...,
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
        tolerance: float = ...,
        maximum_iterations: int = ...,
        algorithm: str = ...,
        logger: Incomplete | None = ...,
        recycle: bool = ...,
    ) -> None: ...
    def estimate(
        self,
        v_start: str = ...,
        delta_start: str = ...,
        calculate_voltage_angles: bool = ...,
        zero_injection: Incomplete | None = ...,
        fuse_buses_with_bb_switch: str = ...,
        **opt_vars,
    ): ...
    def perform_chi2_test(
        self,
        v_in_out: Incomplete | None = ...,
        delta_in_out: Incomplete | None = ...,
        calculate_voltage_angles: bool = ...,
        chi2_prob_false: float = ...,
    ): ...
    def perform_rn_max_test(
        self,
        v_in_out: Incomplete | None = ...,
        delta_in_out: Incomplete | None = ...,
        calculate_voltage_angles: bool = ...,
        rn_max_threshold: float = ...,
    ): ...
