from typing import Literal, overload

from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.patches import PathPatch
from matplotlib.typing import ColorType

from shapely.geometry import LinearRing, LineString, MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry

def patch_from_polygon(polygon: Polygon | MultiPolygon, **kwargs) -> PathPatch: ...
@overload
def plot_polygon(
    polygon: Polygon | MultiPolygon,
    ax: Axes | None = None,
    add_points: Literal[True] = True,
    color: ColorType | None = None,
    facecolor: ColorType | None = None,
    edgecolor: ColorType | None = None,
    linewidth: float | None = None,
    **kwargs,
) -> tuple[PathPatch, Line2D]: ...
@overload
def plot_polygon(
    polygon: Polygon | MultiPolygon,
    ax: Axes | None = None,
    *,
    add_points: Literal[False],
    color: ColorType | None = None,
    facecolor: ColorType | None = None,
    edgecolor: ColorType | None = None,
    linewidth: float | None = None,
    **kwargs,
) -> PathPatch: ...
@overload
def plot_line(
    line: LineString | LinearRing,
    ax: Axes | None = None,
    add_points: Literal[True] = True,
    color: ColorType | None = None,
    linewidth: float = 2,
    **kwargs,
) -> tuple[PathPatch, Line2D]: ...
@overload
def plot_line(
    line: LineString | LinearRing,
    ax: Axes | None = None,
    *,
    add_points: Literal[False],
    color: ColorType | None = None,
    linewidth: float = 2,
    **kwargs,
) -> PathPatch: ...
def plot_points(
    geom: BaseGeometry, ax: Axes | None = None, color: ColorType | None = None, marker: str = "o", **kwargs
) -> Line2D: ...
