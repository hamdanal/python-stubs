from typing import overload

import numpy as np

@overload
def adapt_impedance_params(Z: complex, sign: int = 1, adaption: float = 1e-15) -> float: ...
@overload
def adapt_impedance_params[S: tuple[int, ...]](
    Z: np.ndarray[S, np.dtype[np.complexfloating]], sign: int = 1, adaption: float = 1e-15
) -> np.ndarray[S, np.dtype[np.float64]]: ...
