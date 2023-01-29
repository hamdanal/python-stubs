from _typeshed import Incomplete

from pandapower.pypower.idx_brch import ANGMAX as ANGMAX, ANGMIN as ANGMIN, RATE_B as RATE_B, RATE_C as RATE_C
from pandapower.pypower.idx_bus import BUS_AREA as BUS_AREA, VM as VM

ppc_elms: Incomplete

def from_ppc(ppc, f_hz: int = ..., validate_conversion: bool = ..., **kwargs): ...
def validate_from_ppc(ppc, net, max_diff_values=...): ...
