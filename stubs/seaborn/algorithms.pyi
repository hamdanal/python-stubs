from _typeshed import Incomplete
from collections.abc import Callable

from numpy.typing import ArrayLike, NDArray

def bootstrap(
    *args: ArrayLike,
    n_boot: int = 10000,
    func: str | Callable = "mean",
    axis: int | None = None,
    units: ArrayLike | None = None,
    seed: Incomplete | int | None = None,
) -> NDArray: ...
