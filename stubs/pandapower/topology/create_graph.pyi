from _typeshed import Incomplete

graph_tool_available: bool
INDEX: int
F_BUS: int
T_BUS: int
WEIGHT: int
BR_R: int
BR_X: int
BR_Z: int

def create_nxgraph(
    net,
    respect_switches: bool = ...,
    include_lines: bool = ...,
    include_impedances: bool = ...,
    include_dclines: bool = ...,
    include_trafos: bool = ...,
    include_trafo3ws: bool = ...,
    nogobuses: Incomplete | None = ...,
    notravbuses: Incomplete | None = ...,
    multi: bool = ...,
    calc_branch_impedances: bool = ...,
    branch_impedance_unit: str = ...,
    library: str = ...,
    include_out_of_service: bool = ...,
): ...
def get_edge_table(net, table_name, include_edges): ...
def add_edges(
    mg, indices, parameter, in_service, net, element, calc_branch_impedances: bool = ..., branch_impedance_unit: str = ...
) -> None: ...
def get_baseR(net, ppc, buses): ...
def init_par(tab, calc_branch_impedances: bool = ...): ...
def get_nx_ppc(net): ...
