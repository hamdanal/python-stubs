from pandapower.grid_equivalents.auxiliary import drop_internal_branch_elements as drop_internal_branch_elements

def getFromDict(dict_, keys): ...
def setInDict(dict_, keys, value) -> None: ...
def appendSetInDict(dict_, keys, set_) -> None: ...
def setSetInDict(dict_, keys, set_) -> None: ...
def append_set_to_dict(dict_, set_, keys) -> None: ...
def set_bus_zone_by_boundary_branches(net, all_boundary_branches) -> None: ...
def get_boundaries_by_bus_zone_with_boundary_branches(net): ...
def get_connected_switch_buses_groups(net, buses): ...
