import json
from _typeshed import Incomplete

CONSTRUCTION_COST: int

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj): ...

def convert_pp_to_pm(
    net,
    pm_file_path: Incomplete | None = ...,
    correct_pm_network_data: bool = ...,
    calculate_voltage_angles: bool = ...,
    ac: bool = ...,
    silence: bool = ...,
    trafo_model: str = ...,
    delta: float = ...,
    trafo3w_losses: str = ...,
    check_connectivity: bool = ...,
    pp_to_pm_callback: Incomplete | None = ...,
    pm_model: str = ...,
    pm_solver: str = ...,
    pm_mip_solver: str = ...,
    pm_nl_solver: str = ...,
    opf_flow_lim: str = ...,
    pm_tol: float = ...,
    voltage_depend_loads: bool = ...,
    from_time_step: Incomplete | None = ...,
    to_time_step: Incomplete | None = ...,
    **kwargs,
): ...
def convert_to_pm_structure(
    net, opf_flow_lim: str = ..., from_time_step: Incomplete | None = ..., to_time_step: Incomplete | None = ..., **kwargs
): ...
def dump_pm_json(pm, buffer_file: Incomplete | None = ...): ...
def get_branch_angles(row, correct_pm_network_data): ...
def create_pm_lookups(net, pm_lookup): ...
def ppc_to_pm(net, ppci): ...
def add_pm_options(pm, net): ...
def build_ne_branch(net, ppc): ...
def init_ne_line(net, new_line_index, construction_costs: Incomplete | None = ...) -> None: ...
def add_params_to_pm(net, pm): ...
def add_time_series_to_pm(net, pm, from_time_step, to_time_step): ...
def allow_multi_ext_grids(net, pm, ext_grids: Incomplete | None = ...): ...
