from _typeshed import Incomplete
from collections.abc import Generator

def connected_component(mg, bus, notravbuses=...) -> Generator[Incomplete, None, None]: ...
def connected_components(mg, notravbuses=...) -> Generator[Incomplete, None, None]: ...
def calc_distance_to_bus(
    net,
    bus,
    respect_switches: bool = ...,
    nogobuses: Incomplete | None = ...,
    notravbuses: Incomplete | None = ...,
    weight: str = ...,
): ...
def unsupplied_buses(net, mg: Incomplete | None = ..., slacks: Incomplete | None = ..., respect_switches: bool = ...): ...
def find_basic_graph_characteristics(g, roots, characteristics): ...
def find_graph_characteristics(g, roots, characteristics): ...
def get_2connected_buses(g, roots): ...
def determine_stubs(net, roots: Incomplete | None = ..., mg: Incomplete | None = ..., respect_switches: bool = ...): ...
def lines_on_path(mg, path): ...
def elements_on_path(mg, path, element: str = ...): ...
def get_end_points_of_continuously_connected_lines(net, lines): ...
