from pandapower.grid_equivalents.auxiliary import (
    adaptation_phase_shifter as adaptation_phase_shifter,
    get_boundary_vp as get_boundary_vp,
)

def get_equivalent(
    net,
    eq_type,
    boundary_buses,
    internal_buses,
    return_internal: bool = ...,
    show_computing_time: bool = ...,
    ward_type: str = ...,
    adapt_va_degree: bool = ...,
    calculate_voltage_angles: bool = ...,
    allow_net_change_for_convergence: bool = ...,
    runpp_fct=...,
    **kwargs,
): ...
def merge_internal_net_and_equivalent_external_net(
    net_eq, net_internal, eq_type, show_computing_time: bool = ..., calc_volt_angles: bool = ..., **kwargs
): ...
def drop_repeated_characteristic(net) -> None: ...
