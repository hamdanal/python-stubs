from _typeshed import Incomplete
from collections.abc import Generator

def ga(element, attr): ...
def from_pf(
    dict_net,
    pv_as_slack: bool = True,
    pf_variable_p_loads: str = "plini",
    pf_variable_p_gen: str = "pgini",
    flag_graphics: str = "GPS",
    tap_opt: str = "nntap",
    export_controller: bool = True,
    handle_us: str = "Deactivate",
    max_iter: Incomplete | None = None,
    is_unbalanced: bool = False,
): ...
def get_graphic_object(item): ...
def add_additional_attributes(
    item, net, element, element_id, attr_list: Incomplete | None = None, attr_dict: Incomplete | None = None
) -> None: ...
def create_bus(net, item, flag_graphics, is_unbalanced) -> None: ...
def get_pf_bus_results(net, item, bid, is_unbalanced) -> None: ...
def find_bus_index_in_net(pf_bus, net): ...
def get_connection_nodes(net, item, num_nodes): ...
def import_switch(item, idx_cubicle): ...
def create_connection_switches(net, item, number_switches, et, buses, elements) -> None: ...
def get_coords_from_buses(net, from_bus, to_bus, **kwargs): ...
def get_coords_from_item(item): ...
def get_coords_from_grf_object(item): ...
def create_line(net, item, flag_graphics, n, is_unbalanced) -> None: ...
def point_len(p1, p2): ...
def calc_len_coords(coords): ...
def cut_coords_segment(p1, p2, split_len): ...
def get_section_coords(coords, sec_len, start_len, scale_factor): ...
def segment_buses(net, bus1, bus2, num_sections, line_name) -> Generator[Incomplete, None, None]: ...
def create_line_sections(net, item_list, line, bus1, bus2, coords, parallel, is_unbalanced, **kwargs): ...
def create_line_normal(net, item, bus1, bus2, name, parallel, is_unbalanced): ...
def get_pf_line_results(net, item, lid, is_unbalanced) -> None: ...
def create_line_type(net, item, cable_in_air: bool = False): ...
def monopolar_in_service(item): ...
def create_ext_net(net, item, pv_as_slack, is_unbalanced): ...
def get_pf_ext_grid_results(net, item, xid, is_unbalanced) -> None: ...
def map_power_var(pf_var, map_var): ...
def map_type_var(pf_load_type): ...
def map_sgen_type_var(pf_sgen_type): ...
def get_power_multiplier(item, var): ...
def ask_load_params(item, pf_variable_p_loads, dict_net, variables): ...
def ask_unbalanced_load_params(item, pf_variable_p_loads, dict_net, variables): ...
def find_section(load, sections): ...
def make_split_dict(line): ...
def split_line_add_bus(net, split_dict): ...
def split_line_add_bus_old(net, item, parent): ...
def create_load(net, item, pf_variable_p_loads, dict_net, is_unbalanced) -> None: ...
def get_pf_load_results(net, item, ld, is_unbalanced) -> None: ...
def ask_gen_params(item, pf_variable_p_gen, *vars): ...
def ask_unbalanced_sgen_params(item, pf_variable_p_sgen, *vars): ...
def create_sgen_genstat(net, item, pv_as_slack, pf_variable_p_gen, dict_net, is_unbalanced) -> None: ...
def get_pf_sgen_results(net, item, sg, is_unbalanced, element: str = "sgen") -> None: ...
def create_sgen_neg_load(net, item, pf_variable_p_loads, dict_net) -> None: ...
def create_sgen_sym(net, item, pv_as_slack, pf_variable_p_gen, dict_net) -> None: ...
def create_sgen_asm(net, item, pf_variable_p_gen, dict_net) -> None: ...
def create_trafo_type(net, item): ...
def create_trafo(net, item, export_controller: bool = True, tap_opt: str = "nntap", is_unbalanced: bool = False): ...
def get_pf_trafo_results(net, item, tid, is_unbalanced) -> None: ...
def create_trafo3w(net, item, tap_opt: str = "nntap") -> None: ...
def propagate_bus_coords(net, bus1, bus2) -> None: ...
def create_coup(net, item, is_fuse: bool = False) -> None: ...
def create_shunt(net, item) -> None: ...
def create_zpu(net, item) -> None: ...
def create_vac(net, item) -> None: ...
def create_sind(net, item) -> None: ...
def split_line_at_length(net, line, length_pos): ...
def get_lodlvp_length_pos(line_item, lod_item): ...
def get_next_line(net, line): ...
def split_line(net, line_idx, pos_at_line, line_item): ...
def calc_segment_length(x1, y1, x2, y2): ...
def get_scale_factor(length_line, coords): ...
def break_coords_sections(coords, section_length, scale_factor_length): ...
def set_new_coords(net, bus_id, line_idx, new_line_idx, line_length, pos_at_line) -> None: ...
def get_lvp_for_lines(dict_net): ...
def get_pos_at_sec(net, lvp_dict, line_item, load_item): ...
def write_line_order(net) -> None: ...
def split_all_lines(net, lvp_dict) -> None: ...
def remove_folder_of_std_types(net) -> None: ...
