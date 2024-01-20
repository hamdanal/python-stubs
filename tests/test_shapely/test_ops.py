from __future__ import annotations

from types import NoneType
from typing import TYPE_CHECKING

import pyproj
import pytest
import shapely.ops
from shapely import GeometryCollection, LineString, MultiLineString, MultiPoint, Point, Polygon
from shapely.geometry.base import BaseGeometry, GeometrySequence
from typing_extensions import assert_type

from tests import check

if TYPE_CHECKING:
    from shapely.ops import _PolygonSequence  # noqa: F401

P = Point(1, 2)
LS = LineString([(0, 0), (1, 1)])
PO: Polygon = P.buffer(1)
MP = MultiPoint([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])


def test_polygonize() -> None:
    check(
        assert_type(shapely.ops.polygonize(PO), "_PolygonSequence"), GeometrySequence, dtype=Polygon
    )
    line_likes = [
        ((0, 0), (1, 1)),
        ((0, 0), (0, 1)),
        ((0, 1), (1, 1)),
        ((1, 1), (1, 0)),
        ((1, 0), (0, 0)),
    ]
    check(
        assert_type(shapely.ops.polygonize(line_likes), "_PolygonSequence"),
        GeometrySequence,
        dtype=Polygon,
    )
    lines = [
        LineString([(0, 0), (1, 1)]),
        LineString([(0, 0), (0, 1)]),
        LineString([(0, 1), (1, 1)]),
    ]
    poly = shapely.ops.polygonize(lines)
    check(assert_type(poly, "_PolygonSequence"), GeometrySequence, dtype=Polygon)
    check(assert_type(poly[0], Polygon), Polygon)
    check(assert_type(poly[:], GeometryCollection), GeometryCollection)
    check(assert_type(list(poly), list[Polygon]), list, dtype=Polygon)
    check(assert_type(len(poly), int), int)

    check(
        assert_type(
            shapely.ops.polygonize(
                (
                    LineString([(0, 0), (1, 1)]),
                    ((0, 1), (1, 1)),
                    ((1, 1), (1, 0)),
                    ((1, 0), (0, 0)),
                    None,
                )
            ),
            "_PolygonSequence",
        ),
        GeometrySequence,
        dtype=Polygon,
    )


def test_polygonize_full() -> None:
    expected_type = tuple[
        GeometryCollection, GeometryCollection, GeometryCollection, GeometryCollection
    ]
    check(
        assert_type(shapely.ops.polygonize_full(PO), expected_type), tuple, dtype=GeometryCollection
    )
    line_likes = [
        ((0, 0), (1, 1)),
        ((0, 0), (0, 1)),
        ((0, 1), (1, 1)),
        ((1, 1), (1, 0)),
        ((1, 0), (0, 0)),
    ]
    check(
        assert_type(shapely.ops.polygonize_full(line_likes), expected_type),
        tuple,
        dtype=GeometryCollection,
    )
    lines = [
        LineString([(0, 0), (1, 1)]),
        LineString([(0, 0), (0, 1)]),
        LineString([(0, 1), (1, 1)]),
    ]
    poly = shapely.ops.polygonize_full(lines)
    assert len(poly) == 4
    check(assert_type(poly, expected_type), tuple, dtype=GeometryCollection)

    check(
        assert_type(
            shapely.ops.polygonize_full(
                (
                    LineString([(0, 0), (1, 1)]),
                    ((0, 1), (1, 1)),
                    ((1, 1), (1, 0)),
                    ((1, 0), (0, 0)),
                    None,
                )
            ),
            expected_type,
        ),
        tuple,
        dtype=GeometryCollection,
    )


def test_line_merge() -> None:
    check(assert_type(shapely.ops.linemerge([LS]), LineString | MultiLineString), LineString)
    check(
        assert_type(shapely.ops.linemerge([LS], directed=True), LineString | MultiLineString),
        LineString,
    )
    check(
        assert_type(
            shapely.ops.linemerge(
                (LineString([(0, 0), (1, 1)]), ((0, 1), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (0, 0)))
            ),
            LineString | MultiLineString,
        ),
        MultiLineString,
    )


