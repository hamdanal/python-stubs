from abc import ABCMeta, abstractmethod
from typing import Any, Literal, overload
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from . import array as array, geoseries as geoseries

_RTreeIndex: TypeAlias = type[Any]

class BaseSpatialIndex(metaclass=ABCMeta):
    @property
    @abstractmethod
    def valid_query_predicates(self) -> set[str | None]: ...
    @abstractmethod
    def query(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    def query_bulk(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...  # deprecated
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
    @abstractmethod
    def size(self) -> int: ...
    @property
    @abstractmethod
    def is_empty(self) -> bool: ...

class RTreeIndex(_RTreeIndex):  # type: ignore[misc]
    geometries: NDArray[np.object_]
    def __init__(self, geometry: NDArray[np.object_]) -> None: ...
    @property
    def valid_query_predicates(self) -> set[str | None]: ...
    def query(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    def query_bulk(self, geometry, predicate: str | None = None, sort: bool = False) -> NDArray[np.int_]: ...
    def nearest(self, coordinates, num_results: int = 1, objects: bool | str = False): ...
    def intersection(self, coordinates) -> NDArray[np.int_]: ...
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
