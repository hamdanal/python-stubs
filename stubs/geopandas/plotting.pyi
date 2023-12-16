from collections.abc import Hashable, Iterable, Sequence
from typing import Any, Literal
from typing_extensions import TypeAlias, deprecated

import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.collections import Collection, LineCollection, PatchCollection
from matplotlib.colors import Colormap
from matplotlib.typing import MarkerType
from numpy.typing import ArrayLike, NDArray
from pandas.plotting import PlotAccessor

from .geodataframe import GeoDataFrame
from .geoseries import GeoSeries

_Color: TypeAlias = str | Sequence[str] | pd.Index[str] | pd.Series[str] | NDArray[np.str_]

@deprecated("Function `plot_polygon_collection` is deprecated.")
def plot_polygon_collection(
    ax: Axes,
    geoms: GeoSeries,
    values: ArrayLike | None = None,
    color: _Color | None = None,
    cmap: str | Colormap | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    **kwargs,
) -> PatchCollection: ...
@deprecated("Function `plot_linestring_collection` is deprecated.")
def plot_linestring_collection(
    ax: Axes,
    geoms: GeoSeries,
    values: ArrayLike | None = None,
    color: _Color | None = None,
    cmap: str | Colormap | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    **kwargs,
) -> LineCollection: ...
@deprecated("Function `plot_point_collection` is deprecated.")
def plot_point_collection(
    ax: Axes,
    geoms: GeoSeries,
    values: ArrayLike | None = None,
    color: _Color | None = None,
    cmap: str | Colormap | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    marker: MarkerType = "o",
    markersize: ArrayLike | None = None,
    **kwargs,
) -> Collection: ...
def plot_series(
    s: GeoSeries,
    cmap: str | Colormap | None = None,
    color: _Color | None = None,
    ax: Axes | None = None,
    figsize: tuple[int, int] | None = None,
    aspect: Literal["auto", "equal"] | float | None = "auto",
    **style_kwds: Any,
) -> Axes: ...
def plot_dataframe(
    df: GeoDataFrame,
    column: Hashable | None = None,
    cmap: str | Colormap | None = None,
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
    **style_kwds: Any,
) -> Axes: ...

class GeoplotAccessor(PlotAccessor):
    def __call__(self, *args, **kwargs) -> Axes: ...  # type: ignore[override]
    def geo(self, *args, **kwargs) -> Axes: ...
