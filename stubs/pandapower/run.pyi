from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Literal

import pandas as pd
from pandapower.auxiliary import pandapowerNet

def set_user_pf_options(net: pandapowerNet, overwrite: bool = False, **kwargs: Incomplete) -> None: ...
def runpp(
    net: pandapowerNet,
    algorithm: Literal["nr", "iwamoto_nr", "bfsw", "gs", "fdbx", "fdxb"] = "nr",
    calculate_voltage_angles: bool | Literal["auto"] = "auto",
    init: Literal["auto", "flat", "dc", "results"] = "auto",
    max_iteration: int | Literal["auto"] = "auto",
    tolerance_mva: float = 1e-8,
    trafo_model: Literal["t", "pi"] = "t",
    trafo_loading: Literal["current", "power"] = "current",
    enforce_q_lims: bool = False,
    check_connectivity: bool = True,
    voltage_depend_loads: bool = True,
    consider_line_temperature: bool = False,
    run_control: bool = False,
    distributed_slack: bool = False,
    tdpf: bool = False,
    tdpf_delay_s: float | None = None,
    # the following are defined as **kwargs and documented as follows
    lightsim2grid: bool | Literal["auto"] = "auto",
    numba: bool = True,
    switch_rx_ratio: float = 2,
    delta_q: float = 0,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = "hv",
    v_debug: bool = False,
    init_vm_pu: float | Iterable[float] | pd.Series[float] | Literal["auto", "flat", "results"] | None = None,
    init_va_degree: float | Iterable[float] | pd.Series[float] | Literal["auto", "dc", "flat", "results"] | None = None,
    recycle: dict[Literal["bus_pq", "trafo", "gen"], bool] | None = None,
    neglect_open_switch_branches: bool = False,
    tdpf_update_r_theta: bool = True,
    **kwargs: Incomplete,
) -> None: ...
def rundcpp(
    net: pandapowerNet,
    trafo_model: Literal["t", "pi"] = "t",
    trafo_loading: Literal["current", "power"] = "current",
    recycle: dict[Literal["bus_pq", "trafo", "gen"], bool] | None = None,
    check_connectivity: bool = True,
    switch_rx_ratio: float = 2,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = "hv",
    **kwargs: Incomplete,
) -> None: ...
def runopp(
    net: pandapowerNet,
    verbose: bool = False,
    calculate_voltage_angles: bool = True,
    check_connectivity: bool = True,
    suppress_warnings: bool = True,
    switch_rx_ratio: float = 2,
    delta: float = 1e-10,
    init: Literal["flat", "dc", "results"] = "flat",
    numba: bool = True,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = "hv",
    consider_line_temperature: bool = False,
    **kwargs: Incomplete,
) -> None: ...
def rundcopp(
    net: pandapowerNet,
    verbose: bool = False,
    check_connectivity: bool = True,
    suppress_warnings: bool = True,
    switch_rx_ratio: float = 0.5,
    delta: float = 1e-10,
    trafo3w_losses: Literal["hv", "mv", "lv", "star"] = "hv",
    **kwargs: Incomplete,
) -> None: ...
