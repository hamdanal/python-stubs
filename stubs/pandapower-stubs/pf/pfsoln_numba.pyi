import numpy as np

from pandapower._typing import Array1D, Array2D, Float, Int

EPS: np.float64

# BusT, GenT, BranchT are probably bound to np.ndarray
def pfsoln[BusT, GenT, BranchT](
    baseMVA: Float,
    bus: BusT,
    gen: GenT,
    branch: BranchT,
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
def pf_solution_single_slack[BusT, GenT, BranchT](
    baseMVA: Float,
    bus: BusT,
    gen: GenT,
    branch: BranchT,
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
def calc_branch_flows(Yy_x, Yy_p, Yy_j, v, baseMVA: Float, dim_x: Int, bus_ind) -> Array1D[np.complex128]: ...
def calc_branch_flows_batch(
    Yy_x, Yy_p, Yy_j, V, baseMVA: Float, dim_x: Int, bus_ind, base_kv
) -> tuple[Array2D[np.complex128], Array2D[np.float64], Array2D[np.float64]]: ...
