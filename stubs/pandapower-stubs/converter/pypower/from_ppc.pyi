from _typeshed import Incomplete

from pandapower.pypower.idx_brch import ANGMAX as ANGMAX, ANGMIN as ANGMIN, RATE_B as RATE_B, RATE_C as RATE_C
from pandapower.pypower.idx_bus import BUS_AREA as BUS_AREA, VM as VM

ppc_elms: Incomplete

def from_ppc(ppc, f_hz: int = 50, validate_conversion: bool = False, **kwargs): ...
def validate_from_ppc(
    ppc,
    net,
    max_diff_values={
        "bus_vm_pu": 1e-06,
        "bus_va_degree": 1e-05,
        "branch_p_mw": 1e-06,
        "branch_q_mvar": 1e-06,
        "gen_p_mw": 1e-06,
        "gen_q_mvar": 1e-06,
    },
): ...
