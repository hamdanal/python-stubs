from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar
from typing_extensions import Self, TypeAlias

import numpy as np
from matplotlib.axis import Ticker
from matplotlib.scale import ScaleBase
from matplotlib.ticker import Formatter, Locator
from matplotlib.units import ConversionInterface
from numpy.typing import ArrayLike
from pandas import Series
from seaborn._core.typing import Default

TransFuncs: TypeAlias = tuple[Callable[[ArrayLike], ArrayLike], Callable[[ArrayLike], ArrayLike]]
Pipeline: TypeAlias = Sequence[Callable[[Any], Any] | None]

class Scale:
    values: tuple | str | list | dict | None
    def __post_init__(self) -> None: ...
    def tick(self) -> Self: ...
    def label(self) -> Self: ...
    def __call__(self, data: Series) -> ArrayLike: ...

@dataclass
class Boolean(Scale):
    values: tuple | list | dict | None = ...  # None # pytype parse error
    def tick(self, locator: Locator | None = None) -> Self: ...  # type: ignore[override]
    def label(self, formatter: Formatter | None = None) -> Self: ...  # type: ignore[override]

@dataclass
class Nominal(Scale):
    values: tuple | str | list | dict | None = ...  # None # pytype parse error
    order: list | None = ...  # None # pytype parse error
    def tick(self, locator: Locator | None = None) -> Self: ...  # type: ignore[override]
    def label(self, formatter: Formatter | None = None) -> Self: ...  # type: ignore[override]

@dataclass
class Ordinal(Scale): ...

@dataclass
class Discrete(Scale): ...

@dataclass
class ContinuousBase(Scale):
    values: tuple | str | None = ...  # None # pytype parse error
    norm: tuple | None = ...  # None # pytype parse error

@dataclass
class Continuous(ContinuousBase):
    values: tuple | str | None = ...  # None # pytype parse error
    trans: str | TransFuncs | None = ...  # None # pytype parse error
    def tick(  # type: ignore[override]
        self,
        locator: Locator | None = None,
        *,
        at: Sequence[float] | None = None,
        upto: int | None = None,
        count: int | None = None,
        every: float | None = None,
        between: tuple[float, float] | None = None,
        minor: int | None = None,
    ) -> Self: ...
    def label(  # type: ignore[override]
        self,
        formatter: Formatter | None = None,
        *,
        like: str | Callable | None = None,
        base: int | None | Default = ...,
        unit: str | None = None,
    ) -> Self: ...

@dataclass
class Temporal(ContinuousBase):
    trans: ClassVar[Incomplete]  # not sure it is a classvar but the runtime has no annotation so it is not a dataclass field
    def tick(self, locator: Locator | None = None, *, upto: int | None = None) -> Self: ...  # type: ignore[override]
    def label(self, formatter: Formatter | None = None, *, concise: bool = False) -> Self: ...  # type: ignore[override]

class PseudoAxis:
    axis_name: str
    converter: ConversionInterface | None
    units: Incomplete | None
    scale: ScaleBase
    major: Ticker
    minor: Ticker
    def __init__(self, scale: ScaleBase) -> None: ...
    def set_view_interval(self, vmin: float, vmax: float) -> None: ...
    def get_view_interval(self) -> tuple[float, float]: ...
    def set_data_interval(self, vmin: float, vmax: float) -> None: ...
    def get_data_interval(self) -> tuple[float, float]: ...
    def get_tick_space(self) -> int: ...
    def set_major_locator(self, locator: Locator) -> None: ...
    def set_major_formatter(self, formatter: Formatter) -> None: ...
    def set_minor_locator(self, locator: Locator) -> None: ...
    def set_minor_formatter(self, formatter: Formatter) -> None: ...
    def set_units(self, units: Incomplete) -> None: ...
    def update_units(self, x: Incomplete) -> None: ...
    def convert_units(self, x: Incomplete) -> Incomplete: ...
    def get_scale(self) -> ScaleBase: ...
    def get_majorticklocs(self) -> np.ndarray: ...
