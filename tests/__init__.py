from __future__ import annotations

from collections.abc import Iterable
from types import GenericAlias, UnionType
from typing import Any, cast

import numpy as np
from shapely.geometry.base import BaseMultipartGeometry, GeometrySequence

type _ClassInfo = type | UnionType | tuple["_ClassInfo", ...]  # see isinstance

# Make stubs generic classes generic at runtime
setattr(BaseMultipartGeometry, "__class_getitem__", classmethod(GenericAlias))
setattr(GeometrySequence, "__class_getitem__", classmethod(GenericAlias))


def check[T](obj: T, cls: _ClassInfo, dtype: _ClassInfo | None = None) -> T:
    __tracebackhide__ = True
    if not isinstance(obj, cls):
        raise RuntimeError(f"Expected type '{cls}' but got '{type(obj)}'")
    if dtype is None:
        return obj

    value: Any
    if isinstance(obj, np.ndarray):
        value = np.asarray(obj).flatten()[0]  # pyright: ignore[reportUnknownArgumentType]
    elif hasattr(obj, "__iter__"):
        value = next(iter(cast(Iterable[Any], obj)))
    else:
        value = obj

    if not isinstance(value, dtype):
        raise RuntimeError(f"Expected type '{dtype}' but got '{type(value)}'")
    return obj


class HasArray:
    def __init__(self, array: np.ndarray[Any, Any]) -> None:
        self.array = array

    def __array__(self) -> np.ndarray[Any, Any]:
        return self.array
