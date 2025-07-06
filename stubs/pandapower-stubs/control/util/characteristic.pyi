from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import Literal, Self

import numpy as np
from numpy.typing import ArrayLike
from scipy.interpolate import PchipInterpolator, interp1d  # type: ignore[import-untyped]

from pandapower._typing import Float, Int
from pandapower.auxiliary import pandapowerNet
from pandapower.io_utils import JSONSerializableClass

class Characteristic(JSONSerializableClass):
    x_vals: Incomplete
    y_vals: Incomplete
    index: np.int64
    def __init__(self, net: pandapowerNet, x_values, y_values, table: str = "characteristic", **kwargs) -> None: ...
    @classmethod
    def from_points(cls, net: pandapowerNet, points: Iterable[Iterable[Float]], **kwargs) -> Self: ...
    @classmethod
    def from_gradient(cls, net: pandapowerNet, zero_crossing, gradient, y_min, y_max, **kwargs): ...
    def diff(self, x: Float, measured: Float): ...
    def satisfies(self, x: Float, measured: Float, epsilon: Float) -> bool: ...
    def __call__(self, x: Float) -> np.float64: ...

class SplineCharacteristic(Characteristic):
    json_excludes: list[str]
    kwargs: dict[str, Any]
    interpolator_kind: Literal["interp1d", "Pchip"]
    def __init__(
        self,
        net: pandapowerNet,
        x_values,
        y_values,
        interpolator_kind: Literal["interp1d", "Pchip"] = "interp1d",
        table: str = "characteristic",
        **kwargs,
    ) -> None: ...
    @property
    def interpolator(self) -> interp1d | PchipInterpolator: ...
    def __call__(self, x: Float) -> np.float64: ...

class LogSplineCharacteristic(SplineCharacteristic):
    def __init__(self, net: pandapowerNet, x_values, y_values, **kwargs) -> None: ...
    @property
    def x_vals(self): ...
    @x_vals.setter
    def x_vals(self, x_values) -> None: ...
    @property
    def y_vals(self): ...
    @y_vals.setter
    def y_vals(self, y_values) -> None: ...
    def __call__(self, x: Float) -> np.float64: ...

def default_interp1d(
    x,
    y,
    kind: str | Int = "quadratic",
    bounds_error: bool = False,
    fill_value: ArrayLike | Literal["extrapolate"] = "extrapolate",
    **kwargs,
) -> interp1d: ...
