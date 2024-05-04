from collections.abc import Collection
from typing_extensions import Self, overload

from shapely._typing import OptGeoArrayLike
from shapely.geometry.base import BaseMultipartGeometry, GeometrySequence, _GeoT

class GeometryCollection(BaseMultipartGeometry[_GeoT]):
    # Overloads of __new__ are used because mypy is unable to narrow the typevar otherwise
    @overload
    def __new__(
        self, geoms: BaseMultipartGeometry[_GeoT] | GeometrySequence[BaseMultipartGeometry[_GeoT]] | Collection[_GeoT]
    ) -> Self: ...
    @overload
    def __new__(self, geoms: OptGeoArrayLike = None) -> Self: ...
    # more precise base overrides
    @property
    def boundary(self) -> None: ...
