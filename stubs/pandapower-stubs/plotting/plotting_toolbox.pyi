from collections.abc import Iterable
from typing import TypeVar, overload

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike, NDArray

from pandapower.auxiliary import pandapowerNet

_T = TypeVar("_T")

def get_collection_sizes(
    net: pandapowerNet,
    bus_size: float = 1.0,
    ext_grid_size: float = 1.0,
    trafo_size: float = 1.0,
    load_size: float = 1.0,
    sgen_size: float = 1.0,
    switch_size: float = 2.0,
    switch_distance: float = 1.0,
    gen_size: float = 1.0,
) -> dict[str, float]: ...
@overload
def get_list(individuals: str, number_entries: int, name_ind: str, name_ent: str) -> list[str]: ...
@overload
def get_list(individuals: _T | Iterable[_T], number_entries: int, name_ind: str, name_ent: str) -> list[_T]: ...
@overload
def get_color_list(
    color: tuple[float, float, float], number_entries: int, name_entries: str = "nodes"
) -> list[tuple[float, float, float]]: ...
@overload
def get_color_list(
    color: tuple[float, float, float, float], number_entries: int, name_entries: str = "nodes"
) -> list[tuple[float, float, float, float]]: ...
@overload
def get_color_list(color: str | Iterable[str], number_entries: int, name_entries: str = "nodes") -> list[str]: ...
def get_angle_list(angle: float | Iterable[float], number_entries: int, name_entries: str = "nodes") -> list[float]: ...
def get_linewidth_list(linewidth: float | Iterable[float], number_entries: int, name_entries: str = "lines") -> list[float]: ...
def get_index_array(indices: set[int] | ArrayLike | None, net_table_indices: pd.Index[int]) -> NDArray[np.int_]: ...
def coords_from_node_geodata(
    element_indices: Iterable[int],
    from_nodes: Iterable[int],
    to_nodes: Iterable[int],
    node_geodata: pd.DataFrame,
    table_name: str,
    node_name: str = "Bus",
    ignore_zero_length: bool = True,
) -> tuple[list[tuple[float, float]], NDArray[np.int_]]: ...
def set_line_geodata_from_bus_geodata(
    net: pandapowerNet, line_index: Iterable[int] | None = None, overwrite: bool = False
) -> None: ...
def position_on_busbar(net: pandapowerNet, bus: int, busbar_coords: NDArray[np.float_]) -> NDArray[np.float_] | None: ...
