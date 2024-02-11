from typing_extensions import Self

from shapely._typing import OptGeoArrayLike
from shapely.geometry.base import BaseMultipartGeometry, GeometrySequence

# TODO: make generic with typevar default = BaseGeometry
class GeometryCollection(BaseMultipartGeometry):
    def __new__(
        self, geoms: BaseMultipartGeometry | GeometrySequence[BaseMultipartGeometry] | OptGeoArrayLike = None
    ) -> Self: ...
    # more precise base overrides
    @property
    def boundary(self) -> None: ...
