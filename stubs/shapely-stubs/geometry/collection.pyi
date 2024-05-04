from collections.abc import Collection
from typing_extensions import Self, overload

from shapely._typing import OptGeoArrayLike
from shapely.geometry.base import BaseMultipartGeometry, GeometrySequence, _GeoT_co

class GeometryCollection(BaseMultipartGeometry[_GeoT_co]):
    # Overloads of __new__ are used because mypy is unable to narrow the typevar otherwise
    @overload
    def __new__(
        self, geoms: BaseMultipartGeometry[_GeoT_co] | GeometrySequence[BaseMultipartGeometry[_GeoT_co]] | Collection[_GeoT_co]
    ) -> Self: ...
    @overload
    def __new__(self, geoms: OptGeoArrayLike = None) -> Self: ...
    # more precise base overrides
    @property
    def boundary(self) -> None: ...
