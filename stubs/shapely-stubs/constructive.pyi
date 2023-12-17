from _typeshed import Incomplete
from typing import Literal

from numpy.typing import ArrayLike

from shapely._enum import ParamEnum

__all__ = [
    "BufferCapStyle",
    "BufferJoinStyle",
    "boundary",
    "buffer",
    "offset_curve",
    "centroid",
    "clip_by_rect",
    "concave_hull",
    "convex_hull",
    "delaunay_triangles",
    "segmentize",
    "envelope",
    "extract_unique_points",
    "build_area",
    "make_valid",
    "normalize",
    "node",
    "point_on_surface",
    "polygonize",
    "polygonize_full",
    "remove_repeated_points",
    "reverse",
    "simplify",
    "snap",
    "voronoi_polygons",
    "oriented_envelope",
    "minimum_rotated_rectangle",
    "minimum_bounding_circle",
]

class BufferCapStyle(ParamEnum):
    round: int
    flat: int
    square: int

class BufferJoinStyle(ParamEnum):
    round: int
    mitre: int
    bevel: int

def boundary(geometry, **kwargs): ...
def buffer(
    geometry,
    distance: float | ArrayLike,
    quad_segs: int = 8,
    cap_style: BufferJoinStyle | Literal["round", "square", "flat"] = "round",
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    single_sided: bool = False,
    **kwargs,
): ...
def offset_curve(geometry, distance, quad_segs: int = 8, join_style: str = "round", mitre_limit: float = 5.0, **kwargs): ...
def centroid(geometry, **kwargs): ...
def clip_by_rect(geometry, xmin: float, ymin: float, xmax: float, ymax: float, **kwargs): ...
def concave_hull(geometry, ratio: float = 0.0, allow_holes: bool = False, **kwargs): ...
def convex_hull(geometry, **kwargs): ...
def delaunay_triangles(geometry, tolerance: float = 0.0, only_edges: bool = False, **kwargs): ...
def envelope(geometry, **kwargs): ...
def extract_unique_points(geometry, **kwargs): ...
def build_area(geometry, **kwargs): ...
def make_valid(geometry, **kwargs): ...
def normalize(geometry, **kwargs): ...
def point_on_surface(geometry, **kwargs): ...
def node(geometry, **kwargs): ...
def polygonize(geometries, **kwargs): ...
def polygonize_full(geometries, **kwargs): ...
def remove_repeated_points(geometry, tolerance: float = 0.0, **kwargs): ...
def reverse(geometry, **kwargs): ...
def segmentize(geometry, max_segment_length, **kwargs): ...
def simplify(geometry, tolerance, preserve_topology: bool = True, **kwargs): ...
def snap(geometry, reference, tolerance, **kwargs): ...
def voronoi_polygons(
    geometry, tolerance: float = 0.0, extend_to: Incomplete | None = None, only_edges: bool = False, **kwargs
): ...
def oriented_envelope(geometry, **kwargs): ...

minimum_rotated_rectangle = oriented_envelope

def minimum_bounding_circle(geometry, **kwargs): ...
