from collections.abc import Callable, Iterable
from typing import Any, Literal, TypeVar, overload
from typing_extensions import TypeVarTuple, Unpack, deprecated

from shapely._typing import GeoArrayLike, OptGeoArrayLike, SupportsGeoInterface
from shapely.algorithms.polylabel import polylabel as polylabel
from shapely.geometry import GeometryCollection, LineString, MultiLineString, Point, Polygon
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry, GeometrySequence
from shapely.geometry.linestring import _ConvertibleToLineString

__all__ = [
    "cascaded_union",
    "linemerge",
    "operator",
    "polygonize",
    "polygonize_full",
    "transform",
    "unary_union",
    "triangulate",
    "voronoi_diagram",
    "split",
    "nearest_points",
    "validate",
    "snap",
    "shared_paths",
    "clip_by_rect",
    "orient",
    "substring",
]

_Ts = TypeVarTuple("_Ts")
_GeoT = TypeVar("_GeoT", bound=BaseGeometry)

class CollectionOperator:
    @overload
    def shapeup(self, ob: _GeoT) -> _GeoT: ...
    @overload
    def shapeup(self, ob: dict[str, Any] | SupportsGeoInterface) -> BaseGeometry: ...
    @overload
    def shapeup(self, ob: _ConvertibleToLineString) -> LineString: ...
    def polygonize(
        self, lines: OptGeoArrayLike | Iterable[_ConvertibleToLineString | None]
    ) -> GeometrySequence[GeometryCollection]: ...
    def polygonize_full(
        self, lines: OptGeoArrayLike | Iterable[_ConvertibleToLineString | None]
    ) -> tuple[GeometryCollection, GeometryCollection, GeometryCollection, GeometryCollection]: ...
    def linemerge(
        self, lines: MultiLineString | BaseMultipartGeometry | Iterable[_ConvertibleToLineString], directed: bool = False
    ) -> LineString | MultiLineString: ...
    @deprecated("The `cascaded_union()` function is deprecated. Use `unary_union()` instead.")
    def cascaded_union(self, geoms: GeoArrayLike) -> BaseGeometry: ...
    def unary_union(self, geoms: GeoArrayLike) -> BaseGeometry: ...

operator: CollectionOperator
polygonize = operator.polygonize  # noqa: F821
polygonize_full = operator.polygonize_full  # noqa: F821
linemerge = operator.linemerge  # noqa: F821
cascaded_union = operator.cascaded_union  # noqa: F821  # pyright: ignore[reportDeprecated]
unary_union = operator.unary_union  # noqa: F821

@overload
def triangulate(geom: BaseGeometry, tolerance: float = 0.0, edges: Literal[False] = False) -> list[Polygon]: ...
@overload
def triangulate(geom: BaseGeometry, tolerance: float = 0.0, *, edges: Literal[True]) -> list[LineString]: ...
@overload
def triangulate(geom: BaseGeometry, tolerance: float, edges: Literal[True]) -> list[LineString]: ...
@overload  # fallback
def triangulate(geom: BaseGeometry, tolerance: float = 0.0, edges: bool = False) -> list[Polygon | LineString]: ...
def voronoi_diagram(
    geom: BaseGeometry, envelope: BaseGeometry | None = None, tolerance: float = 0.0, edges: bool = False
) -> GeometryCollection: ...
def validate(geom: BaseGeometry) -> str: ...
def transform(func: Callable[[Unpack[_Ts]], tuple[Unpack[_Ts]]], geom: _GeoT) -> _GeoT: ...
def nearest_points(g1: BaseGeometry, g2: BaseGeometry) -> tuple[Point, Point]: ...
def snap(g1: _GeoT, g2: BaseGeometry, tolerance: float) -> _GeoT: ...
def shared_paths(g1: LineString, g2: LineString) -> GeometryCollection: ...

class SplitOp:
    @staticmethod
    def split(geom: BaseGeometry, splitter: BaseGeometry) -> GeometryCollection: ...

split = SplitOp.split

def substring(geom: LineString, start_dist: float, end_dist: float, normalized: bool = False) -> Point | LineString: ...
def clip_by_rect(geom: BaseGeometry, xmin: float, ymin: float, xmax: float, ymax: float) -> BaseGeometry: ...
def orient(geom: _GeoT, sign: float = 1.0) -> _GeoT: ...
