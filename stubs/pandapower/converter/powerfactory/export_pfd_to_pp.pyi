from _typeshed import Incomplete

from .run_import import prj_import as prj_import

def from_pfd(
    app,
    prj_name: str,
    path_dst: Incomplete | None = None,
    pv_as_slack: bool = False,
    pf_variable_p_loads: str = "plini",
    pf_variable_p_gen: str = "pgini",
    flag_graphics: str = "GPS",
    tap_opt: str = "nntap",
    export_controller: bool = True,
    handle_us: str = "Deactivate",
    is_unbalanced: bool = False,
): ...
def execute(
    app,
    path_src,
    path_dst,
    pv_as_slack,
    scale_feeder_loads: bool = False,
    var_load: str = "plini",
    var_gen: str = "pgini",
    flag_graphics: str = "GPS",
): ...
def import_project(
    path_src,
    app,
    name: str = "Import",
    import_folder: str = "",
    template: Incomplete | None = None,
    clear_import_folder: bool = False,
): ...
def check_network(app): ...
