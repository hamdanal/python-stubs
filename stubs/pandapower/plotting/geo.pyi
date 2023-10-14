from typing import TypeVar

from pandapower.auxiliary import pandapowerNet

_N = TypeVar("_N", bound=pandapowerNet)

shapely_INSTALLED: bool
geopandas_INSTALLED: bool
pyproj_INSTALLED: bool

def convert_gis_to_geodata(net: pandapowerNet, node_geodata: bool = True, branch_geodata: bool = True) -> None: ...
def convert_geodata_to_gis(
    net: pandapowerNet, epsg: int = 31467, node_geodata: bool = True, branch_geodata: bool = True
) -> None: ...
def convert_epsg_bus_geodata(net: _N, epsg_in: int = 4326, epsg_out: int = 31467) -> _N: ...
