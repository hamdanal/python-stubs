def get_equivalent(
    net,
    eq_type,
    boundary_buses,
    internal_buses,
    return_internal: bool = True,
    show_computing_time: bool = False,
    ward_type: str = "ward_injection",
    adapt_va_degree: bool = False,
    calculate_voltage_angles: bool = True,
    allow_net_change_for_convergence: bool = False,
    runpp_fct=...,
    **kwargs,
): ...
def merge_internal_net_and_equivalent_external_net(
    net_eq, net_internal, eq_type, show_computing_time: bool = False, calc_volt_angles: bool = False, **kwargs
): ...
def drop_repeated_characteristic(net) -> None: ...
