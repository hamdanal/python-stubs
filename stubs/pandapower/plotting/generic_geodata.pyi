from _typeshed import Incomplete

IGRAPH_INSTALLED: bool

def build_igraph_from_pp(net, respect_switches: bool = ..., buses: Incomplete | None = ...): ...
def coords_from_igraph(graph, roots, meshed: bool = ..., calculate_meshed: bool = ...): ...
def coords_from_nxgraph(mg: Incomplete | None = ...): ...
def create_generic_coordinates(
    net,
    mg: Incomplete | None = ...,
    library: str = ...,
    respect_switches: bool = ...,
    geodata_table: str = ...,
    buses: Incomplete | None = ...,
    overwrite: bool = ...,
): ...
def fuse_geodata(net) -> None: ...
