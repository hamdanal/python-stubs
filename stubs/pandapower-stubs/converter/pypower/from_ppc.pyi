from pandapower.auxiliary import pandapowerNet

ppc_elms: list[str]

def from_ppc(ppc, f_hz: float = 50, validate_conversion: bool = False, **kwargs) -> pandapowerNet: ...
def validate_from_ppc(
    ppc,
    net: pandapowerNet,
    max_diff_values={
        "bus_vm_pu": 1e-06,
        "bus_va_degree": 1e-05,
        "branch_p_mw": 1e-06,
        "branch_q_mvar": 1e-06,
        "gen_p_mw": 1e-06,
        "gen_q_mvar": 1e-06,
    },
) -> bool: ...
