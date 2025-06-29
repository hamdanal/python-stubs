from _typeshed import Incomplete
from collections.abc import Collection, Iterable, Mapping
from typing import Any, Final, Literal, overload

import networkx as nx
import numpy as np
import pandas as pd
from numpy.typing import NDArray

from pandapower.auxiliary import pandapowerNet
from pandapower.topology.graph_tool_interface import GraphToolInterface

graph_tool_available: bool

INDEX: Final = 0
F_BUS: Final = 1
T_BUS: Final = 2
WEIGHT: Final = 0
BR_R: Final = 1
BR_X: Final = 2
BR_Z: Final = 3

@overload  # multi=False positional
def create_nxgraph(
    net: pandapowerNet,
    respect_switches: bool,
    include_lines: bool,
    include_impedances: bool,
    include_dclines: bool,
    include_trafos: bool,
    include_trafo3ws: bool,
    include_tcsc: bool,
    include_vsc: bool,
    include_line_dc: bool,
    nogobuses: Iterable[int] | None,
    notravbuses: Iterable[int] | None,
    multi: Literal[False],
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    library: Literal["networkx"] = "networkx",
    include_out_of_service: bool = False,
    include_switches: bool = True,
    trafo_length_km: float | None = None,
    switch_length_km: float | None = None,
) -> nx.Graph[Incomplete]: ...
@overload  # multi=False keyword
def create_nxgraph(
    net: pandapowerNet,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_impedances: bool = True,
    include_dclines: bool = True,
    include_trafos: bool = True,
    include_trafo3ws: bool = True,
    include_tcsc: bool = True,
    include_vsc: bool = True,
    include_line_dc: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    *,
    multi: Literal[False],
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    library: Literal["networkx"] = "networkx",
    include_out_of_service: bool = False,
    include_switches: bool = True,
    trafo_length_km: float | None = None,
    switch_length_km: float | None = None,
) -> nx.Graph[Incomplete]: ...
@overload  # library="graph_tool" positional
def create_nxgraph(
    net: pandapowerNet,
    respect_switches: bool,
    include_lines: bool,
    include_impedances: bool,
    include_dclines: bool,
    include_trafos: bool,
    include_trafo3ws: bool,
    include_tcsc: bool,
    include_vsc: bool,
    include_line_dc: bool,
    nogobuses: Iterable[int] | None,
    notravbuses: Iterable[int] | None,
    multi: Literal[True],
    calc_branch_impedances: bool,
    branch_impedance_unit: Literal["ohm", "pu"],
    library: Literal["graph_tool"],
    include_out_of_service: bool = False,
    include_switches: bool = True,
    trafo_length_km: float | None = None,
    switch_length_km: float | None = None,
) -> GraphToolInterface: ...
@overload  # library="graph_tool" keyword
def create_nxgraph(
    net: pandapowerNet,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_impedances: bool = True,
    include_dclines: bool = True,
    include_trafos: bool = True,
    include_trafo3ws: bool = True,
    include_tcsc: bool = True,
    include_vsc: bool = True,
    include_line_dc: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    multi: Literal[True] = True,
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    *,
    library: Literal["graph_tool"],
    include_out_of_service: bool = False,
    include_switches: bool = True,
    trafo_length_km: float | None = None,
    switch_length_km: float | None = None,
) -> GraphToolInterface: ...
@overload
def create_nxgraph(
    net: pandapowerNet,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_impedances: bool = True,
    include_dclines: bool = True,
    include_trafos: bool = True,
    include_trafo3ws: bool = True,
    include_tcsc: bool = True,
    include_vsc: bool = True,
    include_line_dc: bool = True,
    nogobuses: Iterable[int] | None = None,
    notravbuses: Iterable[int] | None = None,
    multi: Literal[True] = True,
    calc_branch_impedances: bool = False,
    branch_impedance_unit: Literal["ohm", "pu"] = "ohm",
    library: Literal["networkx"] = "networkx",
    include_out_of_service: bool = False,
    include_switches: bool = True,
    trafo_length_km: float | None = None,
    switch_length_km: float | None = None,
) -> nx.MultiGraph[Incomplete]: ...
def get_edge_table(net: pandapowerNet, table_name: str, include_edges: bool | Collection[int]) -> pd.DataFrame | None: ...
def add_edges(
    mg: nx.Graph[Incomplete] | GraphToolInterface,
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
def init_par(
    tab: pd.DataFrame, calc_branch_impedances: bool = False, include_out_of_service: bool = False
) -> tuple[NDArray[Any], ...]: ...
def get_nx_ppc(net: pandapowerNet) -> dict[str, Any]: ...
