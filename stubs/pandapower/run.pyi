from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Literal

from pandapower.auxiliary import pandapowerNet
from pandas import Series

def set_user_pf_options(net: pandapowerNet, overwrite: bool = ..., **kwargs: Incomplete) -> None: ...
def runpp(
    net: pandapowerNet,
    algorithm: Literal["nr", "iwamoto_nr", "bfsw", "gs", "fdbx", "fdxb"] = ...,
    calculate_voltage_angles: bool | Literal["auto"] = ...,
    init: Literal["auto", "flat", "dc", "results"] = ...,
    max_iteration: int | Literal["auto"] = ...,
    tolerance_mva: float = ...,
    trafo_model: Literal["t", "pi"] = ...,
    trafo_loading: Literal["current", "power"] = ...,
    enforce_q_lims: bool = ...,
    check_connectivity: bool = ...,
    voltage_depend_loads: bool = ...,
    consider_line_temperature: bool = ...,
    run_control: bool = ...,
    distributed_slack: bool = ...,
    tdpf: bool = ...,
    tdpf_delay_s: float | None = ...,
    # the following are defined as **kwargs and documented as follows
    lightsim2grid: bool | Literal["auto"] = ...,
    numba: bool = ...,
    switch_rx_ratio: float = ...,
    delta_q: float = ...,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = ...,
    v_debug: bool = ...,
    init_vm_pu: float | Iterable[float] | Series[float] | Literal["auto", "flat", "results"] | None = ...,
    init_va_degree: float | Iterable[float] | Series[float] | Literal["auto", "dc", "flat", "results"] | None = ...,
    recycle: dict[Literal["bus_pq", "trafo", "gen"], bool] | None = ...,
    neglect_open_switch_branches: bool = ...,
    tdpf_update_r_theta: bool = ...,
    **kwargs: Incomplete,  #
) -> None: ...
def rundcpp(
    net: pandapowerNet,
    trafo_model: Literal["t", "pi"] = ...,
    trafo_loading: Literal["current", "power"] = ...,
    recycle: dict[Literal["bus_pq", "trafo", "gen"], bool] | None = ...,
    check_connectivity: bool = ...,
    switch_rx_ratio: float = ...,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = ...,
    **kwargs: Incomplete,
) -> None: ...
def runopp(
    net: pandapowerNet,
    verbose: bool = ...,
    calculate_voltage_angles: bool = ...,
    check_connectivity: bool = ...,
    suppress_warnings: bool = ...,
    switch_rx_ratio: int = ...,
    delta: float = ...,
    init: Literal["flat", "dc", "results"] = ...,
    numba: bool = ...,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = ...,
    consider_line_temperature: bool = ...,
    **kwargs: Incomplete,
) -> None: ...
def rundcopp(
    net: pandapowerNet,
    verbose: bool = ...,
    check_connectivity: bool = ...,
    suppress_warnings: bool = ...,
    switch_rx_ratio: float = ...,
    delta: float = ...,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = ...,
    **kwargs: Incomplete,
) -> None: ...
