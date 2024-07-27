from typing import TypeVar

from geopandas.base import _ClipMask
from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

_G = TypeVar("_G", GeoDataFrame, GeoSeries)

def clip(gdf: _G, mask: _ClipMask, keep_geom_type: bool = False, sort: bool = False) -> _G: ...
