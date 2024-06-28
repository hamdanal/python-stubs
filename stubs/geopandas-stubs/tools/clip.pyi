from typing import TypeVar
from typing_extensions import TypeAlias

from shapely import MultiPolygon, Polygon

from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

_G = TypeVar("_G", GeoDataFrame, GeoSeries)
_Mask: TypeAlias = GeoDataFrame | GeoSeries | Polygon | MultiPolygon | tuple[float, float, float, float]

def clip(gdf: _G, mask: _Mask, keep_geom_type: bool = False, sort: bool = False) -> _G: ...
