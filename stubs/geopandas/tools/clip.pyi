from typing import TypeVar

from shapely import MultiPolygon, Polygon

from ..geodataframe import GeoDataFrame
from ..geoseries import GeoSeries

_G = TypeVar("_G", GeoDataFrame, GeoSeries)

def clip(
    gdf: _G,
    mask: GeoDataFrame | GeoSeries | Polygon | MultiPolygon | tuple[float, float, float, float],
    keep_geom_type: bool = False,
) -> _G: ...
