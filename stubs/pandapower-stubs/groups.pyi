from collections.abc import Collection, Iterable
from typing import Any, Literal, NoReturn

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike

from pandapower._typing import Array1D, Bool, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def drop_group(net: pandapowerNet, index: Int) -> None: ...
def drop_group_and_elements(net: pandapowerNet, index: Int) -> None: ...
def append_to_group(*args, **kwargs) -> NoReturn: ...
def attach_to_groups(
    net: pandapowerNet,
    index: Iterable[Int],
    element_types: ScalarOrVector[str],
    element_indices: Collection[Collection[Int]],
    reference_columns: ScalarOrVector[str] | None = None,
) -> None: ...
def attach_to_group(
    net: pandapowerNet,
    index: Int,
    element_types: ScalarOrVector[str],
    element_indices: Collection[Collection[Int]],
    reference_columns: ScalarOrVector[str] | None = None,
    take_existing_reference_columns: Bool = True,
) -> None: ...
def drop_from_group(*args, **kwargs) -> NoReturn: ...
def detach_from_group(net: pandapowerNet, index: Int, element_type: str, element_index: ScalarOrVector[Int]) -> None: ...
def drop_from_groups(*args, **kwargs) -> NoReturn: ...
def detach_from_groups(
    net: pandapowerNet, element_type: str, element_index: ScalarOrVector[Int], index: Int | ArrayLike | None = None
) -> None: ...
def group_element_lists(net: pandapowerNet, index: Int) -> tuple[list[str], list[list[int]], list[str | None]]: ...
def group_name(net: pandapowerNet, index: Int) -> str: ...
def group_index(net: pandapowerNet, name: str) -> int: ...
def group_element_index(net: pandapowerNet, index: Int, element_type: str) -> pd.Index[int]: ...
def group_row(net: pandapowerNet, index: Int, element_type: str) -> pd.Series[Any]: ...
def isin_group(
    net: pandapowerNet,
    element_type: str,
    element_index: ScalarOrVector[Int],
    index: ScalarOrVector[Int] | None = None,
    drop_empty_lines: Bool = True,
) -> np.bool | Array1D[np.bool]: ...
def element_associated_groups(
    net: pandapowerNet,
    element_type: str,
    element_index: ScalarOrVector[Int],
    return_empties: Bool = True,
    drop_empty_lines: Bool = True,
) -> dict[int, list[int]]: ...
def count_group_elements(net: pandapowerNet, index: int) -> pd.Series[int]: ...
def groups_equal(
    net: pandapowerNet,
    index1: Int,
    index2: Int,
    *,
    # kwargs passed to pd.testing.assert_frame_equal
    check_dtype: bool | Literal["equiv"] = True,
    check_index_type: bool | Literal["equiv"] = "equiv",
    check_column_type: bool | Literal["equiv"] = "equiv",
    check_frame_type: bool = True,
    check_names: bool = True,
    by_blocks: bool = False,
    check_exact: bool = ...,
    check_datetimelike_compat: bool = False,
    check_categorical: bool = True,
    check_like: bool = False,
    check_freq: bool = True,
    check_flags: bool = True,
    rtol: float = ...,
    atol: float = ...,
    obj: str = "DataFrame",
) -> bool: ...
def compare_group_elements(net: pandapowerNet, index1: Int, index2: Int) -> bool: ...
def check_unique_group_names(*args, **kwargs) -> NoReturn: ...
def check_unique_group_rows(net: pandapowerNet, raise_error: Bool = True, log_level: str = "warning") -> None: ...
def remove_not_existing_group_members(net: pandapowerNet, verbose: Bool = True) -> None: ...
def ensure_lists_in_group_element_column(net: pandapowerNet, drop_empty_lines: Bool = True) -> None: ...
def group_entries_exist_in_element_table(net: pandapowerNet, index: Int, element_type: str) -> Array1D[np.bool]: ...
def set_group_in_service(net: pandapowerNet, index: Int) -> None: ...
def set_group_out_of_service(net: pandapowerNet, index: Int) -> None: ...
def set_value_to_group(
    net: pandapowerNet, index: Int, value: object, column: str, replace: Bool = True, append_column: Bool = True
) -> None: ...
def group_res_power_per_bus(net: pandapowerNet, index: Int) -> pd.DataFrame: ...
def group_res_p_mw(net: pandapowerNet, index: Int) -> np.float64: ...
def group_res_q_mvar(net: pandapowerNet, index: Int) -> np.float64: ...
def set_group_reference_column(
    net: pandapowerNet, index: Int, reference_column: str, element_type: str | None = None
) -> None: ...
def return_group_as_net(
    net: pandapowerNet,
    index: Int,
    keep_everything_else: Bool = False,
    verbose: Bool = True,
    *,
    # extracted from **kwargs
    add_stdtypes: Bool = True,
) -> pandapowerNet: ...
def elements_connected_to_group(
    net: pandapowerNet,
    index: Int,
    element_types: Iterable[str],
    find_buses_only_from_buses: Bool = False,
    respect_switches: Bool = True,
    respect_in_service: Bool = False,
    include_empty_lists: Bool = False,
) -> dict[str, pd.Index[int]]: ...
