from collections.abc import Hashable, Iterable, Sequence
from typing import Any, Literal
from typing_extensions import TypeAlias, deprecated

from matplotlib.axes import Axes
from matplotlib.collections import Collection, LineCollection, PatchCollection
from matplotlib.colors import Colormap, Normalize
from matplotlib.typing import ColorType, MarkerType
from numpy.typing import ArrayLike
from pandas.plotting import PlotAccessor

from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

_ColorOrColors: TypeAlias = ColorType | Sequence[ColorType] | ArrayLike

@deprecated("Function `plot_polygon_collection` is deprecated.")
def plot_polygon_collection(
    ax: Axes,
    geoms: GeoSeries,
    values: ArrayLike | None = None,
    color: _ColorOrColors | None = None,
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
    color: _ColorOrColors | None = None,
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
    color: _ColorOrColors | None = None,
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
    color: _ColorOrColors | None = None,
    ax: Axes | None = None,
    figsize: tuple[int, int] | None = None,
    aspect: Literal["auto", "equal"] | float | None = "auto",
    *,
    # Extracted from `**style_kwds`
    vmin: float = ...,
    vmax: float = ...,
    facecolor: _ColorOrColors | None = None,
    norm: Normalize | None = None,
    **style_kwds: Any,
) -> Axes: ...
def plot_dataframe(
    df: GeoDataFrame,
    column: Hashable | None = None,
    cmap: str | Colormap | None = None,
    color: _ColorOrColors | None = None,
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
    *,
    # Extracted from `**style_kwds`
    norm: Normalize | None = None,
    alpha: float = 1,
    facecolor: _ColorOrColors | None = None,
    edgecolor: _ColorOrColors | None = None,
    linewidth: float = ...,
    label: str = "NaN",
    **style_kwds: Any,
) -> Axes: ...

class GeoplotAccessor(PlotAccessor):
    def __call__(self, *args, **kwargs) -> Axes: ...  # type: ignore[override]
    def geo(self, *args, **kwargs) -> Axes: ...
