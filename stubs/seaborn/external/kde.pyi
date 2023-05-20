from collections.abc import Callable
from numbers import Number
from typing_extensions import Literal, TypeAlias

from numpy import float64
from numpy.typing import ArrayLike, NDArray

__all__ = ["gaussian_kde"]

_BwMethodType: TypeAlias = Literal["scott", "silverman"] | Callable[[gaussian_kde], object] | Number | bool | None

class gaussian_kde:
    dataset: NDArray[float64]
    def __init__(self, dataset: ArrayLike, bw_method: _BwMethodType = None, weights: ArrayLike | None = None) -> None: ...
    def evaluate(self, points: ArrayLike) -> NDArray[float64]: ...
    __call__ = evaluate
    def scotts_factor(self) -> float: ...
    def silverman_factor(self) -> float: ...
    covariance_factor = scotts_factor
    def set_bandwidth(self, bw_method: _BwMethodType = None): ...
    def pdf(self, x: ArrayLike) -> NDArray[float64]: ...
    @property
    def weights(self) -> NDArray[float64]: ...
    @property
    def neff(self) -> NDArray[float64]: ...
