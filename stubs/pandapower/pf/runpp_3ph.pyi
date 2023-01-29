from _typeshed import Incomplete

from pandapower.auxiliary import ppException

class Not_implemented(ppException): ...

def runpp_3ph(
    net,
    calculate_voltage_angles: bool = ...,
    init: str = ...,
    max_iteration: str = ...,
    tolerance_mva: float = ...,
    trafo_model: str = ...,
    trafo_loading: str = ...,
    enforce_q_lims: bool = ...,
    numba: bool = ...,
    recycle: Incomplete | None = ...,
    check_connectivity: bool = ...,
    switch_rx_ratio: float = ...,
    delta_q: int = ...,
    v_debug: bool = ...,
    **kwargs,
) -> None: ...
