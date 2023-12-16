from collections.abc import Iterable, Mapping
from typing import Any, Literal, overload

import networkx as nx
import numpy as np
import pandas as pd
from numpy.typing import NDArray

from pandapower.auxiliary import pandapowerNet
from pandapower.topology.graph_tool_interface import GraphToolInterface

graph_tool_available: bool
INDEX: int
F_BUS: int
T_BUS: int
WEIGHT: int
BR_R: int
BR_X: int
BR_Z: int

@overload
def create_nxgraph(
    net: pandapowerNet,
    *,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_impedances: bool = True,
    include_dclines: bool = True,
    include_trafos: bool = True,
    include_trafo3ws: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    multi: Literal[False],
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    library: Literal["networkx"] = "networkx",
    include_out_of_service: bool = False,
) -> nx.Graph: ...
@overload
def create_nxgraph(
    net: pandapowerNet,
    *,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_impedances: bool = True,
    include_dclines: bool = True,
    include_trafos: bool = True,
    include_trafo3ws: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    multi: Literal[True] = True,
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    library: Literal["graph_tool"],
    include_out_of_service: bool = False,
) -> GraphToolInterface: ...
@overload
def create_nxgraph(
    net: pandapowerNet,
    *,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_impedances: bool = True,
    include_dclines: bool = True,
    include_trafos: bool = True,
    include_trafo3ws: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    multi: Literal[True] = True,
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    library: Literal["networkx"] = "networkx",
    include_out_of_service: bool = False,
) -> nx.MultiGraph: ...
def get_edge_table(net: pandapowerNet, table_name: str, include_edges: bool | Iterable[int]) -> pd.DataFrame | None: ...
def add_edges(
    mg: nx.Graph | GraphToolInterface,
    indices,
    parameter,
    in_service,
    net: pandapowerNet,
    element,
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
) -> None: ...
@overload
def get_baseR(net: pandapowerNet, ppc: Mapping[str, Any], buses: int) -> float: ...
@overload
def get_baseR(net: pandapowerNet, ppc: Mapping[str, Any], buses: Iterable[int]) -> NDArray[np.float64]: ...
def init_par(tab: pd.DataFrame, calc_branch_impedances: bool = False) -> tuple[NDArray[Any], ...]: ...
def get_nx_ppc(net: pandapowerNet) -> dict[str, Any]: ...
