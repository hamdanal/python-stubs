from collections.abc import Collection, Iterable, Set as AbstractSet
from typing import overload

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike, NDArray

from pandapower._typing import Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def get_collection_sizes(
    net: pandapowerNet,
    bus_size: Float = 1.0,
    ext_grid_size: Float = 1.0,
    trafo_size: Float = 1.0,
    load_size: Float = 1.0,
    sgen_size: Float = 1.0,
    switch_size: Float = 2.0,
    switch_distance: Float = 1.0,
    gen_size: Float = 1.0,
) -> dict[str, float]: ...
@overload
def get_list(individuals: str, number_entries: Int, name_ind: str, name_ent: str) -> list[str]: ...
@overload
def get_list[T](individuals: ScalarOrVector[T], number_entries: Int, name_ind: str, name_ent: str) -> list[T]: ...
@overload
def get_color_list(
    color: tuple[Float, Float, Float], number_entries: Int, name_entries: str = "nodes"
) -> list[tuple[float, float, float]]: ...
@overload
def get_color_list(
    color: tuple[Float, Float, Float, Float], number_entries: Int, name_entries: str = "nodes"
) -> list[tuple[float, float, float, float]]: ...
@overload
def get_color_list(color: str | Iterable[str], number_entries: Int, name_entries: str = "nodes") -> list[str]: ...
def get_angle_list(angle: ScalarOrVector[Float], number_entries: Int, name_entries: str = "nodes") -> list[float]: ...
def get_linewidth_list(linewidth: ScalarOrVector[Float], number_entries: Int, name_entries: str = "lines") -> list[float]: ...
def get_index_array(indices: AbstractSet[Int] | ArrayLike | None, net_table_indices: pd.Index[int]) -> NDArray[np.int_]: ...
def coords_from_node_geodata(
    element_indices: Collection[Int],
    from_nodes: Collection[Int],
    to_nodes: Collection[Int],
    node_geodata: pd.DataFrame,
    table_name: str,
    node_name: str = "Bus",
    ignore_no_geo_diff: Bool = True,
    node_geodata_to: pd.DataFrame | None = None,
) -> tuple[list[tuple[float, float]], NDArray[np.int64]]: ...
def set_line_geodata_from_bus_geodata(
    net: pandapowerNet, line_index: Iterable[Int] | None = None, overwrite: Bool = False, ignore_no_geo_diff: Bool = True
) -> None: ...
def position_on_busbar(net: pandapowerNet, bus: Int, busbar_coords: NDArray[np.float64]) -> NDArray[np.float64] | None: ...
