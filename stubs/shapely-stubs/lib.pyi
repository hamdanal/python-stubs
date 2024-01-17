from typing import Literal, SupportsIndex, final, overload
from typing_extensions import Never

import numpy as np
from numpy.typing import NDArray

# ruff: noqa: PYI021

area: np.ufunc
"""area(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

boundary: np.ufunc
"""boundary(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

bounds: np.ufunc
"""bounds(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

box: np.ufunc
"""box(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

buffer: np.ufunc
"""buffer(x1, x2, x3, x4, x5, x6, x7, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

build_area: np.ufunc
"""build_area(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

centroid: np.ufunc
"""centroid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

clip_by_rect: np.ufunc
"""clip_by_rect(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

concave_hull: np.ufunc
"""concave_hull(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

contains: np.ufunc
"""contains(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

contains_properly: np.ufunc
"""contains_properly(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

contains_xy: np.ufunc
"""contains_xy(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

convex_hull: np.ufunc
"""convex_hull(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

coverage_union: np.ufunc
"""coverage_union(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

covered_by: np.ufunc
"""covered_by(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

covers: np.ufunc
"""covers(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

create_collection: np.ufunc
"""create_collection(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

crosses: np.ufunc
"""crosses(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

delaunay_triangles: np.ufunc
"""delaunay_triangles(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

destroy_prepared: np.ufunc
"""destroy_prepared(x, /, out=(), *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

difference: np.ufunc
"""difference(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

difference_prec: np.ufunc
"""difference_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

disjoint: np.ufunc
"""disjoint(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

distance: np.ufunc
"""distance(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

dwithin: np.ufunc
"""dwithin(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

envelope: np.ufunc
"""envelope(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

equals: np.ufunc
"""equals(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

equals_exact: np.ufunc
"""equals_exact(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

extract_unique_points: np.ufunc
"""extract_unique_points(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

force_2d: np.ufunc
"""force_2d(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

force_3d: np.ufunc
"""force_3d(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

frechet_distance: np.ufunc
"""frechet_distance(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

frechet_distance_densify: np.ufunc
"""frechet_distance_densify(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

from_geojson: np.ufunc
"""from_geojson(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

from_wkb: np.ufunc
"""from_wkb(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

from_wkt: np.ufunc
"""from_wkt(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_coordinate_dimension: np.ufunc
"""get_coordinate_dimension(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_dimensions: np.ufunc
"""get_dimensions(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_exterior_ring: np.ufunc
"""get_exterior_ring(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_geometry: np.ufunc
"""get_geometry(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_interior_ring: np.ufunc
"""get_interior_ring(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_coordinates: np.ufunc
"""get_num_coordinates(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_geometries: np.ufunc
"""get_num_geometries(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_interior_rings: np.ufunc
"""get_num_interior_rings(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_points: np.ufunc
"""get_num_points(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_point: np.ufunc
"""get_point(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_precision: np.ufunc
"""get_precision(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_srid: np.ufunc
"""get_srid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_type_id: np.ufunc
"""get_type_id(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_x: np.ufunc
"""get_x(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_y: np.ufunc
"""get_y(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_z: np.ufunc
"""get_z(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

has_z: np.ufunc
"""has_z(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

hausdorff_distance: np.ufunc
"""hausdorff_distance(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

hausdorff_distance_densify: np.ufunc
"""hausdorff_distance_densify(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersection: np.ufunc
"""intersection(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersection_all: np.ufunc
"""intersection_all(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

intersection_prec: np.ufunc
"""intersection_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersects: np.ufunc
"""intersects(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersects_xy: np.ufunc
"""intersects_xy(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_ccw: np.ufunc
"""is_ccw(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_closed: np.ufunc
"""is_closed(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_empty: np.ufunc
"""is_empty(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_geometry: np.ufunc
"""is_geometry(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_missing: np.ufunc
"""is_missing(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_prepared: np.ufunc
"""is_prepared(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_ring: np.ufunc
"""is_ring(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_simple: np.ufunc
"""is_simple(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_valid: np.ufunc
"""is_valid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_valid_input: np.ufunc
"""is_valid_input(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_valid_reason: np.ufunc
"""is_valid_reason(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

length: np.ufunc
"""length(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_interpolate_point: np.ufunc
"""line_interpolate_point(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_interpolate_point_normalized: np.ufunc
"""line_interpolate_point_normalized(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_locate_point: np.ufunc
"""line_locate_point(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_locate_point_normalized: np.ufunc
"""line_locate_point_normalized(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_merge: np.ufunc
"""line_merge(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_merge_directed: np.ufunc
"""line_merge_directed(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

linearrings: np.ufunc
"""linearrings(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

linestrings: np.ufunc
"""linestrings(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

make_valid: np.ufunc
"""make_valid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

minimum_bounding_circle: np.ufunc
"""minimum_bounding_circle(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

minimum_bounding_radius: np.ufunc
"""minimum_bounding_radius(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

minimum_clearance: np.ufunc
"""minimum_clearance(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

node: np.ufunc
"""node(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

normalize: np.ufunc
"""normalize(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

offset_curve: np.ufunc
"""offset_curve(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

oriented_envelope: np.ufunc
"""oriented_envelope(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

overlaps: np.ufunc
"""overlaps(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

point_on_surface: np.ufunc
"""point_on_surface(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

points: np.ufunc
"""points(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

polygonize: np.ufunc
"""polygonize(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

polygonize_full: np.ufunc
"""polygonize_full(x[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

polygons: np.ufunc
"""polygons(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

prepare: np.ufunc
"""prepare(x, /, out=(), *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

relate: np.ufunc
"""relate(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

relate_pattern: np.ufunc
"""relate_pattern(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

remove_repeated_points: np.ufunc
"""remove_repeated_points(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

reverse: np.ufunc
"""reverse(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

segmentize: np.ufunc
"""segmentize(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

set_precision: np.ufunc
"""set_precision(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

set_srid: np.ufunc
"""set_srid(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

shared_paths: np.ufunc
"""shared_paths(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

shortest_line: np.ufunc
"""shortest_line(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

simplify: np.ufunc
"""simplify(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

simplify_preserve_topology: np.ufunc
"""simplify_preserve_topology(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

snap: np.ufunc
"""snap(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

symmetric_difference: np.ufunc
"""symmetric_difference(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

symmetric_difference_all: np.ufunc
"""symmetric_difference_all(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

symmetric_difference_prec: np.ufunc
"""symmetric_difference_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

to_geojson: np.ufunc
"""to_geojson(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

to_wkb: np.ufunc
"""to_wkb(x1, x2, x3, x4, x5, x6, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

to_wkt: np.ufunc
"""to_wkt(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

touches: np.ufunc
"""touches(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

unary_union: np.ufunc
"""unary_union(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

unary_union_prec: np.ufunc
"""unary_union_prec(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

union: np.ufunc
"""union(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

union_prec: np.ufunc
"""union_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

voronoi_polygons: np.ufunc
"""voronoi_polygons(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

within: np.ufunc
"""within(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

geos_capi_version: tuple[int, int, int]
geos_capi_version_string: str
geos_version: tuple[int, int, int]
geos_version_string: str
registry: list[Geometry]

class Geometry:
    """Geometry type"""

    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __ge__(self, other: Never) -> bool: ...
    def __gt__(self, other: Never) -> bool: ...
    def __le__(self, other: Never) -> bool: ...
    def __lt__(self, other: Never) -> bool: ...

@final
class STRtree:
    """A query-only R-tree created using the Sort-Tile-Recursive (STR) algorithm."""

    count: int
    """The number of geometries inside the tree"""
    def __init__(self, geoms: NDArray[np.object_], node_capacity: SupportsIndex, /, **kwargs: object) -> None: ...
    def dwithin(self, geoms: NDArray[np.object_], distances: NDArray[np.float64], /) -> NDArray[np.int64]:
        """Queries the index for all item(s) in the tree within given distance of search geometries"""
    def nearest(self, geoms: NDArray[np.object_], /) -> NDArray[np.int64]:
        """Queries the index for the nearest item to each of the given search geometries"""
    def query(self, geoms: NDArray[np.object_], predicate: SupportsIndex, /) -> NDArray[np.int64]:
        """Queries the index for all items whose extents intersect the given search geometries, and optionally tests them against predicate function if provided."""
    def query_nearest(
        self, geoms: NDArray[np.object_], max_distance: float, exclusive: SupportsIndex, all_matches: SupportsIndex, /
    ) -> tuple[NDArray[np.int64], NDArray[np.float64]]:
        """Queries the index for all nearest item(s) to each of the given search geometries"""

class ShapelyError(Exception): ...
class GEOSException(ShapelyError): ...

def count_coordinates(geoms: NDArray[np.object_], /) -> int:
    """Counts the total amount of coordinates in a array with geometry objects"""

@overload
def get_coordinates(arr: NDArray[np.object_], include_z: bool, return_index: Literal[False], /) -> NDArray[np.float64]: ...
@overload
def get_coordinates(
    arr: NDArray[np.object_], include_z: bool, return_index: Literal[True], /
) -> tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    arr: NDArray[np.object_], include_z: bool, return_index: bool, /
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]:
    """Gets the coordinates as an (N, 2) shaped ndarray of floats"""

def set_coordinates(geoms: NDArray[np.object_], coords: NDArray[np.float64], /) -> NDArray[np.object_]:
    """Sets coordinates to a geometry array"""
