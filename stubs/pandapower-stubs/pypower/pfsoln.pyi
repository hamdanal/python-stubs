from typing import Final, TypeVar

import numpy as np

from pandapower._typing import Float

EPS: Final[np.float64]

_BusT = TypeVar("_BusT")  # probably bound to ndarray
_GenT = TypeVar("_GenT")  # probably bound to ndarray
_BranchT = TypeVar("_BranchT")  # probably bound to ndarray

def pfsoln(
    baseMVA: Float,
    bus0: _BusT,
    gen0: _GenT,
    branch0: _BranchT,
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
) -> tuple[_BusT, _GenT, _BranchT]: ...
