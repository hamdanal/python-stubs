from typing import Final

import numpy as np

from pandapower._typing import Float

EPS: Final[np.float64]

# BusT, GenT, BranchT are probably bound to np.ndarray
def pfsoln[BusT, GenT, BranchT](
    baseMVA: Float,
    bus0: BusT,
    gen0: GenT,
    branch0: BranchT,
    svc,
    tcsc,
    ssc,
    vsc,
    Ybus,
    Yf,
    Yt,
    V,
    ref,
    ref_gens,
    Ibus=None,
    limited_gens=None,
) -> tuple[BusT, GenT, BranchT]: ...
