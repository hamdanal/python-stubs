from _typeshed import Incomplete

from numpy import r_ as r_

EPS: Incomplete

def pfsoln(
    baseMVA,
    bus,
    gen,
    branch,
    Ybus,
    Yf,
    Yt,
    V,
    ref,
    ref_gens,
    Ibus: Incomplete | None = ...,
    limited_gens: Incomplete | None = ...,
): ...
def pf_solution_single_slack(
    baseMVA,
    bus,
    gen,
    branch,
    Ybus,
    Yf,
    Yt,
    V,
    ref,
    ref_gens,
    Ibus: Incomplete | None = ...,
    limited_gens: Incomplete | None = ...,
): ...
def calc_branch_flows(Yy_x, Yy_p, Yy_j, v, baseMVA, dim_x, bus_ind): ...
def calc_branch_flows_batch(Yy_x, Yy_p, Yy_j, V, baseMVA, dim_x, bus_ind, base_kv): ...
