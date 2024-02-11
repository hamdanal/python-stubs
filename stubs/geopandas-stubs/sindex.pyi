from collections.abc import Iterator
from typing import Any, Literal, overload
from typing_extensions import deprecated

import numpy as np
import rtree.index
from numpy.typing import NDArray

class BaseSpatialIndex:
    @property
    def valid_query_predicates(self) -> set[str | None]: ...
    def query(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    @deprecated("Method `query_bulk()` is deprecated. Use method `query()` instead.")
    def query_bulk(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        return_distance: bool = False,
        exclusive: bool = False,
    ) -> NDArray[np.int_] | tuple[NDArray[np.int_], NDArray[np.float_]]: ...
    def intersection(self, coordinates) -> NDArray[np.int_]: ...
    @property
    def size(self) -> int: ...
    @property
    def is_empty(self) -> bool: ...

@deprecated("class `SpatialIndex` is deprecated. Use `GeoSeries.sindex` or `rtree.index.Index` instead.")
class SpatialIndex(rtree.index.Index, BaseSpatialIndex):
    def __init__(self, *args: Any) -> None: ...
    def intersection(self, coordinates: Any, *args: Any, **kwargs: Any) -> Iterator[Any]: ...  # type: ignore[override]
    def nearest(self, *args: Any, **kwargs: Any) -> Iterator[Any]: ...  # type: ignore[override]
    @property
    def size(self) -> int: ...
    @property
    def is_empty(self) -> bool: ...

class RTreeIndex(rtree.index.Index):
    geometries: NDArray[np.object_]
    def __init__(self, geometry: NDArray[np.object_]) -> None: ...
    @property
    def valid_query_predicates(self) -> set[str | None]: ...
    def query(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    @deprecated("Method `query_bulk()` is deprecated. Use method `query()` instead.")
    def query_bulk(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    @deprecated("`sindex.nearest` using the rtree backend is deprecated. See `PyGEOSSTRTreeIndex.nearest` for details.")
    def nearest(self, coordinates, num_results: int = 1, objects: bool | Literal["raw"] = False) -> Iterator[Any]: ...
    def intersection(self, coordinates) -> Iterator[int]: ...  # type: ignore[override]
    @property
    def size(self) -> int: ...
    @property
    def is_empty(self) -> bool: ...
    def __len__(self) -> int: ...

class PyGEOSSTRTreeIndex(BaseSpatialIndex):
    geometries: NDArray[np.object_]
    def __init__(self, geometry: NDArray[np.object_]) -> None: ...
    @property
    def valid_query_predicates(self) -> set[str | None]: ...
    def query(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    @deprecated("Method `query_bulk()` is deprecated. Use method `query()` instead.")
    def query_bulk(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    @overload
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        return_distance: Literal[False] = False,
        exclusive: bool = False,
    ) -> NDArray[np.int_]: ...
    @overload
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        *,
        return_distance: Literal[True],
        exclusive: bool = False,
    ) -> tuple[NDArray[np.int_], NDArray[np.float_]]: ...
    @overload
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        return_distance: bool = False,
        exclusive: bool = False,
    ) -> NDArray[np.int_] | tuple[NDArray[np.int_], NDArray[np.float_]]: ...
    def intersection(self, coordinates) -> NDArray[np.int_]: ...
    @property
    def size(self) -> int: ...
    @property
    def is_empty(self) -> bool: ...
    def __len__(self) -> int: ...
