from _typeshed import SupportsGetItem
from collections.abc import Collection, Iterable
from typing import TypeVar

import pandas as pd

from pandapower._typing import Bool, Int, RunPPFunc
from pandapower.auxiliary import pandapowerNet

_S = TypeVar("_S", tuple[Int, ...], list[Int])

impedance_columns: list[str]

def add_ext_grids_to_boundaries(
    net: pandapowerNet,
    boundary_buses: Iterable[Int],
    adapt_va_degree: Bool = False,
    runpp_fct: RunPPFunc = ...,
    calc_volt_angles: Bool = True,
    allow_net_change_for_convergence: Bool = False,
) -> pd.Index[int]: ...
def drop_internal_branch_elements(
    net: pandapowerNet, internal_buses: Collection[Int], branch_elements: Iterable[Int] | None = None
) -> None: ...
def calc_zpbn_parameters(
    net: pandapowerNet, boundary_buses: _S, all_external_buses: _S, slack_as: str = "gen", existing_shift_degree: Bool = False
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]: ...
def drop_assist_elms_by_creating_ext_net(net: pandapowerNet, elms: Iterable[str] | None = None) -> None: ...
def build_ppc_and_Ybus(net: pandapowerNet) -> None: ...
def drop_measurements_and_controllers(net: pandapowerNet, buses: Collection[Int], skip_controller: Bool = False) -> None: ...
def ensure_origin_id(net: pandapowerNet, elms: Iterable[str] | None = None) -> None: ...
def drop_and_edit_cost_functions(
    net: pandapowerNet, buses: Collection[Int], drop_cost: Bool, add_origin_id: Bool, check_unique_elms_name: Bool = True
) -> None: ...
def match_cost_functions_and_eq_net(net: pandapowerNet, boundary_buses: Iterable[Int], eq_type: str) -> None: ...
def get_boundary_vp(
    net_eq: pandapowerNet, bus_lookups: SupportsGetItem[str, SupportsGetItem[str, Collection[Int]]]
) -> tuple[pd.DataFrame, pd.DataFrame]: ...
def adaptation_phase_shifter(net: pandapowerNet, v_boundary: pd.DataFrame, p_boundary: pd.DataFrame) -> pandapowerNet: ...
def replace_motor_by_load(net: pandapowerNet, all_external_buses: Collection[Int]) -> None: ...
