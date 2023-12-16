from _typeshed import Incomplete

def browse_dst(input_panel, entry_path_dst) -> None: ...
def get_dst_dir(input_panel, entry_path_dst): ...
def get_filename(entry_fname, save_as: str = "JSON"): ...
def save_net(net, filepath, save_as) -> None: ...
def exit_gracefully(msg, is_err) -> None: ...
def run_export(
    app,
    pv_as_slack,
    pf_variable_p_loads,
    pf_variable_p_gen,
    scale_feeder_loads: bool = False,
    flag_graphics: str = "GPS",
    handle_us: str = "Deactivate",
    save_as: str = "JSON",
    tap_opt: str = "nntap",
    export_controller: bool = True,
    max_iter: Incomplete | None = None,
): ...
def run_verify(net, load_flow_params: Incomplete | None = None): ...
def calc(
    app,
    input_panel,
    entry_path_dst,
    entry_fname,
    is_to_verify,
    is_debug,
    pv_as_slack,
    pf_variable_p_loads,
    pf_variable_p_gen,
    flag_graphics,
    handle_us,
    save_as,
    tap_opt,
    export_controller,
    max_iter_entry,
) -> None: ...
