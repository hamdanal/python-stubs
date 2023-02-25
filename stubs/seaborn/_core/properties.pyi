from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias

from matplotlib.path import Path
from numpy.typing import ArrayLike
from pandas import Series as Series
from seaborn._compat import MarkerStyle as MarkerStyle
from seaborn._core.rules import categorical_order as categorical_order, variable_type as variable_type
from seaborn._core.scales import (
    Boolean as Boolean,
    Continuous as Continuous,
    Nominal as Nominal,
    Scale as Scale,
    Temporal as Temporal,
)
from seaborn.palettes import QUAL_PALETTES as QUAL_PALETTES, blend_palette as blend_palette, color_palette as color_palette
from seaborn.utils import get_color_cycle as get_color_cycle

RGBTuple: TypeAlias = tuple[float, float, float]
RGBATuple: TypeAlias = tuple[float, float, float, float]
ColorSpec: TypeAlias = RGBTuple | RGBATuple | str
DashPattern: TypeAlias = tuple[float, ...]
DashPatternWithOffset: TypeAlias = tuple[float, DashPattern | None]
MarkerPattern: TypeAlias = float | str | tuple[int, int, float] | list[tuple[float, float]] | Path | MarkerStyle
Mapping: TypeAlias = Callable[[ArrayLike], ArrayLike]

class Property:
    legend: bool
    normed: bool
    variable: Incomplete
    def __init__(self, variable: str | None = ...) -> None: ...
    def default_scale(self, data: Series) -> Scale: ...
    def infer_scale(self, arg: Any, data: Series) -> Scale: ...
    def get_mapping(self, scale: Scale, data: Series) -> Mapping: ...
    def standardize(self, val: Any) -> Any: ...

class Coordinate(Property):
    legend: bool
    normed: bool

class IntervalProperty(Property):
    legend: bool
    normed: bool
    @property
    def default_range(self) -> tuple[float, float]: ...
    def infer_scale(self, arg: Any, data: Series) -> Scale: ...
    def get_mapping(self, scale: Scale, data: Series) -> Mapping: ...

class PointSize(IntervalProperty): ...

class LineWidth(IntervalProperty):
    @property
    def default_range(self) -> tuple[float, float]: ...

class EdgeWidth(IntervalProperty):
    @property
    def default_range(self) -> tuple[float, float]: ...

class Stroke(IntervalProperty): ...
class Alpha(IntervalProperty): ...
class Offset(IntervalProperty): ...

class FontSize(IntervalProperty):
    @property
    def default_range(self) -> tuple[float, float]: ...

class ObjectProperty(Property):
    legend: bool
    normed: bool
    null_value: Any
    def default_scale(self, data: Series) -> Scale: ...
    def infer_scale(self, arg: Any, data: Series) -> Scale: ...
    def get_mapping(self, scale: Scale, data: Series) -> Mapping: ...

class Marker(ObjectProperty):
    null_value: Incomplete
    def standardize(self, val: MarkerPattern) -> MarkerStyle: ...

class LineStyle(ObjectProperty):
    null_value: str
    def standardize(self, val: str | DashPattern) -> DashPatternWithOffset: ...

class TextAlignment(ObjectProperty):
    legend: bool

class HorizontalAlignment(TextAlignment): ...
class VerticalAlignment(TextAlignment): ...

class Color(Property):
    legend: bool
    normed: bool
    def standardize(self, val: ColorSpec) -> RGBTuple | RGBATuple: ...
    def infer_scale(self, arg: Any, data: Series) -> Scale: ...
    def get_mapping(self, scale: Scale, data: Series) -> Mapping: ...

class Fill(Property):
    legend: bool
    normed: bool
    def default_scale(self, data: Series) -> Scale: ...
    def infer_scale(self, arg: Any, data: Series) -> Scale: ...
    def standardize(self, val: Any) -> bool: ...
    def get_mapping(self, scale: Scale, data: Series) -> Mapping: ...

PROPERTY_CLASSES: Incomplete
PROPERTIES: Incomplete
