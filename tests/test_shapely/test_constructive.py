from __future__ import annotations

from types import NoneType
from typing import Any

import numpy as np
import pytest
import shapely
from numpy.typing import NDArray
from shapely import (
    Geometry,
    GeometryCollection,
    LinearRing,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry
from typing_extensions import assert_type

from tests import check

BG = shapely.from_wkt("LINESTRING (1 2, 3 4, 5 6, 7 8)")
P = Point(1, 2)
P3 = Point(1, 2, 4)
LS = LineString([(1, 2), (3, 4), (5, 6), (7, 8)])
LR = LinearRing([(1, 2), (3, 4), (5, 6), (7, 8)])
PO = Polygon([P, P, P, P], holes=[[(0.1, 0.2), (0.3, 0.4), (0.5, 0.6), (0.7, 0.8)]])
MP = MultiPoint([P, P])
MLS = MultiLineString([LS, [P, P]])
MPO = MultiPolygon([PO, (LR,)])
GC = GeometryCollection([P, LS, PO])

GEOMS: list[Geometry] = [P, MP, LS, MLS, LR, PO, MPO, GC]


def test_boundary() -> None:
    check(assert_type(shapely.boundary(P), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.boundary(MP), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.boundary(LS), MultiPoint), MultiPoint)
    check(assert_type(shapely.boundary(MLS), MultiPoint), MultiPoint)
    check(assert_type(shapely.boundary(LR), MultiPoint), MultiPoint)
    check(assert_type(shapely.boundary(PO), MultiLineString), MultiLineString)
    check(assert_type(shapely.boundary(MPO), MultiLineString), MultiLineString)
    check(assert_type(shapely.boundary(GC), None), NoneType)
    check(assert_type(shapely.boundary(None), None), NoneType)
    check(assert_type(shapely.boundary(BG), BaseMultipartGeometry | Any), MultiPoint)
    check(
        assert_type(shapely.boundary([P]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.boundary((P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )


def test_buffer() -> None:
    check(assert_type(shapely.buffer(None, 1.0), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.buffer(geom, 1.0), Polygon), Polygon)

    check(assert_type(shapely.buffer(P, [1.0]), NDArray[np.object_]), np.ndarray, dtype=Polygon)
    check(assert_type(shapely.buffer(None, [1.0]), NDArray[np.object_]), np.ndarray)
    check(assert_type(shapely.buffer([P], 1.0), NDArray[np.object_]), np.ndarray, dtype=Polygon)
    check(assert_type(shapely.buffer([None], 1.0), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.buffer((P, None), 1.0), NDArray[np.object_]), np.ndarray, dtype=Polygon
    )
    check(assert_type(shapely.buffer([P], [1.0]), NDArray[np.object_]), np.ndarray, dtype=Polygon)


def test_offset_curve() -> None:
    check(assert_type(shapely.offset_curve(None, 1.0), None), NoneType)
    for geom in GEOMS:
        check(
            assert_type(shapely.offset_curve(geom, 1.0), LineString | MultiLineString),
            LineString | MultiLineString,
        )
    check(
        assert_type(shapely.offset_curve([LS], 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )


def test_centroid() -> None:
    check(assert_type(shapely.centroid(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.centroid(geom), Point), Point)
    check(assert_type(shapely.centroid([P]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.centroid((P, None)), NDArray[np.object_]), np.ndarray, dtype=Point)


def test_clip_by_rect() -> None:
    check(assert_type(shapely.clip_by_rect(None, 0.0, 0, 2, 3.0), None), NoneType)
    check(assert_type(shapely.clip_by_rect(P, 0.0, 0, 2, 3.0), BaseGeometry), Point)
    check(assert_type(shapely.clip_by_rect(P, 0.0, 0, 2, 1.0), BaseGeometry), GeometryCollection)
    check(
        assert_type(shapely.clip_by_rect([P], 0.0, 0, 2, 3.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.clip_by_rect((P, None), 0.0, 0, 2, 3.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )


def test_concave_hull() -> None:
    check(assert_type(shapely.concave_hull(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.concave_hull(geom), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.concave_hull([P]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.concave_hull([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.concave_hull((P, None)), NDArray[np.object_]), np.ndarray, dtype=Point
    )


def test_convex_hull() -> None:
    check(assert_type(shapely.convex_hull(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.convex_hull(geom), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.convex_hull([P]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(assert_type(shapely.convex_hull([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.convex_hull((P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_delaunay_triangles() -> None:
    check(assert_type(shapely.delaunay_triangles(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.delaunay_triangles(geom), GeometryCollection), GeometryCollection)
        check(
            assert_type(shapely.delaunay_triangles(geom, only_edges=True), MultiLineString),
            MultiLineString,
        )
        check(
            assert_type(shapely.delaunay_triangles(geom, 0.0, True), MultiLineString),
            MultiLineString,
        )
        check(
            assert_type(
                shapely.delaunay_triangles(geom, only_edges=bool(0.5)),
                GeometryCollection | MultiLineString,
            ),
            MultiLineString,
        )
    check(
        assert_type(shapely.delaunay_triangles([P]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.delaunay_triangles(P, [0.0]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.delaunay_triangles(P, only_edges=[False]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(assert_type(shapely.delaunay_triangles([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.delaunay_triangles((P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )


def test_envelope() -> None:
    check(assert_type(shapely.envelope(None), None), NoneType)
    check(assert_type(shapely.envelope(P), Point), Point)
    for geom in GEOMS:
        check(assert_type(shapely.envelope(geom), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.envelope([P]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(shapely.envelope([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.envelope((P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_extract_unique_points() -> None:
    check(assert_type(shapely.extract_unique_points(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.extract_unique_points(geom), MultiPoint), MultiPoint)
    check(
        assert_type(shapely.extract_unique_points([P]), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiPoint,
    )
    check(assert_type(shapely.extract_unique_points([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.extract_unique_points((P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiPoint,
    )


def test_build_area() -> None:
    check(assert_type(shapely.build_area(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.build_area(geom), BaseGeometry), GeometryCollection)
    # It doesn't always return a GeometryCollection
    check(
        assert_type(shapely.build_area(GeometryCollection([PO, P.buffer(3)])), BaseGeometry),
        Polygon,
    )
    check(
        assert_type(shapely.build_area([P]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(assert_type(shapely.build_area([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.build_area((P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )


def test_make_valid() -> None:
    check(assert_type(shapely.make_valid(None), None), NoneType)
    for geom in GEOMS:
        if isinstance(geom, LinearRing):
            continue
        check(assert_type(shapely.make_valid(geom), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.make_valid([P]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.make_valid([None]), NDArray[np.object_]), np.ndarray)
    check(assert_type(shapely.make_valid((P, None)), NDArray[np.object_]), np.ndarray, dtype=Point)


def test_normalize() -> None:
    check(assert_type(shapely.normalize(None), None), NoneType)
    check(assert_type(shapely.normalize(P), Point), Point)
    check(assert_type(shapely.normalize(LS), LineString), LineString)
    check(assert_type(shapely.normalize([P]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.normalize([None]), NDArray[np.object_]), np.ndarray)
    check(assert_type(shapely.normalize((P, None)), NDArray[np.object_]), np.ndarray, dtype=Point)


def test_point_on_surface() -> None:
    check(assert_type(shapely.point_on_surface(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.point_on_surface(geom), Point), Point)
    check(assert_type(shapely.point_on_surface([BG]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(
        assert_type(shapely.point_on_surface([None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.point_on_surface((BG, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )


def test_node() -> None:
    check(assert_type(shapely.node(None), None), NoneType)
    for geom in GEOMS:
        check(assert_type(shapely.node(geom), MultiLineString), MultiLineString)
    check(assert_type(shapely.node([BG]), NDArray[np.object_]), np.ndarray, dtype=MultiLineString)
    check(assert_type(shapely.node([None]), NDArray[np.object_]), np.ndarray, dtype=NoneType)
    check(
        assert_type(shapely.node((BG, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiLineString,
    )


def test_polygonize() -> None:
    check(assert_type(shapely.polygonize([P, LS]), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.polygonize((LS, None)), GeometryCollection), GeometryCollection)
    check(
        assert_type(shapely.polygonize([(LS, None)]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(
            shapely.polygonize(np.array([P, LS])), GeometryCollection | NDArray[np.object_]
        ),
        GeometryCollection,
    )
    check(
        assert_type(
            shapely.polygonize(np.array([[P, LS]])), GeometryCollection | NDArray[np.object_]
        ),
        np.ndarray,
        dtype=GeometryCollection,
    )
    with pytest.raises(Exception):
        shapely.polygonize(LS)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_polygonize_full() -> None:
    FourCollections = tuple[
        GeometryCollection, GeometryCollection, GeometryCollection, GeometryCollection
    ]
    FourArrays = tuple[
        NDArray[np.object_], NDArray[np.object_], NDArray[np.object_], NDArray[np.object_]
    ]
    check(
        assert_type(shapely.polygonize_full([P, LS]), FourCollections),
        tuple,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.polygonize_full((LS, None)), FourCollections),
        tuple,
        dtype=GeometryCollection,
    )
    check(assert_type(shapely.polygonize_full([(LS, None)]), FourArrays), tuple, dtype=np.ndarray)
    check(
        assert_type(shapely.polygonize_full(np.array([P, LS])), FourCollections | FourArrays),
        tuple,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.polygonize_full(np.array([[P, LS]])), FourCollections | FourArrays),
        tuple,
        dtype=np.ndarray,
    )
    with pytest.raises(Exception):
        shapely.polygonize_full(LS)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_remove_repeated_points() -> None:
    check(assert_type(shapely.remove_repeated_points(None), None), NoneType)
    check(assert_type(shapely.remove_repeated_points(P), Point), Point)
    check(assert_type(shapely.remove_repeated_points(MP), MultiPoint), MultiPoint)
    check(assert_type(shapely.remove_repeated_points(LS), LineString), LineString)
    check(assert_type(shapely.remove_repeated_points(MLS), MultiLineString), MultiLineString)
    check(assert_type(shapely.remove_repeated_points(LR), LinearRing), LinearRing)
    check(assert_type(shapely.remove_repeated_points(PO), Polygon), Polygon)
    check(assert_type(shapely.remove_repeated_points(MPO), MultiPolygon), MultiPolygon)
    check(assert_type(shapely.remove_repeated_points(GC), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.remove_repeated_points(BG), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.remove_repeated_points([LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )
    check(
        assert_type(shapely.remove_repeated_points([None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.remove_repeated_points((LS, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )


def test_reverse() -> None:
    check(assert_type(shapely.reverse(None), None), NoneType)
    check(assert_type(shapely.reverse(P), Point), Point)
    check(assert_type(shapely.reverse(LS), LineString), LineString)
    check(assert_type(shapely.reverse([P]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.reverse((P, None)), NDArray[np.object_]), np.ndarray, dtype=Point)


def test_segmentize() -> None:
    check(assert_type(shapely.segmentize(None, 1.0), None), NoneType)
    check(assert_type(shapely.segmentize(P, 1.0), Point), Point)
    check(assert_type(shapely.segmentize(LS, 1.0), LineString), LineString)
    check(assert_type(shapely.segmentize(P, [1.0]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.segmentize([P], 1.0), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(
        assert_type(shapely.segmentize((P, None), 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.segmentize((P, None), [1.0, 0.1]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )


def test_simplify() -> None:
    check(assert_type(shapely.simplify(None, 0.0), None), NoneType)
    check(assert_type(shapely.simplify(P, 0.0), Point), Point)
    check(assert_type(shapely.simplify(LS, 0.0), LineString), LineString)
    check(assert_type(shapely.simplify(PO, 0.0), Polygon), Polygon)
    check(assert_type(shapely.simplify(MLS, 0.0), MultiLineString), MultiLineString)
    check(assert_type(shapely.simplify(GC, 0.0), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.simplify(P, [0.0]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.simplify([P], 0.0), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(
        assert_type(shapely.simplify((P, None), 0.0), NDArray[np.object_]), np.ndarray, dtype=Point
    )
    check(
        assert_type(shapely.simplify((P, None), [0.0, 0.1]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )


def test_snap() -> None:
    check(assert_type(shapely.snap(None, LS, 0.0), None), NoneType)
    check(assert_type(shapely.snap(P, None, 0.0), None), NoneType)
    check(assert_type(shapely.snap(P, LS, 0.0), Point), Point)
    check(assert_type(shapely.snap(LS, P, 0.0), LineString), LineString)
    check(assert_type(shapely.snap(PO, LS, 0.0), Polygon), Polygon)
    check(assert_type(shapely.snap(MLS, LS, 0.0), MultiLineString), MultiLineString)
    check(assert_type(shapely.snap(GC, LS, 0.0), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.snap(P, LS, [0.0]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.snap(P, [LS], 0.0), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(shapely.snap([P], LS, 0.0), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(
        assert_type(shapely.snap((P, None), LS, 0.0), NDArray[np.object_]), np.ndarray, dtype=Point
    )
    check(
        assert_type(shapely.snap((P, None), LS, [0.0, 0.1]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.snap((P, None), [LS, P], 0.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.snap((P, None), [LS, P], [0.0, 0.1]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )


def test_voronoi_polygons() -> None:
    check(assert_type(shapely.voronoi_polygons(None), None), NoneType)
    for geom in (LS, MLS, LR, PO, MPO, GC):
        check(assert_type(shapely.voronoi_polygons(geom), GeometryCollection), GeometryCollection)
        check(
            assert_type(
                shapely.voronoi_polygons(geom, only_edges=True), LineString | MultiLineString
            ),
            LineString | MultiLineString,
        )
        check(
            assert_type(
                shapely.voronoi_polygons(geom, 0.0, LS, True), LineString | MultiLineString
            ),
            LineString | MultiLineString,
        )
        check(
            assert_type(
                shapely.voronoi_polygons(geom, only_edges=bool(0.5)),
                GeometryCollection | LineString | MultiLineString,
            ),
            LineString | MultiLineString,
        )
    check(
        assert_type(shapely.voronoi_polygons([LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.voronoi_polygons(LS, [0.0]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.voronoi_polygons(LS, 0.0, [LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.voronoi_polygons(LS, extend_to=[LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.voronoi_polygons(LS, 0.0, None, [False]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.voronoi_polygons(LS, only_edges=[False]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(assert_type(shapely.voronoi_polygons([None]), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.voronoi_polygons((LS, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )


def test_oriented_envelope() -> None:
    check(assert_type(shapely.oriented_envelope(P), Point), Point)
    for geom in GEOMS:
        check(assert_type(shapely.oriented_envelope(geom), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.oriented_envelope(None), None), NoneType)
    check(
        assert_type(shapely.oriented_envelope([LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.oriented_envelope([None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.oriented_envelope((LS, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_minimum_bounding_circle() -> None:
    check(assert_type(shapely.minimum_bounding_circle(P), Point), Point)
    check(assert_type(shapely.minimum_bounding_circle(MP), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(LS), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(MLS), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(LR), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(PO), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(MPO), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(GC), Polygon), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(BG), Polygon | Point), Polygon)
    check(assert_type(shapely.minimum_bounding_circle(None), None), NoneType)
    check(
        assert_type(shapely.minimum_bounding_circle([LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(shapely.minimum_bounding_circle([None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.minimum_bounding_circle((LS, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