def test_unary_union() -> None:
    check(assert_type(shapely.ops.unary_union(P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.ops.unary_union(None), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.ops.unary_union([P]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.ops.unary_union([None]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.ops.unary_union([P, P]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.ops.unary_union([P, None]), BaseGeometry), BaseGeometry)


def test_triangulate() -> None:
    check(assert_type(shapely.ops.triangulate(MP), list[Polygon]), list, dtype=Polygon)
    check(assert_type(shapely.ops.triangulate(MP, edges=False), list[Polygon]), list, dtype=Polygon)
    check(
        assert_type(shapely.ops.triangulate(MP, edges=True), list[LineString]),
        list,
        dtype=LineString,
    )
    check(
        assert_type(shapely.ops.triangulate(MP, edges=bool("")), list[Polygon] | list[LineString]),
        list,
        dtype=LineString | Polygon,  # pyright: ignore[reportGeneralTypeIssues]  # TODO report to pyright
    )


def test_voronoi_diagram() -> None:
    regions = shapely.ops.voronoi_diagram(MP)
    check(assert_type(regions, GeometryCollection), GeometryCollection)
    check(list(regions.geoms), list, dtype=Polygon)
    edges = shapely.ops.voronoi_diagram(MP, edges=True)
    check(assert_type(edges, GeometryCollection), GeometryCollection)
    check(list(edges.geoms), list, dtype=MultiLineString)


def test_validate() -> None:
    check(assert_type(shapely.ops.validate(P), str), str)
    check(assert_type(shapely.ops.validate(None), None), NoneType)


def test_transform() -> None:
    def id_func(x: float, y: float, z: float | None = None) -> tuple[float, ...]:
        return tuple(filter(None, [x, y, z]))

    check(assert_type(shapely.ops.transform(id_func, P), Point), Point)
    check(assert_type(shapely.ops.transform(id_func, LS), LineString), LineString)

    def wrong_id_func(x: float, y: float, z: float) -> tuple[float, ...]:
        return x, y, z

    with pytest.raises(TypeError):
        shapely.ops.transform(wrong_id_func, P)  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]

    wgs84_pt = Point(-72.2495, 43.886)
    wgs84 = pyproj.CRS("EPSG:4326")
    utm = pyproj.CRS("EPSG:32618")
    project = pyproj.Transformer.from_crs(wgs84, utm, always_xy=True).transform
    check(assert_type(shapely.ops.transform(project, wgs84_pt), Point), Point)


def test_nearest_points() -> None:
    nearest = shapely.ops.nearest_points(PO, MP)
    check(assert_type(nearest, tuple[Point, Point]), tuple, dtype=Point)
    assert len(nearest) == 2


def test_snap() -> None:
    check(assert_type(shapely.ops.snap(LS, PO, 0.1), LineString), LineString)
    check(assert_type(shapely.ops.snap(P, PO, 0.1), Point), Point)
    check(assert_type(shapely.ops.snap(PO, PO, 0.1), Polygon), Polygon)
    check(assert_type(shapely.ops.snap(MP, PO, 0.1), MultiPoint), MultiPoint)


def test_shared_paths() -> None:
    shared = shapely.ops.shared_paths(LS, PO.exterior)
    check(assert_type(shared, GeometryCollection), GeometryCollection)
    with pytest.raises(Exception):
        shapely.ops.shared_paths(LS, PO)  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_split() -> None:
    check(assert_type(shapely.ops.split(LS, P), GeometryCollection), GeometryCollection)


def test_substring() -> None:
    check(assert_type(shapely.ops.substring(LS, 0.0, 1.2), LineString | Point), LineString)
    check(assert_type(shapely.ops.substring(LS, 0.2, 0.2), LineString | Point), Point)
    check(
        assert_type(shapely.ops.substring(LS, 0.0, 1.2, normalized=True), LineString | Point),
        LineString,
    )


def test_clip_by_rect() -> None:
    clipped_point = shapely.ops.clip_by_rect(P, 0, 0, 1, 1)
    check(assert_type(clipped_point, BaseGeometry), BaseGeometry)
    check(clipped_point, GeometryCollection)  # not point
    clipped_poly = shapely.ops.clip_by_rect(PO, 0.0, 0.0, 10.0, 10.0)
    check(assert_type(clipped_poly, BaseGeometry), BaseGeometry)
    check(clipped_poly, Polygon)


def test_orient() -> None:
    check(assert_type(shapely.ops.orient(P), Point), Point)
    check(assert_type(shapely.ops.orient(PO), Polygon), Polygon)
    check(
        assert_type(shapely.ops.orient(GeometryCollection(PO)), GeometryCollection),
        GeometryCollection,
    )
