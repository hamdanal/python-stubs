from collections.abc import Collection
from typing_extensions import Self

from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.linestring import LineString, _ConvertibleToLineString
from shapely.geometry.multipoint import MultiPoint

__all__ = ["MultiLineString"]

class MultiLineString(BaseMultipartGeometry[LineString]):
    def __new__(self, lines: BaseMultipartGeometry | Collection[_ConvertibleToLineString] | None = None) -> Self: ...
    def svg(self, scale_factor: float = 1.0, stroke_color: str | None = None, opacity: float | None = None) -> str: ...  # type: ignore[override]
    # more precise base overrides
    @property
    def boundary(self) -> MultiPoint: ...
