from _typeshed import Incomplete
from collections import UserString
from collections.abc import Callable, Container, Generator, Mapping
from typing import TypeVar
from typing_extensions import Literal, Self

import pandas as pd

from ._decorators import share_init_params_with_map as share_init_params_with_map
from .external.version import Version as Version
from .palettes import QUAL_PALETTES as QUAL_PALETTES, color_palette as color_palette
from .utils import get_color_cycle as get_color_cycle, remove_na as remove_na

_PlotterT = TypeVar("_PlotterT", bound=VectorPlotter)

class SemanticMapping:
    map_type: str
    levels: Incomplete
    lookup_table: Incomplete
    plotter: VectorPlotter
    def __init__(self, plotter: VectorPlotter) -> None: ...
    def map(cls, plotter: _PlotterT, *args, **kwargs) -> _PlotterT: ...
    def __call__(self, key, *args, **kwargs) -> Incomplete: ...

class HueMapping(SemanticMapping):
    palette: Incomplete
    norm: Incomplete
    cmap: Incomplete
    map_type: str
    lookup_table: dict[Incomplete, Incomplete]
    levels: list[Incomplete]
    def __init__(
        self,
        plotter: VectorPlotter,
        palette: Incomplete | None = None,
        order: Incomplete | None = None,
        norm: Incomplete | None = None,
    ) -> None: ...
    def infer_map_type(self, palette, norm, input_format, var_type) -> str: ...
    def categorical_mapping(self, data, palette, order) -> tuple[list[Incomplete], dict[Incomplete, Incomplete]]: ...
    def numeric_mapping(
        self, data, palette, norm
    ) -> tuple[list[Incomplete], dict[Incomplete, Incomplete], Incomplete, Incomplete]: ...

class SizeMapping(SemanticMapping):
    norm: Incomplete
    map_type: str
    levels: list[Incomplete]
    sizes: Incomplete
    size_range: Incomplete
    lookup_table: dict[Incomplete, Incomplete]
    def __init__(
        self,
        plotter: VectorPlotter,
        sizes: Incomplete | None = None,
        order: Incomplete | None = None,
        norm: Incomplete | None = None,
    ) -> None: ...
    def infer_map_type(self, norm, sizes, var_type) -> str: ...
    def categorical_mapping(self, data, sizes, order) -> tuple[list[Incomplete], dict[Incomplete, Incomplete]]: ...
    def numeric_mapping(
        self, data, sizes, norm
    ) -> tuple[list[Incomplete], dict[Incomplete, Incomplete], Incomplete, Incomplete]: ...

class StyleMapping(SemanticMapping):
    map_type: str
    levels: Incomplete
    lookup_table: Incomplete
    def __init__(
        self, plotter, markers: Incomplete | None = None, dashes: Incomplete | None = None, order: Incomplete | None = None
    ) -> None: ...

class VectorPlotter:
    semantics: tuple[str, ...]
    wide_structure: dict[str, str]
    flat_structure: dict[str, str]
    input_format: str
    plot_data: pd.DataFrame
    variables: dict[str, Incomplete]
    var_types: dict[str, VariableType]
    map_hue: Callable[..., Self]
    map_size: Callable[..., Self]
    map_style: Callable[..., Self]
    def __init__(self, data: Incomplete | None = None, variables: dict[str, Incomplete] = {}) -> None: ...
    @classmethod
    def get_semantics(
        cls, kwargs: Mapping[str, Incomplete], semantics: Container[str] | None = None
    ) -> dict[str, Incomplete]: ...
    @property
    def has_xy_data(self) -> bool: ...
    @property
    def var_levels(self) -> dict[str, Incomplete]: ...
    def assign_variables(self, data: Incomplete | None = None, variables: dict[str, Incomplete] = {}) -> Self: ...
    def iter_data(
        self,
        grouping_vars: str | tuple[str, ...] | list[str] | None = None,
        *,
        reverse: bool = False,
        from_comp_data: bool = False,
        by_facet: bool = True,
        allow_empty: bool = False,
        dropna: bool = True,
    ) -> Generator[tuple[dict[str, Incomplete], pd.DataFrame], None, None]: ...
    @property
    def comp_data(self) -> pd.DataFrame: ...
    def scale_native(self, axis, *args, **kwargs) -> None: ...
    def scale_numeric(self, axis, *args, **kwargs) -> None: ...
    def scale_datetime(self, axis, *args, **kwargs) -> None: ...
    def scale_categorical(
        self, axis: Literal["x", "y"], order: Incomplete | None = None, formatter: Incomplete | None = None
    ) -> Self: ...

class VariableType(UserString):
    allowed: tuple[str, ...]
    def __init__(self, data: str) -> None: ...
    def __eq__(self, other: str) -> bool: ...

def variable_type(vector, boolean_type: Literal["numeric", "categorical"] = "numeric") -> VariableType: ...
def infer_orient(
    x: Incomplete | None = None, y: Incomplete | None = None, orient: Incomplete | None = None, require_numeric: bool = True
) -> Literal["v", "h"]: ...
def unique_dashes(n: int) -> list[tuple[float, ...] | str]: ...
def unique_markers(n: int) -> list[tuple[float, ...] | str]: ...
def categorical_order(vector, order: Incomplete | None = None) -> list[Incomplete]: ...
