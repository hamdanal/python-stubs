from collections.abc import Hashable, Iterable, Sequence
from typing import Any, Callable, Literal, TypeVar
from typing_extensions import TypeAlias

import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.collections import Collection, LineCollection, PatchCollection
from numpy.typing import ArrayLike, NDArray
from pandas.plotting import PlotAccessor

from .geodataframe import GeoDataFrame
from .geoseries import GeoSeries

_F = TypeVar("_F", bound=Callable[..., Any])
_Color: TypeAlias = str | Sequence[str] | pd.Index[str] | pd.Series[str] | NDArray[np.str_]

def deprecated(new: _F, warning_type: type[Warning] = ...) -> _F: ...
@deprecated
def plot_polygon_collection(
    ax: Axes, geoms, values=None, color=None, cmap=None, vmin=None, vmax=None, **kwargs
) -> PatchCollection: ...
@deprecated
def plot_linestring_collection(
    ax: Axes, geoms, values=None, color=None, cmap=None, vmin=None, vmax=None, **kwargs
) -> LineCollection: ...
@deprecated
def plot_point_collection(
    ax: Axes, geoms, values=None, color=None, cmap=None, vmin=None, vmax=None, marker="o", markersize=None, **kwargs
) -> Collection: ...
def plot_series(
    s: GeoSeries,
    cmap: str | None = None,
    color: _Color | None = None,
    ax: Axes | None = None,
    figsize: tuple[int, int] | None = None,
    aspect: Literal["auto", "equal"] | float | None = "auto",
    **style_kwds: Any,
) -> Axes: ...
def plot_dataframe(
    df: GeoDataFrame,
    column: Hashable | None = None,
    cmap: str | None = None,
    color: _Color | None = None,
    ax: Axes | None = None,
    cax: Axes | None = None,
    categorical: bool = False,
    legend: bool = False,
    scheme: str | None = None,
    k: int = 5,
    vmin: float | None = None,
    vmax: float | None = None,
    markersize: str | float | Iterable[float] | ArrayLike | None = None,
    figsize: tuple[int, int] | None = None,
    legend_kwds: dict[str, Any] | None = None,
    categories: Iterable[Hashable] | None = None,
    classification_kwds: dict[str, Any] | None = None,
    missing_kwds: dict[str, Any] | None = None,
    aspect: Literal["auto", "equal"] | float | None = "auto",
    **style_kwds,
) -> Axes: ...

class GeoplotAccessor(PlotAccessor):
    def __call__(self, *args, **kwargs) -> Axes: ...  # type: ignore[override]
    def geo(self, *args, **kwargs) -> Axes: ...
