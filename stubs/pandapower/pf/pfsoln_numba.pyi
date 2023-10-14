from _typeshed import Incomplete

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
    Ibus: Incomplete | None = None,
    limited_gens: Incomplete | None = None,
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
    Ibus: Incomplete | None = None,
    limited_gens: Incomplete | None = None,
): ...
def calc_branch_flows(Yy_x, Yy_p, Yy_j, v, baseMVA, dim_x, bus_ind): ...
def calc_branch_flows_batch(Yy_x, Yy_p, Yy_j, V, baseMVA, dim_x, bus_ind, base_kv): ...
