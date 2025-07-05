from typing import TypeVar

import numpy as np

from pandapower._typing import Array1D, Array2D, Float, Int

EPS: np.float64

_BusT = TypeVar("_BusT")  # probably bound to ndarray
_GenT = TypeVar("_GenT")  # probably bound to ndarray
_BranchT = TypeVar("_BranchT")  # probably bound to ndarray

def pfsoln(
    baseMVA: Float,
    bus: _BusT,
    gen: _GenT,
    branch: _BranchT,
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
def pf_solution_single_slack(
    baseMVA: Float,
    bus: _BusT,
    gen: _GenT,
    branch: _BranchT,
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
def calc_branch_flows(Yy_x, Yy_p, Yy_j, v, baseMVA: Float, dim_x: Int, bus_ind) -> Array1D[np.complex128]: ...
def calc_branch_flows_batch(
    Yy_x, Yy_p, Yy_j, V, baseMVA: Float, dim_x: Int, bus_ind, base_kv
) -> tuple[Array2D[np.complex128], Array2D[np.float64], Array2D[np.float64]]: ...
