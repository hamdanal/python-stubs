from _typeshed import Incomplete
from collections.abc import Iterable

from pandas._typing import Axes

from pandapower.auxiliary import pandapowerNet

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
    element_type: str,
    new_indices: Axes | None = None,
    old_indices: Axes | None = None,
    lookup: dict[int, int] | None = None,
) -> None: ...
def create_continuous_elements_index(net: pandapowerNet, start: int = 0, add_df_to_reindex: Iterable[str] = ...) -> None: ...
def set_scaling_by_type(
    net: pandapowerNet, scalings: dict[str, float], scale_load: bool = True, scale_sgen: bool = True
) -> None: ...
def set_data_type_of_columns_to_default(net: pandapowerNet) -> None: ...
