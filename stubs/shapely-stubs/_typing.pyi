import sys
from collections.abc import Sequence
from typing import Any, Protocol, TypeVar, type_check_only
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from shapely.geometry.base import BaseGeometry

_T = TypeVar("_T")
_DType = TypeVar("_DType", bound=np.dtype[Any])
_DType_co = TypeVar("_DType_co", covariant=True, bound=np.dtype[Any])

GeoT = TypeVar("GeoT", bound=BaseGeometry)  # noqa: PYI001

@type_check_only
class SupportsArray(Protocol[_DType_co]):
    def __array__(self) -> np.ndarray[Any, _DType_co]: ...

# TODO revisit when mypy is happy with recursive type alias
# NestedSequence: TypeAlias = Sequence[_T] | Sequence[NestedSequence[_T]]
NestedSequence: TypeAlias = Sequence[_T] | Sequence[Sequence[_T]] | Sequence[Sequence[Sequence[_T]]]
DualArrayLike: TypeAlias = SupportsArray[_DType] | NestedSequence[SupportsArray[_DType]] | NestedSequence[_T]

if sys.version_info >= (3, 12):
    from collections.abc import Buffer

    ArrayLikeSeq: TypeAlias = Buffer | DualArrayLike[np.dtype[Any], _T]
    GeoArrayLikeSeq: TypeAlias = Buffer | DualArrayLike[np.dtype[Any], BaseGeometry]
    OptGeoArrayLikeSeq: TypeAlias = Buffer | DualArrayLike[np.dtype[Any], BaseGeometry | None]
else:
    ArrayLikeSeq: TypeAlias = DualArrayLike[np.dtype[Any], _T]
    GeoArrayLikeSeq: TypeAlias = DualArrayLike[np.dtype[Any], BaseGeometry]
    OptGeoArrayLikeSeq: TypeAlias = DualArrayLike[np.dtype[Any], BaseGeometry | None]
ArrayLike: TypeAlias = _T | ArrayLikeSeq[_T]
GeoArrayLike: TypeAlias = BaseGeometry | GeoArrayLikeSeq
OptGeoArrayLike: TypeAlias = BaseGeometry | None | OptGeoArrayLikeSeq
GeoArray: TypeAlias = NDArray[np.object_]  # array of `BaseGeometry`

@type_check_only
class SupportsGeoInterface(Protocol):
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...
