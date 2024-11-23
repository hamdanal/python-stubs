from _typeshed import Incomplete
from collections.abc import Iterable
from logging import Logger
from typing import Any, Literal, overload
from typing_extensions import TypeAlias

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from pandas._typing import Axes

from pandapower.auxiliary import pandapowerNet

_PMode: TypeAlias = Literal["load", "gen"]
_QMode: TypeAlias = Literal["underexcited", "overexcited"]

GRAPHS_EQUAL_POSSIBLE: bool

def element_bus_tuples(
    bus_elements: bool = True, branch_elements: bool = True, res_elements: bool = False
) -> set[tuple[str, str]]: ...
def pp_elements(
    bus: bool = True,
    bus_elements: bool = True,
    branch_elements: bool = True,
    other_elements: bool = True,
    cost_tables: bool = False,
    res_elements: bool = False,
) -> set[str]: ...
def branch_element_bus_dict(include_switch: bool = False, sort: bool = False) -> dict[str, list[str]]: ...
def signing_system_value(elm: str) -> Literal[-1, 1]: ...
@overload
def pq_from_cosphi(s: float, cosphi: float, qmode: _QMode, pmode: _PMode) -> tuple[float, float]: ...  # type: ignore[overload-overlap]
@overload
def pq_from_cosphi(
    s: Iterable[float], cosphi: float | Iterable[float], qmode: _QMode | Iterable[_QMode], pmode: _PMode | Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float], cosphi: Iterable[float], qmode: _QMode | Iterable[_QMode], pmode: _PMode | Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float], cosphi: float | Iterable[float], qmode: Iterable[_QMode], pmode: _PMode | Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float], cosphi: float | Iterable[float], qmode: _QMode | Iterable[_QMode], pmode: Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float],
    cosphi: float | Iterable[float],
    qmode: _QMode | Iterable[_QMode],
    pmode: _PMode | Iterable[_PMode],
) -> tuple[float, float] | tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def cosphi_from_pq(p: float, q: float) -> tuple[float, float, _PMode, _QMode]: ...
@overload
def cosphi_from_pq(
    p: Iterable[float], q: float | Iterable[float]
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.str_], NDArray[np.str_]]: ...
@overload
def cosphi_from_pq(
    p: float | Iterable[float], q: Iterable[float]
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.str_], NDArray[np.str_]]: ...
@overload
def cosphi_from_pq(
    p: float | Iterable[float], q: float | Iterable[float]
) -> (
    tuple[float, float, _PMode, _QMode] | tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.str_], NDArray[np.str_]]
): ...
def dataframes_equal(df1: pd.DataFrame, df2: pd.DataFrame, ignore_index_order: bool = True, **kwargs: Incomplete) -> bool: ...
def compare_arrays(x: NDArray[Any], y: NDArray[Any]) -> NDArray[np.bool_]: ...
def log_to_level(msg: object, passed_logger: Logger, level: str) -> None: ...
def lf_info(net: pandapowerNet, numv: int = 1, numi: int = 1) -> None: ...
def opf_task(
    net: pandapowerNet, delta_pq: float = 1e-3, keep: bool = False, log: bool = True
) -> dict[str, dict[Incomplete, Incomplete]]: ...
def switch_info(net: pandapowerNet, sidx: int) -> None: ...
def overloaded_lines(net: pandapowerNet, max_load: int = 100) -> pd.Index[int]: ...
def violated_buses(net: pandapowerNet, min_vm_pu: float, max_vm_pu: float) -> pd.Index[int]: ...
def nets_equal(
    net1: pandapowerNet,
    net2: pandapowerNet,
    check_only_results: bool = False,
    check_without_results: bool = False,
    exclude_elms: Iterable[str] | None = None,
    name_selection: Iterable[str] | None = None,
    **kwargs,
) -> bool: ...
def clear_result_tables(net: pandapowerNet) -> None: ...
def add_column_from_node_to_elements(
    net: pandapowerNet,
    column: str,
    replace: bool,
    elements: Iterable[str] | None = None,
    branch_bus: list[str] | None = None,
    verbose: bool = True,
) -> None: ...
def add_column_from_element_to_elements(
    net: pandapowerNet, column: str, replace: bool, elements: Iterable[str] | None = None, continue_on_missing_column: bool = True
) -> None: ...
def add_zones_to_elements(
    net: pandapowerNet, replace: bool = True, elements: Iterable[str] | None = None, **kwargs: Incomplete
) -> None: ...
def reindex_buses(net: pandapowerNet, bus_lookup: dict[int, int]) -> dict[int, int]: ...
def create_continuous_bus_index(net: pandapowerNet, start: int = 0, store_old_index: bool = False) -> dict[int, int]: ...
def reindex_elements(
    net: pandapowerNet,
    element: str,
    new_indices: Axes | None = None,
    old_indices: Axes | None = None,
    lookup: dict[int, int] | None = None,
) -> None: ...
def create_continuous_elements_index(net: pandapowerNet, start: int = 0, add_df_to_reindex: Iterable[str] = ...) -> None: ...
def set_scaling_by_type(
    net: pandapowerNet, scalings: dict[str, float], scale_load: bool = True, scale_sgen: bool = True
) -> None: ...
def set_data_type_of_columns_to_default(net: pandapowerNet) -> None: ...
def close_switch_at_line_with_two_open_switches(net: pandapowerNet) -> None: ...
def fuse_buses(
    net: pandapowerNet, b1: int, b2: int | Iterable[int], drop: bool = True, fuse_bus_measurements: bool = True
) -> None: ...
def drop_buses(net: pandapowerNet, buses: Iterable[int], drop_elements: bool = True) -> None: ...
def drop_switches_at_buses(net: pandapowerNet, buses: Iterable[int]) -> None: ...
def drop_elements_at_buses(
    net: pandapowerNet,
    buses: Iterable[int],
    bus_elements: bool = True,
    branch_elements: bool = True,
    drop_measurements: bool = True,
) -> None: ...
def drop_trafos(net: pandapowerNet, trafos: Iterable[int], table: Literal["trafo", "trafo3w"] = "trafo") -> None: ...
def drop_lines(net: pandapowerNet, lines: Iterable[int]) -> None: ...
def drop_measurements_at_elements(
    net: pandapowerNet, element_type: str, idx: int | Iterable[int] | None = None, side: Incomplete | None = None
) -> None: ...
def drop_duplicated_measurements(
    net: pandapowerNet, buses: Incomplete | None = None, keep: Literal["first", "last", False] = "first"
) -> None: ...
def get_connecting_branches(
    net: pandapowerNet, buses1: Iterable[int], buses2: Iterable[int], branch_elements: Iterable[str] | None = None
) -> dict[str, pd.Index[int]]: ...
def get_inner_branches(
    net: pandapowerNet, buses: Iterable[int], branch_elements: Iterable[str] | None = None
) -> dict[str, pd.Index[int]]: ...
def drop_inner_branches(net: pandapowerNet, buses: Iterable[int], branch_elements: Iterable[str] | None = None) -> None: ...
def set_element_status(net: pandapowerNet, buses: Iterable[int], in_service: bool | Iterable[bool]) -> None: ...
def set_isolated_areas_out_of_service(net: pandapowerNet, respect_switches: bool = True) -> None: ...
def drop_elements_simple(net: pandapowerNet, element: str, idx: int) -> None: ...
def drop_out_of_service_elements(net: pandapowerNet) -> None: ...
def drop_inactive_elements(net: pandapowerNet, respect_switches: bool = True) -> None: ...
def drop_from_group(net: pandapowerNet, index: int, element_type: str, element_index: int | Iterable[int]) -> None: ...
def drop_from_groups(
    net: pandapowerNet, element_type: str, element_index: int | Iterable[int], index: int | Iterable[int] | None = None
) -> None: ...
def drop_group(net: pandapowerNet, index: int) -> None: ...
def drop_group_and_elements(net: pandapowerNet, index: int) -> None: ...
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
def repl_to_line(
    net: pandapowerNet, idx: int, std_type: str, name: str | None = None, in_service: bool = False, **kwargs: Incomplete
) -> int: ...
def merge_parallel_line(net: pandapowerNet, idx: int) -> pandapowerNet: ...
def merge_same_bus_generation_plants(
    net: pandapowerNet, add_info: bool = True, error: bool = True, gen_elms: list[str] = ["ext_grid", "gen", "sgen"]
) -> bool: ...
def create_replacement_switch_for_branch(net: pandapowerNet, element: str, idx: int) -> int: ...
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
    old_elm: Literal["sgen", "load", "storage"],
    new_elm: Literal["sgen", "load", "storage"],
    old_indices: int | Iterable[int] | None = None,
    new_indices: Iterable[int] | None = None,
    cols_to_keep: list[str] | None = None,
    add_cols_to_keep: list[str] | None = None,
) -> list[str]: ...
def replace_ward_by_internal_elements(net: pandapowerNet, wards: int | Iterable[int] | None = None) -> None: ...
def replace_xward_by_internal_elements(net: pandapowerNet, xwards: int | Iterable[int] | None = None) -> None: ...
@overload
def get_element_index(net: pandapowerNet, element: str, name: str, exact_match: Literal[True] = True) -> int: ...
@overload
def get_element_index(net: pandapowerNet, element: str, name: str, exact_match: Literal[False]) -> pd.Index[int]: ...
@overload
def get_element_index(net: pandapowerNet, element: str, name: str, exact_match: bool = True) -> int | pd.Index[int]: ...
@overload
def get_element_indices(
    net: pandapowerNet, element: str | Iterable[str], name: str | Iterable[str], exact_match: Literal[True] = True
) -> list[int]: ...
@overload
def get_element_indices(
    net: pandapowerNet, element: str | Iterable[str], name: str | Iterable[str], exact_match: Literal[False]
) -> list[pd.Index[int]]: ...
@overload
def get_element_indices(
    net: pandapowerNet, element: str | Iterable[str], name: str | Iterable[str], exact_match: bool = True
) -> list[int | pd.Index[int]]: ...
def next_bus(net: pandapowerNet, bus: int, element_id: int, et: str = "line", **kwargs: Incomplete) -> int: ...
def get_connected_elements(
    net: pandapowerNet, element: str, buses: int | Iterable[int], respect_switches: bool = True, respect_in_service: bool = False
) -> set[int]: ...
def get_connected_buses(
    net: pandapowerNet,
    buses: int | Iterable[int],
    consider: Iterable[str] = ("l", "s", "t", "t3", "i"),
    respect_switches: bool = True,
    respect_in_service: bool = False,
) -> set[int]: ...
def get_connected_buses_at_element(net: pandapowerNet, element: int, et: str, respect_in_service: bool = False) -> set[int]: ...
def get_connected_switches(
    net: pandapowerNet,
    buses: int | Iterable[int],
    consider: Iterable[str] = ("b", "l", "t", "t3"),
    status: Literal["all", "closed", "open"] = "all",
) -> set[int]: ...
def get_connected_elements_dict(
    net: pandapowerNet,
    buses: int | Iterable[int],
    respect_switches: bool = True,
    respect_in_service: bool = False,
    include_empty_lists: bool = False,
    element_types: Iterable[str] | None = None,
    **kwargs: bool,
) -> dict[str, list[int]]: ...
def get_gc_objects_dict() -> dict[type[Any], int]: ...
def false_elm_links(net: pandapowerNet, elm: str, col: str, target_elm: str | Iterable[str]) -> pd.Index[int]: ...
def false_elm_links_loop(net: pandapowerNet, elms: Iterable[str] | None = None) -> dict[str, pd.Index[int]]: ...
def read_from_net(
    net: pandapowerNet,
    element: str,
    index: int | Iterable[int],
    variable: str,
    flag: Literal["auto", "single_index", "all_index", "loc", "object"] = "auto",
) -> Any: ...
def write_to_net(
    net: pandapowerNet,
    element: str,
    index: int | Iterable[int],
    variable: str,
    values: Any,
    flag: Literal["auto", "single_index", "all_index", "loc", "object"] = "auto",
) -> None: ...
def group_row(net: pandapowerNet, index: int, element_type: str) -> pd.Series[Incomplete]: ...
def group_element_index(net: pandapowerNet, index: int, element_type: str) -> pd.Index[int]: ...
