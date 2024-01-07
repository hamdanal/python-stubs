from collections.abc import Collection
from typing_extensions import Self

from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.point import _PointLike

__all__ = ["MultiPoint"]

class MultiPoint(BaseMultipartGeometry):
    # Note on "points" type in `__new__`:
    # * `Collection` here is loose as the expected type should support "__getitem__".
    # * `Sequence` is more correct but it will lead to False positives with common types
    #   like np.ndarray, pd.Index, pd.Series, ...
    # I went with Collection as false negatives seem better to me than false positives in this case
    def __new__(self, points: MultiPoint | Collection[_PointLike] | None = None) -> Self: ...
    def svg(self, scale_factor: float = 1.0, fill_color: str | None = None, opacity: float | None = None) -> str: ...  # type: ignore[override]
