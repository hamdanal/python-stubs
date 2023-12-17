from collections.abc import Collection
from typing_extensions import Self

from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.linestring import _ConvertibleToLineString
from shapely.geometry.polygon import Polygon

__all__ = ["MultiPolygon"]

class MultiPolygon(BaseMultipartGeometry):
    def __new__(
        self,
        polygons: (
            MultiPolygon
            | BaseMultipartGeometry
            | Collection[
                Polygon  # polygon
                | tuple[_ConvertibleToLineString]  # polygon shell
                | tuple[_ConvertibleToLineString, Collection[_ConvertibleToLineString | None]]  # polygon shell and holes
            ]
            | None
        ) = None,
    ) -> Self: ...
    def svg(self, scale_factor: float = 1.0, fill_color: str | None = None, opacity: float | None = None) -> str: ...
