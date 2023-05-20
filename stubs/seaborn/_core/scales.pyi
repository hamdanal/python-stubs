from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar
from typing_extensions import Self, TypeAlias

from matplotlib.axis import Axis as Axis, Ticker
from matplotlib.scale import ScaleBase as ScaleBase
from matplotlib.ticker import Formatter, Locator
from matplotlib.units import ConversionInterface
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
    trans: ClassVar[Incomplete]  # not sure if this is a classvar but dataclass machinery is corrupted otherwise
    def tick(self, locator: Locator | None = None, *, upto: int | None = None) -> Self: ...  # type: ignore[override]
    def label(self, formatter: Formatter | None = None, *, concise: bool = False) -> Self: ...  # type: ignore[override]

class PseudoAxis:
    axis_name: str
    converter: ConversionInterface | None
    units: Incomplete | None
    scale: ScaleBase
    major: Ticker
    minor: Ticker
    def __init__(self, scale) -> None: ...
    def set_view_interval(self, vmin, vmax) -> None: ...
    def get_view_interval(self) -> tuple[Incomplete, Incomplete]: ...
    def set_data_interval(self, vmin, vmax) -> None: ...
    def get_data_interval(self) -> tuple[Incomplete, Incomplete]: ...
    def get_tick_space(self) -> float: ...
    def set_major_locator(self, locator: Locator) -> None: ...
    def set_major_formatter(self, formatter: Formatter) -> None: ...
    def set_minor_locator(self, locator: Locator) -> None: ...
    def set_minor_formatter(self, formatter: Formatter) -> None: ...
    def set_units(self, units) -> None: ...
    def update_units(self, x) -> None: ...
    def convert_units(self, x): ...
    def get_scale(self) -> ScaleBase: ...
    def get_majorticklocs(self) -> NDArray: ...
