from _typeshed import Incomplete
from collections.abc import Collection, Iterable
from typing import Literal

import numpy as np
import pandas as pd

from pandapower.auxiliary import pandapowerNet

def select_subnet(
    net: pandapowerNet,
    buses: Iterable[int],
    include_switch_buses: bool = False,
    include_results: bool = False,
    keep_everything_else: bool = False,
) -> pandapowerNet: ...
def merge_nets(
    net1: pandapowerNet, net2: pandapowerNet, validate: bool = True, merge_results: bool = True, tol: float = 1e-9, **kwargs
) -> pandapowerNet: ...
def set_element_status(net: pandapowerNet, buses: Iterable[int], in_service: bool | Iterable[bool]) -> None: ...
def set_isolated_areas_out_of_service(net: pandapowerNet, respect_switches: bool = True) -> None: ...
def repl_to_line(
    net: pandapowerNet, idx: int, std_type: str, name: str | None = None, in_service: bool = False, **kwargs: Incomplete
) -> int: ...
def merge_parallel_line(net: pandapowerNet, idx: int) -> pandapowerNet: ...
def merge_same_bus_generation_plants(
    net: pandapowerNet, add_info: bool = True, error: bool = True, gen_elms: Collection[str] = ("ext_grid", "gen", "sgen")
) -> bool: ...
def close_switch_at_line_with_two_open_switches(net: pandapowerNet) -> None: ...
def fuse_buses(
    net: pandapowerNet, b1: int, b2: int | Iterable[int], drop: bool = True, fuse_bus_measurements: bool = True
) -> None: ...
def drop_elements(
    net: pandapowerNet,
    element_type: str,
    element_index: Iterable[int],
    *,
    # from **kwargs passed to drop_buses
    drop_elements: bool = True,
) -> None: ...
def drop_elements_simple(net: pandapowerNet, element_type: str, element_index: int) -> None: ...
def drop_buses(net: pandapowerNet, buses: Iterable[int], drop_elements: bool = True) -> None: ...
def drop_trafos(net: pandapowerNet, trafos: Iterable[int], table: Literal["trafo", "trafo3w"] = "trafo") -> None: ...
def drop_lines(net: pandapowerNet, lines: Iterable[int]) -> None: ...
def drop_elements_at_buses(
    net: pandapowerNet,
    buses: Iterable[int],
    bus_elements: bool = True,
    branch_elements: bool = True,
    drop_measurements: bool = True,
) -> None: ...
def drop_switches_at_buses(net: pandapowerNet, buses: Iterable[int]) -> None: ...
def drop_measurements_at_elements(
    net: pandapowerNet, element_type: str, idx: int | Collection[int] | None = None, side: Incomplete | None = None
) -> None: ...
def drop_controllers_at_elements(net: pandapowerNet, element_type: str, idx: int | Collection[int] | None = None) -> None: ...
def drop_controllers_at_buses(net: pandapowerNet, buses: int | Iterable[int]) -> None: ...
def drop_duplicated_measurements(
    net: pandapowerNet, buses: Iterable[int] | None = None, keep: Literal["first", "last", False] = "first"
) -> None: ...
def get_inner_branches(
    net: pandapowerNet, buses: Iterable[int], branch_elements: Iterable[str] | None = None
) -> dict[str, pd.Index[int]]: ...
def drop_inner_branches(net: pandapowerNet, buses: Iterable[int], branch_elements: Iterable[str] | None = None) -> None: ...
def drop_out_of_service_elements(net: pandapowerNet) -> None: ...
def drop_inactive_elements(net: pandapowerNet, respect_switches: bool = True) -> None: ...
def create_replacement_switch_for_branch(net: pandapowerNet, element_type: str, element_index: int) -> int: ...
def replace_zero_branches_with_switches(
    net: pandapowerNet,
    elements: tuple[str, ...] = ("line", "impedance"),
    zero_length: bool = True,
    zero_impedance: bool = True,
    in_service_only: bool = True,
    min_length_km: float = 0,
    min_r_ohm_per_km: float = 0,
    min_x_ohm_per_km: float = 0,
    min_c_nf_per_km: float = 0,
    min_rft_pu: float = 0,
    min_xft_pu: float = 0,
    min_rtf_pu: float = 0,
    min_xtf_pu: float = 0,
    drop_affected: bool = False,
) -> dict[str, pd.DataFrame]: ...
def replace_impedance_by_line(
    net: pandapowerNet, index: int | Iterable[int] | None = None, only_valid_replace: bool = True, max_i_ka: float = ...
) -> list[int]: ...
def replace_line_by_impedance(
    net: pandapowerNet,
    index: int | Iterable[int] | None = None,
    sn_mva: float | Iterable[float] | None = None,
    only_valid_replace: bool = True,
) -> list[int]: ...
def replace_ext_grid_by_gen(
    net: pandapowerNet,
    ext_grids: int | Iterable[int] | None = None,
    gen_indices: Iterable[int] | None = None,
    slack: bool = False,
    cols_to_keep: list[str] | None = None,
    add_cols_to_keep: list[str] | None = None,
) -> list[int]: ...
def replace_gen_by_ext_grid(
    net: pandapowerNet,
    gens: int | Iterable[int] | None = None,
    ext_grid_indices: Iterable[int] | None = None,
    cols_to_keep: list[str] | None = None,
    add_cols_to_keep: list[str] | None = None,
) -> list[int]: ...
def replace_gen_by_sgen(
    net: pandapowerNet,
    gens: int | Iterable[int] | None = None,
    sgen_indices: Iterable[int] | None = None,
    cols_to_keep: list[str] | None = None,
    add_cols_to_keep: list[str] | None = None,
) -> list[str]: ...
def replace_sgen_by_gen(
    net: pandapowerNet,
    sgens: int | Iterable[int] | None = None,
    gen_indices: Iterable[int] | None = None,
    cols_to_keep: list[str] | None = None,
    add_cols_to_keep: list[str] | None = None,
) -> list[str]: ...
def replace_pq_elmtype(
    net: pandapowerNet,
    old_element_type: Literal["sgen", "load", "storage"],
    new_element_type: Literal["sgen", "load", "storage"],
    old_indices: int | Iterable[int] | None = None,
    new_indices: Iterable[int] | None = None,
    cols_to_keep: list[str] | None = None,
    add_cols_to_keep: list[str] | None = None,
) -> list[str]: ...
def replace_ward_by_internal_elements(
    net: pandapowerNet, wards: int | Iterable[int] | None = None, log_level: str = "warning"
) -> None: ...
def replace_xward_by_internal_elements(
    net: pandapowerNet, xwards: int | Iterable[int] | None = None, set_xward_bus_limits: bool = False
) -> None: ...
def replace_xward_by_ward(
    net: pandapowerNet, index: int | Collection[int] | None = None, drop: bool = True
) -> list[np.int64]: ...
