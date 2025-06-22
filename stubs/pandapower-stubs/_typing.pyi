from collections.abc import Collection, Iterable, Mapping, MutableMapping
from typing import Any, Protocol, SupportsFloat, SupportsIndex, TypedDict, TypeVar, type_check_only
from typing_extensions import TypeAlias

import numpy as np

_T = TypeVar("_T", bound=Any)

# Wide primitives for input types
Bool: TypeAlias = bool | np.bool
Int: TypeAlias = SupportsIndex
Float: TypeAlias = SupportsFloat | Int

# Vector-related
ScalarOrVector: TypeAlias = _T | Collection[_T]
Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_T]]
Array2D: TypeAlias = np.ndarray[tuple[int, int], np.dtype[_T]]

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
