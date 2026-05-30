import io
from _typeshed import SupportsRead
from collections.abc import Collection
from pathlib import Path
from typing import Any, Protocol, type_check_only
from typing_extensions import CapsuleType

import numpy as np

@type_check_only
class SupportsArrowCStream(Protocol):
    def __arrow_c_stream__(self, requested_schema: object | None = None) -> CapsuleType: ...

@type_check_only
class SupportsArray[G: np.generic](Protocol):
    def __array__(self) -> np.ndarray[Any, np.dtype[G]]: ...

type Array1D[G: np.generic] = np.ndarray[tuple[int], np.dtype[G]]
type Array2D[G: np.generic] = np.ndarray[tuple[int, int], np.dtype[G]]
type ReadPathOrBuffer = str | Path | bytes | SupportsRead[bytes]
type WritePathOrBuffer = str | Path | io.BytesIO

type DualArrayLike[G: np.generic, T] = SupportsArray[G] | Collection[T] | T
type ArrayLikeInt = DualArrayLike[np.bool | np.integer, int]
