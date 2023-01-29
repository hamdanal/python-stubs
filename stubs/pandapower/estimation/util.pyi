from _typeshed import Incomplete

def estimate_voltage_vector(net): ...
def set_bb_switch_impedance(net, bus_to_be_fused: Incomplete | None = ..., z_ohm: float = ...) -> None: ...
def reset_bb_switch_impedance(net) -> None: ...
def add_virtual_meas_from_loadflow(
    net, v_std_dev: float = ..., p_std_dev: float = ..., q_std_dev: float = ..., seed: int = ..., with_random_error: bool = ...
) -> None: ...
def add_virtual_pmu_meas_from_loadflow(
    net,
    v_std_dev: float = ...,
    i_std_dev: float = ...,
    p_std_dev: float = ...,
    q_std_dev: float = ...,
    dg_std_dev: float = ...,
    seed: int = ...,
    with_random_error: bool = ...,
) -> None: ...
def add_virtual_meas_error(
    net,
    v_std_dev: float = ...,
    i_std_dev: float = ...,
    p_std_dev: float = ...,
    q_std_dev: float = ...,
    dg_std_dev: float = ...,
    with_random_error: bool = ...,
) -> None: ...
