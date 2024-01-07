from typing_extensions import Self

from shapely._typing import OptGeoArrayLike
from shapely.geometry.base import BaseMultipartGeometry

class GeometryCollection(BaseMultipartGeometry):
    def __new__(self, geoms: BaseMultipartGeometry | OptGeoArrayLike = None) -> Self: ...
