from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any, Literal, overload

import pandas as pd

from pandapower.auxiliary import pandapowerNet

@overload
def get_element_index(net: pandapowerNet, element_type: str, name: str, exact_match: Literal[True] = True) -> int: ...
@overload
def get_element_index(net: pandapowerNet, element_type: str, name: str, exact_match: Literal[False]) -> pd.Index[int]: ...
@overload
def get_element_index(net: pandapowerNet, element_type: str, name: str, exact_match: bool = True) -> int | pd.Index[int]: ...
@overload
def get_element_indices(
    net: pandapowerNet, element_type: str | Iterable[str], name: str | Iterable[str], exact_match: Literal[True] = True
) -> list[int]: ...
@overload
def get_element_indices(
    net: pandapowerNet, element_type: str | Iterable[str], name: str | Iterable[str], exact_match: Literal[False]
) -> list[pd.Index[int]]: ...
@overload
def get_element_indices(
    net: pandapowerNet, element_type: str | Iterable[str], name: str | Iterable[str], exact_match: bool = True
) -> list[int | pd.Index[int]]: ...
def next_bus(net: pandapowerNet, bus: int, element_id: int, et: str = "line", **kwargs: Incomplete) -> int: ...
def get_connected_elements(
    net: pandapowerNet,
    element_type: str,
    buses: int | Iterable[int],
    respect_switches: bool = True,
    respect_in_service: bool = False,
) -> set[int]: ...
def get_connected_buses(
    net: pandapowerNet,
    buses: int | Iterable[int],
    consider: Iterable[str] = ("l", "s", "t", "t3", "i"),
    respect_switches: bool = True,
    respect_in_service: bool = False,
) -> set[int]: ...
def get_connected_buses_at_element(
    net: pandapowerNet, element_index: int, element_type: str, respect_in_service: bool = False
) -> set[int]: ...
def get_connected_buses_at_switches(net: pandapowerNet, switches: int | Iterable[int]) -> set[int]: ...
def get_connected_switches(
    net: pandapowerNet,
    buses: int | Iterable[int],
    consider: Iterable[str] = ("b", "l", "t", "t3", "i"),
    status: Literal["all", "closed", "open"] = "all",
    include_element_connections: bool = False,
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
def get_connecting_branches(
    net: pandapowerNet, buses1: Iterable[int], buses2: Iterable[int], branch_elements: Iterable[str] | None = None
) -> dict[str, pd.Index[int]]: ...
def get_gc_objects_dict() -> dict[type[Any], int]: ...
def false_elm_links(
    net: pandapowerNet, element_type: str, col: str, target_element_type: str | Iterable[str]
) -> pd.Index[int]: ...
def false_elm_links_loop(net: pandapowerNet, element_types: Iterable[str] | None = None) -> dict[str, pd.Index[int]]: ...
def pp_elements(
    bus: bool = True,
    bus_elements: bool = True,
    branch_elements: bool = True,
    other_elements: bool = True,
    cost_tables: bool = False,
    res_elements: bool = False,
) -> set[str]: ...
def branch_element_bus_dict(include_switch: bool = False, sort: None = None) -> dict[str, list[str]]: ...
def element_bus_tuples(
    bus_elements: bool = True, branch_elements: bool = True, res_elements: bool = False
) -> set[tuple[str, str]]: ...
def count_elements(net, return_empties=False, **kwargs): ...
