from collections.abc import Collection
from typing_extensions import deprecated

import geojson  # type: ignore[import-untyped] # https://github.com/jazzband/geojson/pull/203

from pandapower._typing import ConvertibleToCRS, Int
from pandapower.auxiliary import pandapowerNet

@deprecated("Use convert_gis_to_geojson instead. Support for geodata will be dropped.")
def convert_gis_to_geodata(net: pandapowerNet, node_geodata: bool = True, branch_geodata: bool = True) -> None: ...
@deprecated("Use convert_geodata_to_geojson instead. Support for gis will be dropped.")
def convert_geodata_to_gis(
    net: pandapowerNet, epsg: int = 31467, node_geodata: bool = True, branch_geodata: bool = True, remove_xy: bool = False
) -> None: ...
@deprecated("Use convert_crs instead. Networks should not use different crs for bus and line geodata.")
def convert_epsg_bus_geodata(net: pandapowerNet, epsg_in: int = 4326, epsg_out: int = 31467) -> pandapowerNet: ...
def convert_crs(net: pandapowerNet, epsg_in: ConvertibleToCRS = 4326, epsg_out: ConvertibleToCRS = 31467) -> None: ...
def dump_to_geojson(
    net: pandapowerNet,
    nodes: bool | Collection[Int] = False,
    branches: bool | Collection[Int] = False,
    switches: bool | Collection[Int] = False,
    trafos: bool | Collection[Int] = False,
    t_is_3w: bool = False,
    include_type_id: bool = True,
) -> geojson.FeatureCollection: ...
def convert_geodata_to_geojson(net: pandapowerNet, delete: bool = True, lonlat: bool = False) -> None: ...
def convert_gis_to_geojson(net: pandapowerNet, delete: bool = True) -> None: ...
