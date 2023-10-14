from _typeshed import Incomplete
from collections.abc import Iterable

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike, NDArray
from pandapower.auxiliary import pandapowerNet

def drop_group(net: pandapowerNet, index: int) -> None: ...
def drop_group_and_elements(net: pandapowerNet, index: int) -> None: ...
def attach_to_groups(
    net: pandapowerNet,
    index: Iterable[int],
    element_types: str | Iterable[str],
    elements: Iterable[list[Incomplete]],
    reference_columns: str | Iterable[str] | None = None,
) -> None: ...
def attach_to_group(
    net: pandapowerNet,
    index: int,
    element_types: str | Iterable[str],
    elements: Iterable[list[Incomplete]],
    reference_columns: str | Iterable[str] | None = None,
    take_existing_reference_columns: bool = True,
) -> None: ...
def detach_from_group(net: pandapowerNet, index: int, element_type: str, element_index: int | Iterable[int]) -> None: ...
def detach_from_groups(
    net: pandapowerNet, element_type: str, element_index: int | Iterable[int], index: int | ArrayLike | None = None
) -> None: ...
def group_element_lists(net: pandapowerNet, index: int) -> tuple[list[Incomplete], ...]: ...
def group_name(net: pandapowerNet, index: int) -> str: ...
def group_index(net: pandapowerNet, name: str) -> int: ...
def group_element_index(net: pandapowerNet, index: int, element_type: str) -> pd.Index[int]: ...
def group_row(net: pandapowerNet, index: int, element_type: str) -> pd.Series[Incomplete]: ...
def isin_group(
    net: pandapowerNet,
    element_type: str,
    element_index: int | Iterable[int],
    index: int | Iterable[int] | None = None,
    drop_empty_lines: bool = True,
) -> bool | NDArray[np.bool_]: ...
def element_associated_groups(
    net: pandapowerNet, element_type: str, element_index: Incomplete, return_empties: bool = True, drop_empty_lines: bool = True
) -> dict[int, list[int]]: ...
def count_group_elements(net: pandapowerNet, index: int) -> pd.Series[int]: ...
def groups_equal(net: pandapowerNet, index1: int, index2: int, **kwargs: Incomplete) -> bool: ...
def compare_group_elements(net: pandapowerNet, index1: int, index2: int) -> bool: ...
def check_unique_group_rows(net: pandapowerNet, raise_error: bool = True, log_level: str = "warning") -> None: ...
def remove_not_existing_group_members(net: pandapowerNet, verbose: bool = True) -> None: ...
def ensure_lists_in_group_element_column(net: pandapowerNet, drop_empty_lines: bool = True) -> None: ...
def group_entries_exist_in_element_table(net: pandapowerNet, index: int, element_type: str) -> NDArray[np.bool_]: ...
def set_group_in_service(net: pandapowerNet, index: int) -> None: ...
def set_group_out_of_service(net: pandapowerNet, index: int) -> None: ...
def set_value_to_group(
    net: pandapowerNet, index: int, value: object, column: str, replace: bool = True, append_column: bool = True
) -> None: ...
def group_res_power_per_bus(net: pandapowerNet, index: int) -> pd.DataFrame: ...
def group_res_p_mw(net: pandapowerNet, index: int) -> float | Incomplete: ...
def group_res_q_mvar(net: pandapowerNet, index: int) -> float | Incomplete: ...
def set_group_reference_column(
    net: pandapowerNet, index: int, reference_column: str, element_type: str | None = None
) -> None: ...
def return_group_as_net(
    net: pandapowerNet, index: int, keep_everything_else: bool = False, verbose: bool = True, **kwargs: Incomplete
) -> pandapowerNet: ...
def elements_connected_to_group(
    net: pandapowerNet,
    index: int,
    element_types: Iterable[str],
    find_buses_only_from_buses: bool = False,
    respect_switches: bool = True,
    respect_in_service: bool = False,
    include_empty_lists: bool = False,
) -> dict[str, pd.Index[int]]: ...
