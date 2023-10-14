from collections.abc import Collection, Container, Generator, Iterable, Set as AbstractSet
from typing import Literal, TypedDict
from typing_extensions import TypeAlias

import networkx as nx
import pandas as pd
from pandapower.auxiliary import pandapowerNet

_GraphCharKey: TypeAlias = Literal["connected", "articulation_points", "bridges", "stub_buses", "required_bridges", "notn1_areas"]

class _GraphCharDict(TypedDict, total=False):
    connected: set[int]
    articulation_points: set[int]
    bridges: set[tuple[int, int]]
    stub_buses: set[int]
    required_bridges: dict[int, list[tuple[int, int]]]
    notn1_areas: dict[int, set[int]]

class _BasicGraphCharDict(TypedDict, total=False):
    connected: set[int]
    stub_buses: set[int]
    bridges: set[tuple[int, int]]
    articulation_points: set[int]
    notn1_starts: set[int]

def connected_component(mg: nx.Graph, bus: int, notravbuses: Container[int] = []) -> Generator[int, None, None]: ...
def connected_components(mg: nx.Graph, notravbuses: AbstractSet[int] = ...) -> Generator[set[int], None, None]: ...
def calc_distance_to_bus(
    net: pandapowerNet,
    bus: int,
    respect_switches: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    weight: str | None = "weight",
) -> pd.Series[float]: ...
def unsupplied_buses(
    net: pandapowerNet, mg: nx.Graph | None = None, slacks: AbstractSet[int] | None = None, respect_switches: bool = True
) -> set[int]: ...
def find_basic_graph_characteristics(
    g: nx.Graph, roots: Iterable[int], characteristics: Collection[_GraphCharKey]
) -> _BasicGraphCharDict: ...
def find_graph_characteristics(
    g: nx.Graph, roots: Iterable[int], characteristics: Collection[_GraphCharKey]
) -> _GraphCharDict: ...
def get_2connected_buses(g: nx.Graph, roots: Iterable[int]) -> tuple[set[int], set[int]]: ...
def determine_stubs(
    net: pandapowerNet, roots: Iterable[int] | None = None, mg: nx.Graph | None = None, respect_switches: bool = False
) -> set[int]: ...
def lines_on_path(mg: nx.Graph, path: Iterable[int]) -> list[int]: ...
def elements_on_path(
    mg: nx.Graph, path: Iterable[int], element: Literal["line", "switch", "trafo", "trafo3w"] = "line"
) -> list[int]: ...
def get_end_points_of_continuously_connected_lines(net: pandapowerNet, lines: slice | Iterable[int]) -> tuple[int, int]: ...
