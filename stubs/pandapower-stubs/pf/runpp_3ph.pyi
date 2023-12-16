from pandapower.auxiliary import pandapowerNet, ppException

class Not_implemented(ppException): ...

def runpp_3ph(
    net: pandapowerNet,
    calculate_voltage_angles: bool = True,
    init: str = "auto",
    max_iteration: str = "auto",
    tolerance_mva: float = 1e-08,
    trafo_model: str = "t",
    trafo_loading: str = "current",
    enforce_q_lims: bool = False,
    numba: bool = True,
    recycle: dict[str, bool] | None = None,
    check_connectivity: bool = True,
    switch_rx_ratio: float = 2.0,
    delta_q: float = 0,
    v_debug: bool = False,
    **kwargs,
) -> None: ...
