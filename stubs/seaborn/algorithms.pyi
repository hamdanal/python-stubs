from _typeshed import Incomplete
from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike

def bootstrap(
    *args: ArrayLike,
    n_boot: int = 10000,
    func: str | Callable,
    axis: int | None = None,
    units: ArrayLike | None = None,
    seed: Incomplete | int | None = None,
) -> np.ndarray: ...
