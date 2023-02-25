from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from typing import Any
from typing_extensions import TypeAlias

from matplotlib.axis import Axis as Axis
from matplotlib.scale import ScaleBase as ScaleBase
from matplotlib.ticker import Formatter, Locator
from numpy.typing import ArrayLike, NDArray as NDArray
from pandas import Series as Series
from seaborn._core.plot import Plot as Plot
from seaborn._core.properties import Property as Property
from seaborn._core.rules import categorical_order as categorical_order
from seaborn._core.typing import Default as Default, default as default

TransFuncs: TypeAlias = tuple[Callable[[ArrayLike], ArrayLike], Callable[[ArrayLike], ArrayLike]]
Pipeline: TypeAlias = Sequence[Callable[[Any], Any] | None]

class Scale:
    values: tuple | str | list | dict | None
    def __post_init__(self) -> None: ...
    def tick(self) -> None: ...
    def label(self) -> None: ...
    def __call__(self, data: Series) -> ArrayLike: ...

class Boolean(Scale):
    values: tuple | list | dict | None
    def tick(self, locator: Locator | None = ...): ...
    def label(self, formatter: Formatter | None = ...): ...
    def __init__(self, values) -> None: ...

class Nominal(Scale):
    values: tuple | str | list | dict | None
    order: list | None
    def tick(self, locator: Locator | None = ...) -> Nominal: ...
    def label(self, formatter: Formatter | None = ...) -> Nominal: ...
    def __init__(self, values, order) -> None: ...

class Ordinal(Scale): ...
class Discrete(Scale): ...

class ContinuousBase(Scale):
    values: tuple | str | None
    norm: tuple | None
    def __init__(self, values, norm) -> None: ...

class Continuous(ContinuousBase):
    values: tuple | str | None
    trans: str | TransFuncs | None
    def tick(
        self,
        locator: Locator | None = ...,
        *,
        at: Sequence[float] | None = ...,
        upto: int | None = ...,
        count: int | None = ...,
        every: float | None = ...,
        between: tuple[float, float] | None = ...,
        minor: int | None = ...,
    ) -> Continuous: ...
    def label(
        self,
        formatter: Formatter | None = ...,
        *,
        like: str | Callable | None = ...,
        base: int | None | Default = ...,
        unit: str | None = ...,
    ) -> Continuous: ...
    def __init__(self, values, norm, trans) -> None: ...

class Temporal(ContinuousBase):
    trans: Incomplete
    def tick(self, locator: Locator | None = ..., *, upto: int | None = ...) -> Temporal: ...
    def label(self, formatter: Formatter | None = ..., *, concise: bool = ...) -> Temporal: ...
    def __init__(self, values, norm) -> None: ...

class PseudoAxis:
    axis_name: str
    converter: Incomplete
    units: Incomplete
    scale: Incomplete
    major: Incomplete
    minor: Incomplete
    def __init__(self, scale) -> None: ...
    def set_view_interval(self, vmin, vmax) -> None: ...
    def get_view_interval(self): ...
    def set_data_interval(self, vmin, vmax) -> None: ...
    def get_data_interval(self): ...
    def get_tick_space(self): ...
    def set_major_locator(self, locator) -> None: ...
    def set_major_formatter(self, formatter) -> None: ...
    def set_minor_locator(self, locator) -> None: ...
    def set_minor_formatter(self, formatter) -> None: ...
    def set_units(self, units) -> None: ...
    def update_units(self, x) -> None: ...
    def convert_units(self, x): ...
    def get_scale(self): ...
    def get_majorticklocs(self): ...
