from collections.abc import Iterable, Sequence
from typing import Any
from typing_extensions import TypeAlias

import networkx as nx
from numpy.typing import ArrayLike
from pandapower.auxiliary import pandapowerNet

IGRAPH_INSTALLED: bool
IGraph: TypeAlias = Any  # igraph.Graph but igraph is not installed

def build_igraph_from_pp(
    net: pandapowerNet, respect_switches: bool = False, buses: Sequence[int] | ArrayLike | None = None
) -> tuple[IGraph, bool, list[int]]: ...
def coords_from_igraph(
    graph: IGraph, roots: Iterable[int], meshed: bool = False, calculate_meshed: bool = False
) -> list[tuple[float, float]]: ...
def coords_from_nxgraph(mg: nx.Graph | None = None) -> list[tuple[float, float]]: ...
def create_generic_coordinates(
    net: pandapowerNet,
    mg: nx.Graph | None = None,
    library: str = "igraph",
    respect_switches: bool = False,
    geodata_table: str = "bus_geodata",
    buses: Sequence[int] | ArrayLike | None = None,
    overwrite: bool = False,
) -> pandapowerNet: ...
def fuse_geodata(net: pandapowerNet) -> None: ...
