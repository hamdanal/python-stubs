from collections.abc import Callable, Iterable
from typing import Any, Literal, overload
from typing_extensions import deprecated

from shapely._typing import GeoT, OptGeoArrayLike, SupportsGeoInterface
from shapely.algorithms.polylabel import polylabel as polylabel
from shapely.geometry import GeometryCollection, LineString, MultiLineString, Point, Polygon
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry, GeometrySequence
from shapely.geometry.linestring import _ConvertibleToLineString
from shapely.lib import Geometry

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

class CollectionOperator:
    @overload
    def shapeup(self, ob: GeoT) -> GeoT: ...  # type: ignore[overload-overlap]
    @overload
    def shapeup(self, ob: dict[str, Any] | SupportsGeoInterface) -> BaseGeometry: ...  # type: ignore[overload-overlap]
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
    def cascaded_union(self, geoms: OptGeoArrayLike) -> BaseGeometry: ...
    def unary_union(self, geoms: OptGeoArrayLike) -> BaseGeometry: ...

operator: CollectionOperator
polygonize = operator.polygonize  # noqa: F821
polygonize_full = operator.polygonize_full  # noqa: F821
linemerge = operator.linemerge  # noqa: F821
unary_union = operator.unary_union  # noqa: F821

# This is also an alias to operator method but we want to mark it as deprecated
@deprecated("The `cascaded_union()` function is deprecated. Use `unary_union()` instead.")
def cascaded_union(geoms: OptGeoArrayLike) -> BaseGeometry: ...
@overload  # edges false
def triangulate(geom: Geometry, tolerance: float = 0.0, edges: Literal[False] = False) -> list[Polygon]: ...
@overload  # edges true (keyword)
def triangulate(geom: Geometry, tolerance: float = 0.0, *, edges: Literal[True]) -> list[LineString]: ...
@overload  # edges true (positional)
def triangulate(geom: Geometry, tolerance: float, edges: Literal[True]) -> list[LineString]: ...
@overload  # fallback
def triangulate(geom: Geometry, tolerance: float = 0.0, edges: bool = False) -> list[Polygon] | list[LineString]: ...
def voronoi_diagram(
    geom: Geometry, envelope: Geometry | None = None, tolerance: float = 0.0, edges: bool = False
) -> GeometryCollection: ...
@overload
def validate(geom: None) -> None: ...
@overload
def validate(geom: Geometry) -> str: ...
@overload
def validate(geom: Geometry | None) -> str | None: ...
def transform(func: Callable[[float, float, float | None], tuple[float, ...]], geom: GeoT) -> GeoT: ...
def nearest_points(g1: Geometry, g2: Geometry) -> tuple[Point, Point]: ...
def snap(g1: GeoT, g2: Geometry, tolerance: float) -> GeoT: ...
def shared_paths(g1: LineString, g2: LineString) -> GeometryCollection: ...

class SplitOp:
    @staticmethod
    def split(geom: Geometry, splitter: Geometry) -> GeometryCollection: ...

split = SplitOp.split

def substring(geom: LineString, start_dist: float, end_dist: float, normalized: bool = False) -> Point | LineString: ...
def clip_by_rect(geom: Geometry, xmin: float, ymin: float, xmax: float, ymax: float) -> BaseGeometry: ...
def orient(geom: GeoT, sign: float = 1.0) -> GeoT: ...
