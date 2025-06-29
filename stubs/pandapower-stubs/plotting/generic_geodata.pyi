from _typeshed import Incomplete
from collections.abc import Iterable
from typing import (
    Any as IGraph,  # igraph.Graph but igraph is not installed
    Literal,
)

import networkx as nx
from numpy.typing import ArrayLike

from pandapower._typing import Float
from pandapower.auxiliary import pandapowerNet

def build_igraph_from_pp(
    net: pandapowerNet,
    respect_switches: bool = False,
    buses: ArrayLike | None = None,
    trafo_length_km: Float = 0.01,
    switch_length_km: Float = 0.001,
    dcline_length_km: Float = 1.0,
) -> tuple[IGraph, bool, list[int]]: ...
def coords_from_igraph(
    graph: IGraph, roots: Iterable[int], meshed: bool = False, calculate_meshed: bool = False
) -> list[tuple[float, float]]: ...
def coords_from_nxgraph(mg: nx.Graph[Incomplete] | None = None, layout_engine: str = "neato") -> list[tuple[float, float]]: ...
def create_generic_coordinates(
    net: pandapowerNet,
    mg: nx.Graph[Incomplete] | None = None,
    library: Literal["igraph", "networkx"] = "igraph",
    respect_switches: bool = False,
    geodata_table: str = "bus",
    buses: ArrayLike | None = None,
    overwrite: bool = False,
    layout_engine: str = "neato",
    trafo_length_km: Float = 0.01,
    switch_length_km: Float = 0.001,
) -> pandapowerNet: ...
def fuse_geodata(net: pandapowerNet) -> None: ...
