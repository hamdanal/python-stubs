from collections.abc import Collection, Iterable, Mapping, MutableMapping
from typing import Any, Protocol, SupportsFloat, SupportsIndex, TypedDict, TypeVar, type_check_only
from typing_extensions import TypeAlias

import numpy as np

_T = TypeVar("_T")
_G = TypeVar("_G", bound=np.generic)
_Generic_co = TypeVar("_Generic_co", covariant=True, bound=np.generic)

# Wide primitives for input types
Bool: TypeAlias = bool | np.bool
Int: TypeAlias = SupportsIndex
Float: TypeAlias = SupportsFloat | Int

# Vector-related
ScalarOrVector: TypeAlias = _T | Collection[_T]
Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_G]]
Array2D: TypeAlias = np.ndarray[tuple[int, int], np.dtype[_G]]

class SupportsArray(Protocol[_Generic_co]):
    def __array__(self) -> np.ndarray[Any, np.dtype[_Generic_co]]: ...

VectorLike: TypeAlias = Collection[_T] | SupportsArray[_G]
FloatVectorLike: TypeAlias = VectorLike[Float, np.floating | np.integer | np.bool]

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

ConvertibleToCRS: TypeAlias = str | int | tuple[str, str] | list[str] | dict[str, Any] | SupportsToWkt

from pandapower.auxiliary import pandapowerNet  # noqa: E402

class RunPPFunc(Protocol):
    def __call__(self, net: pandapowerNet, *, calculate_voltage_angles: bool, **kwargs) -> object: ...
