from _typeshed import Incomplete

def estimate_voltage_vector(net): ...
def set_bb_switch_impedance(net, bus_to_be_fused: Incomplete | None = None, z_ohm: float = 0.1) -> None: ...
def reset_bb_switch_impedance(net) -> None: ...
def add_virtual_meas_from_loadflow(
    net,
    v_std_dev: float = 0.01,
    p_std_dev: float = 0.03,
    q_std_dev: float = 0.03,
    seed: int = 14,
    with_random_error: bool = False,
) -> None: ...
def add_virtual_pmu_meas_from_loadflow(
    net,
    v_std_dev: float = 0.001,
    i_std_dev: float = 0.1,
    p_std_dev: float = 0.01,
    q_std_dev: float = 0.01,
    dg_std_dev: float = 0.1,
    seed: int = 14,
    with_random_error: bool = True,
) -> None: ...
def add_virtual_meas_error(
    net,
    v_std_dev: float = 0.001,
    i_std_dev: float = 0.01,
    p_std_dev: float = 0.03,
    q_std_dev: float = 0.03,
    dg_std_dev: float = 0.1,
    with_random_error: bool = True,
) -> None: ...
