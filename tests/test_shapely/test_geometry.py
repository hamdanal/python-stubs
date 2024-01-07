from __future__ import annotations

from array import array
from collections.abc import Iterator
from types import NoneType
from typing import Any

import numpy as np
import pytest
import shapely
from numpy.typing import NDArray
from shapely import (
    GeometryCollection,
    LinearRing,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.coords import CoordinateSequence
from shapely.geometry.base import BaseGeometry, GeometrySequence
from shapely.geometry.geo import box, mapping, shape
from shapely.geometry.polygon import InteriorRingSequence
from typing_extensions import assert_never, assert_type

from tests import check

BG: BaseGeometry = shapely.from_wkt("LINESTRING (1 2, 3 4, 5 6, 7 8)")
P = Point(1, 2)
P3 = Point(1, 2, 4)
LS = LineString([(1, 2), (3, 4), (5, 6), (7, 8)])
LR = LinearRing([(1, 2), (3, 4), (5, 6), (7, 8)])
PO = Polygon([P, P, P, P], holes=[[(0.1, 0.2), (0.3, 0.4), (0.5, 0.6), (0.7, 0.8)]])
MP = MultiPoint([P, P])
MLS = MultiLineString([LS, [P, P]])
MPO = MultiPolygon([PO, (LR,)])
GC = GeometryCollection([P, LS, PO])


class HasArray:
    def __init__(self, array: np.ndarray[Any, Any]) -> None:
        self.array = array

    def __array__(self) -> np.ndarray[Any, Any]:
        return self.array


def test_base_geometry_constructor() -> None:
    with pytest.warns(FutureWarning):
        check(assert_type(BaseGeometry(), GeometryCollection), GeometryCollection)


def test_geometry_operators() -> None:
    check(assert_type(BG & P, BaseGeometry), BaseGeometry)
    check(assert_type(BG & None, None), NoneType)
    check(assert_type(BG & [P, None], NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(BG | P, BaseGeometry), BaseGeometry)
    check(assert_type(BG | None, None), NoneType)
    check(assert_type(BG | [P, None], NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(BG - P, BaseGeometry), BaseGeometry)
    check(assert_type(BG - None, None), NoneType)
    check(assert_type(BG - [P, None], NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(BG ^ P, BaseGeometry), BaseGeometry)
    check(assert_type(BG ^ None, None), NoneType)
    check(assert_type(BG ^ [P, None], NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(BG == P, bool), bool)
    check(assert_type(BG != P, bool), bool)
    _ = {BG}  # testing hash


def test_geometry_coordinate_access() -> None:
    check(assert_type(BG.coords, CoordinateSequence), CoordinateSequence)
    check(assert_type(BG.xy, tuple["array[float]", "array[float]"]), tuple, array)
    check(assert_type(BG.__geo_interface__, dict[str, Any]), dict, str)


def test_geometry_type_and_repr() -> None:
    check(assert_type(BG.wkt, str), str)
    check(assert_type(BG.wkb, bytes), bytes)
    check(assert_type(BG.wkb_hex, str), str)
    check(assert_type(BG.geom_type, str), str)
    check(assert_type(BG.svg(), str), str)
    check(assert_type(BG._repr_svg_(), str), str)


def test_geometry_real_values() -> None:
    check(assert_type(BG.area, float), float)
    check(assert_type(BG.distance(P), float), float)
    check(assert_type(BG.distance(None), float), float)
    check(assert_type(BG.distance([[P, None]]), NDArray[np.float64]), np.ndarray, dtype=np.float64)
    check(assert_type(BG.hausdorff_distance(P), float), float)
    check(assert_type(BG.hausdorff_distance(None), float), float)
    check(
        assert_type(BG.hausdorff_distance([[P, None]]), NDArray[np.float64]),
        np.ndarray,
        dtype=np.float64,
    )
    check(assert_type(BG.length, float), float)
    check(assert_type(BG.minimum_clearance, float), float)


def test_geometry_topology() -> None:
    check(assert_type(BG.boundary, BaseGeometry), BaseGeometry)
    check(assert_type(BG.bounds, tuple[float, float, float, float]), tuple, dtype=float)
    check(assert_type(BG.centroid, Point), Point)
    check(assert_type(BG.point_on_surface(), Point), Point)
    check(assert_type(BG.representative_point(), Point), Point)
    check(assert_type(BG.convex_hull, BaseGeometry), BaseGeometry)
    check(assert_type(BG.envelope, BaseGeometry), BaseGeometry)
    check(assert_type(BG.oriented_envelope, BaseGeometry), BaseGeometry)
    check(assert_type(BG.minimum_rotated_rectangle, BaseGeometry), BaseGeometry)
    check(assert_type(BG.buffer(1.5), BaseGeometry), BaseGeometry)
    check(assert_type(BG.simplify(1.5), BaseGeometry), BaseGeometry)
    check(assert_type(BG.normalize(), BaseGeometry), BaseGeometry)


def test_geometry_overlay() -> None:
    check(assert_type(BG.difference(P), BaseGeometry), BaseGeometry)
    check(assert_type(BG.difference(None), None), NoneType)
    check(
        assert_type(BG.difference([P, None]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(assert_type(BG.intersection(P), BaseGeometry), BaseGeometry)
    check(assert_type(BG.intersection(None), None), NoneType)
    check(
        assert_type(BG.intersection([P, None]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(assert_type(BG.symmetric_difference(P), BaseGeometry), BaseGeometry)
    check(assert_type(BG.symmetric_difference(None), None), NoneType)
    check(
        assert_type(BG.symmetric_difference([P, None]), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(assert_type(BG.union(P), BaseGeometry), BaseGeometry)
    check(assert_type(BG.union(None), None), NoneType)
    check(assert_type(BG.union([P, None]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)


def test_geometry_unary_predicates() -> None:
    check(assert_type(BG.has_z, bool), bool)
    check(assert_type(BG.is_empty, bool), bool)
    check(assert_type(BG.is_ring, bool), bool)
    check(assert_type(BG.is_closed, bool), bool)
    check(assert_type(BG.is_simple, bool), bool)
    check(assert_type(BG.is_valid, bool), bool)


def test_geometry_binary_predicates() -> None:
    check(assert_type(BG.relate(P), str), str)
    check(assert_type(BG.relate(None), None), NoneType)
    check(assert_type(BG.relate([P, None]), NDArray[np.str_]), np.ndarray, dtype=str)
    check(assert_type(BG.covers(P), bool), bool)
    check(assert_type(BG.covers(None), bool), bool)
    check(assert_type(BG.covers([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.covered_by(P), bool), bool)
    check(assert_type(BG.covered_by(None), bool), bool)
    check(assert_type(BG.covered_by([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.contains(P), bool), bool)
    check(assert_type(BG.contains(None), bool), bool)
    check(assert_type(BG.contains([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.contains_properly(P), bool), bool)
    check(assert_type(BG.contains_properly(None), bool), bool)
    check(
        assert_type(BG.contains_properly([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_
    )
    check(assert_type(BG.crosses(P), bool), bool)
    check(assert_type(BG.crosses(None), bool), bool)
    check(assert_type(BG.crosses([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.disjoint(P), bool), bool)
    check(assert_type(BG.disjoint(None), bool), bool)
    check(assert_type(BG.disjoint([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.equals(P), bool), bool)
    check(assert_type(BG.equals(None), bool), bool)
    check(assert_type(BG.equals([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.intersects(P), bool), bool)
    check(assert_type(BG.intersects(None), bool), bool)
    check(assert_type(BG.intersects([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.overlaps(P), bool), bool)
    check(assert_type(BG.overlaps(None), bool), bool)
    check(assert_type(BG.overlaps([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.touches(P), bool), bool)
    check(assert_type(BG.touches(None), bool), bool)
    check(assert_type(BG.touches([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.within(P), bool), bool)
    check(assert_type(BG.within(None), bool), bool)
    check(assert_type(BG.within([P, None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.dwithin(P, 1.5), bool), bool)
    check(assert_type(BG.dwithin(None, 1.5), bool), bool)
    check(assert_type(BG.dwithin([P, None], 1.5), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.dwithin(P, [1.5]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.dwithin(None, [1.5]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.dwithin([P, None], [1.5]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.equals_exact(P, 1.5), bool), bool)
    check(assert_type(BG.equals_exact(None, 1.5), bool), bool)
    check(
        assert_type(BG.equals_exact([P, None], 1.5), NDArray[np.bool_]), np.ndarray, dtype=np.bool_
    )
    check(assert_type(BG.equals_exact(P, [1.5]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(BG.equals_exact(None, [1.5]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(
        assert_type(BG.equals_exact([P, None], [1.5]), NDArray[np.bool_]),
        np.ndarray,
        dtype=np.bool_,
    )
    with pytest.warns(FutureWarning):
        check(assert_type(BG.almost_equals(P, 1), bool | NDArray[np.bool_]), bool)  # pyright: ignore[reportDeprecated]
    with pytest.warns(FutureWarning):
        check(assert_type(BG.almost_equals(None, 1), bool | NDArray[np.bool_]), bool)  # pyright: ignore[reportDeprecated]
    with pytest.warns(FutureWarning):
        check(assert_type(BG.almost_equals([P, None], 1), bool | NDArray[np.bool_]), np.ndarray)  # pyright: ignore[reportDeprecated]
    p = "T*F**F***"
    check(assert_type(BG.relate_pattern(P, p), bool), bool)
    check(assert_type(BG.relate_pattern(None, p), bool), bool)
    check(
        assert_type(BG.relate_pattern([P, None], p), NDArray[np.bool_]), np.ndarray, dtype=np.bool_
    )


def test_geometry_linear_referencing() -> None:
    check(assert_type(BG.line_locate_point(P), float), float)
    check(assert_type(BG.line_locate_point(None), float), float)
    check(
        assert_type(BG.line_locate_point([P, None]), NDArray[np.float64]), np.ndarray, dtype=float
    )
    check(assert_type(BG.project(P), float), float)
    check(assert_type(BG.project(None), float), float)
    check(assert_type(BG.project([P, None]), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(BG.line_interpolate_point(1.5), Point), Point)
    check(
        assert_type(BG.line_interpolate_point([1.5]), NDArray[np.object_]), np.ndarray, dtype=Point
    )
    check(assert_type(BG.interpolate(1.5), Point), Point)
    check(assert_type(BG.interpolate([1.5]), NDArray[np.object_]), np.ndarray, dtype=Point)
    check(assert_type(BG.segmentize(1.5), BaseGeometry), BaseGeometry)
    check(assert_type(BG.segmentize([1.5]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(BG.reverse(), BaseGeometry), BaseGeometry)  # returns Self
    check(assert_type(P.reverse(), Point), Point)
    check(assert_type(LS.reverse(), LineString), LineString)


def test_multipart_geometry() -> None:
    with pytest.raises(NotImplementedError):
        assert_never(MLS.coords)

    check(assert_type(MP.geoms, "GeometrySequence[MultiPoint]"), GeometrySequence, Point)
    check(assert_type(MLS.geoms, "GeometrySequence[MultiLineString]"), GeometrySequence, LineString)
    check(assert_type(MPO.geoms, "GeometrySequence[MultiPolygon]"), GeometrySequence, Polygon)
    check(
        assert_type(GC.geoms, "GeometrySequence[GeometryCollection]"),
        GeometrySequence,
        BaseGeometry,
    )
    check(assert_type(iter(MP.geoms), Iterator[Point]), Iterator, dtype=Point)
    # TODO: mypy does not correctly handle the next 3 lines
    check(assert_type(iter(MLS.geoms), Iterator[LineString]), Iterator, dtype=LineString)  # type: ignore[assert-type]
    check(assert_type(iter(MPO.geoms), Iterator[Polygon]), Iterator, dtype=Polygon)  # type: ignore[assert-type]
    check(assert_type(iter(GC.geoms), Iterator[BaseGeometry]), Iterator, dtype=BaseGeometry)  # type: ignore[assert-type]
    check(assert_type(MP.geoms[0], Point), Point)
    check(assert_type(MLS.geoms[0], LineString), LineString)
    check(assert_type(MPO.geoms[0], Polygon), Polygon)
    check(assert_type(GC.geoms[0], BaseGeometry), BaseGeometry)
    check(assert_type(MP.geoms[:], MultiPoint), MultiPoint)
    check(assert_type(MLS.geoms[:], MultiLineString), MultiLineString)
    check(assert_type(MPO.geoms[:], MultiPolygon), MultiPolygon)
    check(assert_type(GC.geoms[:], GeometryCollection), GeometryCollection)
    _ = len(MLS.geoms)  # testing geoms len

    _ = {MLS}  # testing hash


def test_point() -> None:
    # Test constructor
    Point()
    Point(1.0, 2)
    Point(1, 2, 3.5)
    Point(P)
    Point((1, 2))
    Point([1, 2])
    Point(np.array([1, 2]))
    Point(range(2))
    Point(float(i) for i in range(2))

    with pytest.raises(TypeError):
        Point(1)  # type: ignore # pyright: ignore
    with pytest.raises(TypeError):
        Point(1, 2, 3, 4)  # type: ignore # pyright: ignore

    # Test new attributes
    check(assert_type(P.x, float), float)
    check(assert_type(P.y, float), float)
    check(assert_type(P3.z, float), float)

    # Test BaseGeometry overrides
    check(assert_type(P.boundary, GeometryCollection), GeometryCollection)
    check(assert_type(P.convex_hull, Point), Point)
    check(assert_type(P.envelope, Point), Point)
    check(assert_type(P.oriented_envelope, Point), Point)
    check(assert_type(P.minimum_rotated_rectangle, Point), Point)
    check(assert_type(P.buffer(1), Polygon), Polygon)


def test_linestring() -> None:
    # Test constructor
    LineString()
    LineString([(1, 2), (3, 4)])
    LineString([P, P])
    LineString(LS)
    LineString(LR)
    LineString(np.array([[1, 2], [3, 4]]))
    LineString(HasArray(np.array([[1, 2], [3, 4]])))

    with pytest.raises(TypeError):
        LineString(1)  # type: ignore # pyright: ignore
    with pytest.raises(TypeError):
        LineString(P)  # type: ignore # pyright: ignore
    with pytest.raises(TypeError):
        LineString([P, LS])  # type: ignore # pyright: ignore

    # Test new attributes
    check(assert_type(LS.offset_curve(1.5), LineString | MultiLineString), LineString)
    check(assert_type(LS.parallel_offset(1.5), LineString | MultiLineString), LineString)

    # Test BaseGeometry overrides
    check(assert_type(LS.boundary, MultiPoint), MultiPoint)
    check(assert_type(LS.convex_hull, LineString), LineString)
    check(assert_type(LS.envelope, Polygon), Polygon)
    check(assert_type(LS.oriented_envelope, LineString), LineString)
    check(assert_type(LS.minimum_rotated_rectangle, LineString), LineString)
    check(assert_type(LS.buffer(1), Polygon), Polygon)


def test_linearring() -> None:
    # Test constructor
    coords = [(1, 2), (3, 4), (1, 2), (3, 4)]
    LinearRing()
    LinearRing(coords)
    LinearRing([P, P, P, P])
    LinearRing(LS)
    LinearRing(LR)
    LinearRing(np.array(coords))
    LinearRing(HasArray(np.array(coords)))

    with pytest.raises(TypeError):
        LinearRing(1)  # type: ignore # pyright: ignore
    with pytest.raises(TypeError):
        LinearRing(P)  # type: ignore # pyright: ignore
    with pytest.raises(TypeError):
        LinearRing([P, LR])  # type: ignore # pyright: ignore

    # Test new attributes
    check(assert_type(LR.offset_curve(1.5), LineString | MultiLineString), LineString)
    check(assert_type(LR.parallel_offset(1.5), LineString | MultiLineString), LineString)
    check(assert_type(LR.is_ccw, bool), bool)
    check(assert_type(LR.is_simple, bool), bool)

    # Test BaseGeometry overrides
    check(assert_type(LR.boundary, MultiPoint), MultiPoint)
    check(assert_type(LR.convex_hull, LineString), LineString)
    check(assert_type(LR.envelope, Polygon), Polygon)
    check(assert_type(LR.oriented_envelope, LineString), LineString)
    check(assert_type(LR.minimum_rotated_rectangle, LineString), LineString)
    check(assert_type(LR.buffer(1), Polygon), Polygon)


def test_polygon() -> None:
    # Test constructor
    coords = [(1, 2), (3, 4), (1, 2), (3, 4)]
    Polygon()
    Polygon(PO)
    Polygon([P, P, P, P])
    Polygon(np.array(coords))

    with pytest.raises(TypeError):
        Polygon(1.0, 2)  # type: ignore # pyright: ignore
    with pytest.raises(TypeError):
        Polygon(1, 2, 3, 4)  # type: ignore # pyright: ignore

    # Test new attributes
    check(assert_type(PO.exterior, LinearRing), LinearRing)
    check(assert_type(PO.interiors, list[LinearRing] | InteriorRingSequence), InteriorRingSequence)
    check(
        assert_type(Polygon().interiors, list[LinearRing] | InteriorRingSequence), list
    )  # empty polygon returns an empty list
    check(assert_type(next(iter(PO.interiors)), LinearRing), LinearRing)
    check(assert_type(PO.interiors[0], LinearRing), LinearRing)
    check(assert_type(PO.interiors[:], list[LinearRing]), list, dtype=LinearRing)

    # Test BaseGeometry overrides
    with pytest.raises(NotImplementedError):
        assert_never(PO.coords)


def test_multipoint() -> None:
    MultiPoint()
    MultiPoint(None)
    MultiPoint(MP)
    MultiPoint([P, P])
    l_: list[Point | tuple[float, float] | list[float]] = [P, (1, 2), [1, 2]]
    MultiPoint(l_)
    t: tuple[Point | tuple[float, float] | list[float], ...] = (P, (1, 2), [1, 2])
    MultiPoint(t)
    with pytest.raises(TypeError):
        MultiPoint(o for o in [LS, LS, LS])  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPoint(BG)  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPoint((PO,))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPoint((None,))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPoint((P, PO, None))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_multilinestring() -> None:
    MultiLineString()
    MultiLineString(None)
    MultiLineString(MLS)
    l_: list[LineString | list[Point]] = [LS, LS, LS, [P, P]]
    MultiLineString(l_)
    t: tuple[LineString | list[Point], ...] = (LS, LS, LS, [P, P])
    MultiLineString(t)
    with pytest.raises(TypeError):
        MultiLineString(o for o in [LS, LS, LS])  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiLineString(BG)  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiLineString((PO,))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(shapely.errors.ShapelyError):
        MultiLineString((None,))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiLineString((P, PO, None))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_multipolygon() -> None:
    MultiPolygon()
    MultiPolygon(None)
    MultiPolygon([PO])
    MultiPolygon([PO, None])
    MultiPolygon((None,))
    l_: list[Polygon | tuple[LineString]] = [PO, (LS,)]
    MultiPolygon(l_)
    t: tuple[Polygon, None] = (PO, None)
    MultiPolygon(t)
    with pytest.raises(TypeError):
        MultiPolygon(o for o in [LS, LS, LS])  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPolygon(BG)  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPolygon((MLS,))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(TypeError):
        MultiPolygon((P, PO, None))  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_geometry_collection() -> None:
    GeometryCollection(None)
    GeometryCollection(BG)
    GeometryCollection([BG])
    GeometryCollection([None])
    GeometryCollection([P, PO, None])
    with pytest.raises(TypeError):
        GeometryCollection(o for o in [P, PO, None])  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_geo() -> None:
    check(assert_type(box(0.0, 0, 1.0, 1), Polygon), Polygon)
    check(assert_type(box(0, 0.0, 1, 1.0, ccw=False), Polygon), Polygon)
    check(assert_type(box(0, 0.0, 1, 1.0, ccw=bool(1)), Polygon), Polygon)

    class ImplementsGeoInterfaceRW:
        __geo_interface__ = {"type": "Point", "coordinates": (1.0, 2.0)}

    class ImplementsGeoInterfaceRO:
        @property
        def __geo_interface__(self) -> dict[str, object]:
            return {"type": "Point", "coordinates": (1.0, 2.0)}

    check(assert_type(mapping(BG), dict[str, Any]), dict, str)
    check(assert_type(mapping(ImplementsGeoInterfaceRW()), dict[str, Any]), dict, dtype=str)
    check(assert_type(mapping(ImplementsGeoInterfaceRO()), dict[str, Any]), dict, dtype=str)

    d = {"type": "Point", "coordinates": (1.0, 2.0)}
    check(
        assert_type(shape({"type": "Point", "coordinates": (1.0, 2.0)}), BaseGeometry), BaseGeometry
    )
    check(assert_type(shape(d), BaseGeometry), BaseGeometry)
    check(assert_type(shape(ImplementsGeoInterfaceRW()), BaseGeometry), BaseGeometry)
    check(assert_type(shape(ImplementsGeoInterfaceRO()), BaseGeometry), BaseGeometry)
