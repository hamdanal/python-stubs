from collections.abc import Collection
from typing import Literal

from pandapower._typing import Bool, Int, RunPPFunc
from pandapower.auxiliary import pandapowerNet

def get_equivalent(
    net: pandapowerNet,
    eq_type: Literal["rei", "ward", "xward"],
    boundary_buses: Collection[Int],
    internal_buses: Collection[Int],
    return_internal: Bool = True,
    show_computing_time: Bool = False,
    ward_type: str = "ward_injection",
    adapt_va_degree: Bool = False,
    calculate_voltage_angles: Bool = True,
    allow_net_change_for_convergence: Bool = False,
    runpp_fct: RunPPFunc = ...,
    **kwargs,
) -> pandapowerNet | None: ...
def merge_internal_net_and_equivalent_external_net(
    net_eq: pandapowerNet, net_internal: pandapowerNet, fuse_bus_column: str = "auto", show_computing_time: bool = False, **kwargs
) -> pandapowerNet: ...
def drop_repeated_characteristic(net: pandapowerNet) -> None: ...
