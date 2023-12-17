from typing import Any

from shapely._typing import SupportsGeoInterface
from shapely.geometry.base import BaseGeometry
from shapely.geometry.polygon import Polygon

def box(minx: float, miny: float, maxx: float, maxy: float, ccw: bool = True) -> Polygon: ...
def shape(context: dict[str, Any] | SupportsGeoInterface) -> BaseGeometry: ...
def mapping(ob: SupportsGeoInterface) -> dict[str, Any]: ...
