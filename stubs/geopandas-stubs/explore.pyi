from collections.abc import Callable, Hashable, MutableMapping, Sequence
from typing import Any

import branca
import folium
import pandas as pd
import xyzservices
from matplotlib.colors import Colormap
from numpy.typing import ArrayLike, NDArray

from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

def _explore(
    df: GeoDataFrame,
    column: Hashable | NDArray[Any] | pd.Series[Any] | None = None,
    cmap: str | Colormap | branca.colormap.ColorMap | Sequence[str] | Callable[[Any], str] | None = None,
    color: str | ArrayLike | None = None,
    m: folium.Map | None = None,
    tiles: str | folium.TileLayer | xyzservices.TileProvider | None = "OpenStreetMap",
    attr: str | None = None,
    tooltip: bool = True,
    popup: bool = False,
    highlight: bool = True,
    categorical: bool = False,
    legend: bool = True,
    scheme: str | None = None,
    k: int = 5,
    vmin: float | None = None,
    vmax: float | None = None,
    width: float | str = "100%",
    height: float | str = "100%",
    categories=None,
    classification_kwds: MutableMapping[str, Any] | None = None,
    control_scale: bool = True,
    marker_type: str | folium.Marker | None = None,
    marker_kwds: MutableMapping[str, Any] = {},
    style_kwds: MutableMapping[str, Any] = {},
    highlight_kwds: MutableMapping[str, Any] = {},
    missing_kwds: MutableMapping[str, Any] = {},
    tooltip_kwds: MutableMapping[str, Any] = {},
    popup_kwds: MutableMapping[str, Any] = {},
    legend_kwds: MutableMapping[str, Any] = {},
    map_kwds: MutableMapping[str, Any] = {},
    **kwargs: Any,
) -> folium.Map: ...
def _explore_geoseries(
    s: GeoSeries,
    color: str | ArrayLike | None = None,
    m: folium.Map | None = None,
    tiles: str | folium.TileLayer | xyzservices.TileProvider | None = "OpenStreetMap",
    attr: str | None = None,
    highlight: bool = True,
    width: float | str = "100%",
    height: float | str = "100%",
    control_scale: bool = True,
    marker_type: str | folium.Marker | None = None,
    marker_kwds: MutableMapping[str, Any] = {},
    style_kwds: MutableMapping[str, Any] = {},
    highlight_kwds: MutableMapping[str, Any] = {},
    map_kwds: MutableMapping[str, Any] = {},
    **kwargs: Any,
) -> folium.Map: ...
