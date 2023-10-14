import json
from _typeshed import Incomplete

CONSTRUCTION_COST: int

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj): ...

def convert_pp_to_pm(
    net,
    pm_file_path: Incomplete | None = None,
    correct_pm_network_data: bool = True,
    calculate_voltage_angles: bool = True,
    ac: bool = True,
    silence: bool = True,
    trafo_model: str = "t",
    delta: float = 1e-08,
    trafo3w_losses: str = "hv",
    check_connectivity: bool = True,
    pp_to_pm_callback: Incomplete | None = None,
    pm_model: str = "ACPPowerModel",
    pm_solver: str = "ipopt",
    pm_mip_solver: str = "cbc",
    pm_nl_solver: str = "ipopt",
    opf_flow_lim: str = "S",
    pm_tol: float = 1e-08,
    voltage_depend_loads: bool = False,
    from_time_step: Incomplete | None = None,
    to_time_step: Incomplete | None = None,
    **kwargs,
): ...
def convert_to_pm_structure(
    net, opf_flow_lim: str = "S", from_time_step: Incomplete | None = None, to_time_step: Incomplete | None = None, **kwargs
): ...
def dump_pm_json(pm, buffer_file: Incomplete | None = None): ...
def get_branch_angles(row, correct_pm_network_data): ...
def create_pm_lookups(net, pm_lookup): ...
def ppc_to_pm(net, ppci): ...
def add_pm_options(pm, net): ...
def build_ne_branch(net, ppc): ...
def init_ne_line(net, new_line_index, construction_costs: Incomplete | None = None) -> None: ...
def add_params_to_pm(net, pm): ...
def add_time_series_to_pm(net, pm, from_time_step, to_time_step): ...
def allow_multi_ext_grids(net, pm, ext_grids: Incomplete | None = None): ...
