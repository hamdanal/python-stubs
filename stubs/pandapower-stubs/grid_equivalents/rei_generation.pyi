from typing import TypeVar, overload

import numpy as np

_S = TypeVar("_S", bound=tuple[int, ...])

@overload
def adapt_impedance_params(Z: complex, sign: int = 1, adaption: float = 1e-15) -> float: ...
@overload
def adapt_impedance_params(
    Z: np.ndarray[_S, np.dtype[np.complexfloating]], sign: int = 1, adaption: float = 1e-15
) -> np.ndarray[_S, np.dtype[np.float64]]: ...
