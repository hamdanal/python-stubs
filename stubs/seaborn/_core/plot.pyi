from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator
from contextlib import contextmanager
from typing import Any, TypeVar
from typing_extensions import TypedDict

from matplotlib.artist import Artist as Artist
from matplotlib.axes import Axes as Axes
from matplotlib.figure import Figure as Figure, SubFigure as SubFigure
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from seaborn._compat import set_layout_engine as set_layout_engine, set_scale_obj as set_scale_obj
from seaborn._core.data import PlotData as PlotData
from seaborn._core.exceptions import PlotSpecError as PlotSpecError
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.moves import Move as Move
from seaborn._core.properties import PROPERTIES as PROPERTIES, Property as Property
from seaborn._core.rules import categorical_order as categorical_order
from seaborn._core.scales import Nominal as Nominal, Scale as Scale
from seaborn._core.subplots import Subplots as Subplots
from seaborn._core.typing import (
    DataSource as DataSource,
    Default as Default,
    OrderSpec as OrderSpec,
    VariableSpec as VariableSpec,
    VariableSpecList as VariableSpecList,
)
from seaborn._marks.base import Mark as Mark
from seaborn._stats.base import Stat as Stat
from seaborn.external.version import Version as Version
from seaborn.palettes import color_palette as color_palette
from seaborn.rcmod import axes_style as axes_style, plotting_context as plotting_context

_ClsT = TypeVar("_ClsT", bound=type)

default: Default

class Layer(TypedDict, total=False):
    mark: Mark
    stat: Stat | None
    move: Move | list[Move] | None
    data: PlotData
    source: DataSource
    vars: dict[str, VariableSpec]
    orient: str
    legend: bool

class FacetSpec(TypedDict, total=False):
    variables: dict[str, VariableSpec]
    structure: dict[str, list[str]]
    wrap: int | None

class PairSpec(TypedDict, total=False):
    variables: dict[str, VariableSpec]
    structure: dict[str, list[str]]
    cross: bool
    wrap: int | None

@contextmanager
def theme_context(params: dict[str, Any]) -> Generator[None, None, None]: ...
def build_plot_signature(cls: _ClsT) -> _ClsT: ...
@build_plot_signature
class Plot:
    def __init__(self, *args: DataSource | VariableSpec, data: DataSource = None, **variables: VariableSpec) -> None: ...
    def __add__(self, other) -> None: ...
    def on(self, target: Axes | SubFigure | Figure) -> Plot: ...
    def add(
        self,
        mark: Mark,
        *transforms: Stat | Mark,
        orient: str | None = None,
        legend: bool = True,
        data: DataSource = None,
        **variables: VariableSpec,
    ) -> Plot: ...
    def pair(
        self, x: VariableSpecList = None, y: VariableSpecList = None, wrap: int | None = None, cross: bool = True
    ) -> Plot: ...
    def facet(
        self,
        col: VariableSpec = None,
        row: VariableSpec = None,
        order: OrderSpec | dict[str, OrderSpec] = None,
        wrap: int | None = None,
    ) -> Plot: ...
    def scale(self, **scales: Scale) -> Plot: ...
    def share(self, **shares: bool | str) -> Plot: ...
    def limit(self, **limits: tuple[Any, Any]) -> Plot: ...
    def label(self, *, title: Incomplete | None = None, **variables: str | Callable[[str], str]) -> Plot: ...
    def layout(self, *, size: tuple[float, float] | Default = ..., engine: str | None | Default = ...) -> Plot: ...
    def theme(self, *args: dict[str, Any]) -> Plot: ...
    def save(self, loc, **kwargs) -> Plot: ...
    def show(self, **kwargs) -> None: ...
    def plot(self, pyplot: bool = False) -> Plotter: ...

class Plotter:
    def __init__(self, pyplot: bool, theme: dict[str, Any]) -> None: ...
    def save(self, loc, **kwargs) -> Plotter: ...
    def show(self, **kwargs) -> None: ...
