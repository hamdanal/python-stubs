from typing_extensions import Self

from shapely._typing import GeoArrayLike
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry

class GeometryCollection(BaseMultipartGeometry):
    def __new__(self, geoms: BaseGeometry | BaseMultipartGeometry | GeoArrayLike | None = None) -> Self: ...
