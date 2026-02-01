from _typeshed import Incomplete
from collections.abc import Collection

import geojson  # type: ignore[import-untyped] # https://github.com/jazzband/geojson/pull/203

from pandapower._typing import ConvertibleToCRS, Int
from pandapower.auxiliary import ADict, pandapowerNet

def abstract_convert_crs(
    net: ADict[Incomplete], epsg_in: int = 4326, epsg_out: int = 31467, component_name: str = "bus"
) -> None: ...
def convert_crs(net: pandapowerNet, epsg_in: ConvertibleToCRS = 4326, epsg_out: ConvertibleToCRS = 31467) -> None: ...
def dump_to_geojson_node_branch(
    net: ADict[Incomplete],
    node_name: str = "bus",
    branch_name: str = "line",
    nodes: bool | Collection[Int] = False,
    branches: bool | Collection[Int] = False,
    include_type_id: bool = True,
) -> tuple[list[geojson.Feature], int, int]: ...
def dump_to_geojson(
    net: pandapowerNet,
    buses: bool | Collection[Int] = False,
    lines: bool | Collection[Int] = False,
    switches: bool | Collection[Int] = False,
    trafos: bool | Collection[Int] = False,
    t_is_3w: bool = False,
    include_type_id: bool = True,
) -> geojson.FeatureCollection: ...
def abstract_convert_geodata_to_geojson(
    net: ADict[Incomplete],
    node_name: str = "bus",
    branch_name: str = "line",
    delete: bool = True,
    lonlat: bool = False,
    drop_invalid_geodata: bool = True,
) -> None: ...
def convert_geodata_to_geojson(
    net: pandapowerNet, delete: bool = True, lonlat: bool = False, drop_invalid_geodata: bool = True
) -> None: ...
def abstract_convert_gis_to_geojson(
    net: ADict[Incomplete], node_name: str = "bus", branch_name: str = "line", delete: bool = True
) -> None: ...
def convert_gis_to_geojson(net: pandapowerNet, delete: bool = True) -> None: ...
