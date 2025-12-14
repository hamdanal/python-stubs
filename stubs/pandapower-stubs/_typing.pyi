from collections.abc import Collection, Iterable, Mapping, MutableMapping
from typing import Any, Protocol, SupportsFloat, SupportsIndex, TypedDict, type_check_only

import numpy as np

# Wide primitives for input types
type Bool = bool | np.bool
type Int = SupportsIndex
type Float = SupportsFloat | Int

# Vector-related
type ScalarOrVector[T] = T | Collection[T]
type Array1D[G: np.generic] = np.ndarray[tuple[int], np.dtype[G]]
type Array2D[G: np.generic] = np.ndarray[tuple[int, int], np.dtype[G]]

class SupportsArray[G: np.generic](Protocol):
    def __array__(self) -> np.ndarray[Any, np.dtype[G]]: ...

type VectorLike[T, G: np.generic] = Collection[T] | SupportsArray[G]
type FloatVectorLike = VectorLike[Float, np.floating | np.integer | np.bool]

# File I/O related
@type_check_only
class FromJsonKwds(TypedDict, total=False):  # keep inline with pandapower.file_io functions
    convert: bool
    encryption_key: str | None
    elements_to_deserialize: Iterable[str] | None
    keep_serialized_elements: bool
    add_basic_std_types: bool
    replace_elements: Mapping[str, str] | None
    empty_dict_like_object: MutableMapping[str, Any] | None

@type_check_only
class SupportsToWkt(Protocol):
    def to_wkt(self) -> str: ...

@type_check_only
class SupportsGeoInterface(Protocol):
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...  # values are arbitrary

type ConvertibleToCRS = str | int | tuple[str, str] | list[str] | dict[str, Any] | SupportsToWkt

from pandapower.auxiliary import pandapowerNet  # noqa: E402

class RunPPFunc(Protocol):
    def __call__(self, net: pandapowerNet, *, calculate_voltage_angles: bool, **kwargs) -> object: ...
