from __future__ import annotations

from collections.abc import Iterable
from typing import Any, TypeVar, cast

import numpy as np

T = TypeVar("T")


def check(obj: T, cls: type, dtype: type | None = None) -> T:
    __tracebackhide__ = True
    if not isinstance(obj, cls):
        raise RuntimeError(f"Expected type '{cls}' but got '{type(obj)}'")
    if dtype is None:
        return obj  # type: ignore[return-value]

    value: Any
    if isinstance(obj, np.ndarray):
        value = np.asarray(obj).flatten()[0]  # pyright: ignore[reportUnknownArgumentType]
    elif hasattr(obj, "__iter__"):
        value = next(iter(cast(Iterable[Any], obj)))
    else:
        value = obj

    if not isinstance(value, dtype):
        raise RuntimeError(f"Expected type '{dtype}' but got '{type(value)}'")
    return obj  # type: ignore[return-value]


class HasArray:
    def __init__(self, array: np.ndarray[Any, Any]) -> None:
        self.array = array

    def __array__(self) -> np.ndarray[Any, Any]:
        return self.array
