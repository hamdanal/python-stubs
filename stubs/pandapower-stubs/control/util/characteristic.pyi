from _typeshed import Incomplete
from builtins import object as object

from pandapower.io_utils import JSONSerializableClass

class Characteristic(JSONSerializableClass):
    x_vals: Incomplete
    y_vals: Incomplete
    index: Incomplete
    def __init__(self, net, x_values, y_values, **kwargs) -> None: ...
    @classmethod
    def from_points(cls, net, points, **kwargs): ...
    @classmethod
    def from_gradient(cls, net, zero_crossing, gradient, y_min, y_max, **kwargs): ...
    def diff(self, x, measured): ...
    def satisfies(self, x, measured, epsilon): ...
    def __call__(self, x): ...

class SplineCharacteristic(Characteristic):
    json_excludes: Incomplete
    fill_value: Incomplete
    kind: Incomplete
    def __init__(self, net, x_values, y_values, kind: str = "quadratic", fill_value: str = "extrapolate", **kwargs) -> None: ...
    @property
    def interpolator(self): ...
    def __call__(self, x): ...
