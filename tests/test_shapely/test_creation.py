from __future__ import annotations

import numpy as np
import pytest
import shapely
from numpy.typing import NDArray
from shapely import (
    GeometryType,
    LinearRing,
    LineString,
    MultiLineString,
    MultiPoint,
    Point,
    Polygon,
)
from shapely.prepared import PreparedGeometry
from typing_extensions import assert_type

from tests import HasArray, check

P = Point(1, 2)
LS = LineString([(1, 2), (3, 4), (5, 6), (7, 8)])


def test_points() -> None:
    check(assert_type(shapely.points((0, 1, 2.0)), Point), Point)
    check(assert_type(shapely.points([0, 1, 2], None), Point), Point)
    check(assert_type(shapely.points(0.0, 1, 2.0), Point), Point)
    check(assert_type(shapely.points(0, 1.0, None), Point), Point)
    check(
        assert_type(shapely.points([[0, 1], [4, 5]]), NDArray[np.object_]), np.ndarray, dtype=Point
    )
    check(
        assert_type(shapely.points([0.0], [1.2], [2.3]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.points([(0, 1, 2.0)], indices=[0]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )

    # less precise types
    check(assert_type(shapely.points(np.array([0, 1, 2])), NDArray[np.object_] | Point), Point)
    check(
        assert_type(shapely.points(HasArray(np.array([0, 1, 2]))), NDArray[np.object_] | Point),
        Point,
    )
    check(
        assert_type(shapely.points(np.array([[0, 1], [4, 5]])), NDArray[np.object_] | Point),
        np.ndarray,
        dtype=Point,
    )
    check(assert_type(shapely.points(0, [1]), NDArray[np.object_] | Point), np.ndarray, dtype=Point)
    check(
        assert_type(shapely.points(0, [1, 2]), NDArray[np.object_] | Point), np.ndarray, dtype=Point
    )
    out = np.array([P], dtype=object)
    check(
        assert_type(shapely.points(0, 1.0, out=out), NDArray[np.object_] | Point),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.points((0, 1, 2.0), out=out), NDArray[np.object_] | Point),
        np.ndarray,
        dtype=Point,
    )

    # wrong
    with pytest.raises(Exception):
        shapely.points(0)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.points(0, None, 1)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.points(0, 1, indices=[0])  # False negative (difficult to catch)


def test_linestrings() -> None:
    check(assert_type(shapely.linestrings([(0, 1, 2.0), (0, 1, 2.0)]), LineString), LineString)
    check(assert_type(shapely.linestrings([[0, 1, 2], [1, 1, 3]], None), LineString), LineString)
    check(
        assert_type(shapely.linestrings([[[0, 1], [4, 5]], [[2, 3], [5, 6]]]), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )

    # less precise types
    check(
        assert_type(
            shapely.linestrings(np.array([[0, 1, 2], [1, 1, 3]])), NDArray[np.object_] | LineString
        ),
        LineString,
    )
    check(
        assert_type(
            shapely.linestrings(np.array([[[0, 1], [4, 5]], [[2, 3], [5, 6]]])),
            NDArray[np.object_] | LineString,
        ),
        np.ndarray,
        dtype=LineString,
    )

    # wrong
    with pytest.raises(Exception):
        shapely.linestrings(0, 1)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_linearrings() -> None:
    check(
        assert_type(
            shapely.linearrings([(0, 1, 2.0), (0, 2.0, 2), (0.5, 1.5, 0.0), (0, 1, 0)]), LinearRing
        ),
        LinearRing,
    )
    check(
        assert_type(shapely.linearrings([[0, 0.0], [0, 1], [1, 1], [0, 0]], None), LinearRing),
        LinearRing,
    )
    check(
        assert_type(
            shapely.linearrings([[[0, 0.0], [0, 1], [1, 1]], [[2, 3], [5, 6], [7, 8]]]),
            NDArray[np.object_],
        ),
        np.ndarray,
        dtype=LinearRing,
    )

    # less precise types
    check(
        assert_type(
            shapely.linearrings(np.array([(0, 1, 2.0), (0, 2.0, 2), (0.5, 1.5, 0.0), (0, 1, 0)])),
            NDArray[np.object_] | LinearRing,
        ),
        LinearRing,
    )
    check(
        assert_type(
            shapely.linearrings(np.array([[[0, 0.0], [0, 1], [1, 1]], [[2, 3], [5, 6], [7, 8]]])),
            NDArray[np.object_] | LinearRing,
        ),
        np.ndarray,
        dtype=LinearRing,
    )

    # wrong
    with pytest.raises(Exception):
        shapely.linearrings(0, 1)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_polygons() -> None:
    ring_1 = LinearRing([[0, 0], [0, 10], [10, 10], [10, 0]])
    ring_2 = LinearRing([[2, 6], [2, 7], [3, 7], [3, 6]])

    check(assert_type(shapely.polygons([[0, 0], [0, 10], [10, 10], [10, 0]]), Polygon), Polygon)
    check(assert_type(shapely.polygons(ring_1), Polygon), Polygon)
    check(assert_type(shapely.polygons(ring_1, holes=[ring_2]), Polygon), Polygon)
    check(assert_type(shapely.polygons(None), Polygon), Polygon)
    check(assert_type(shapely.polygons(ring_1, holes=[None]), Polygon), Polygon)

    check(
        assert_type(shapely.polygons([ring_1, ring_2]), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(shapely.polygons([ring_1, ring_2], indices=[0, 1]), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(shapely.polygons([ring_1, ring_2], indices=[0, 1]), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(shapely.polygons([ring_1, ring_2], indices=[0, 0]), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(shapely.polygons([ring_1, None], indices=[0, 0]), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )

    # less precise types
    check(
        assert_type(
            shapely.polygons(np.array([[0, 0], [0, 10], [10, 10], [10, 0]])),
            NDArray[np.object_] | Polygon,
        ),
        Polygon,
    )
    check(
        assert_type(shapely.polygons(np.array([ring_1, ring_2])), NDArray[np.object_] | Polygon),
        np.ndarray,
        dtype=Polygon,
    )


def test_box() -> None:
    check(assert_type(shapely.box(0, 0, 1, 1), Polygon), Polygon)
    check(assert_type(shapely.box(0.1, 0.1, 1.1, 1.1), Polygon), Polygon)
    check(assert_type(shapely.box(0, 0, 1, 1, ccw=False), Polygon), Polygon)
    check(
        assert_type(shapely.box([0], [0], [1], [1]), NDArray[np.object_]), np.ndarray, dtype=Polygon
    )
    check(
        assert_type(shapely.box([0], [0], [1], [1], ccw=False), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(
            shapely.box(np.array([0]), np.array([0]), np.array([1]), np.array([1])),
            NDArray[np.object_],
        ),
        np.ndarray,
        dtype=Polygon,
    )


def test_multipoints() -> None:
    p1 = Point([1, 1])
    p2 = Point([2, 2])

    check(assert_type(shapely.multipoints([None]), MultiPoint), MultiPoint)
    check(assert_type(shapely.multipoints([p1, p2]), MultiPoint), MultiPoint)
    check(assert_type(shapely.multipoints((p1, None)), MultiPoint), MultiPoint)
    check(assert_type(shapely.multipoints([[0, 0], [2, 2], [3, 3.0]]), MultiPoint), MultiPoint)

    check(
        assert_type(shapely.multipoints([(p1, None)]), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiPoint,
    )
    check(
        assert_type(shapely.multipoints([[[0, 0], [2, 2], [3, 3.0]]]), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiPoint,
    )

    # less precise types
    check(
        assert_type(shapely.multipoints(np.array((p1, None))), MultiPoint | NDArray[np.object_]),
        MultiPoint,
    )
    check(
        assert_type(
            shapely.multipoints(np.array((p1, None)), indices=[0, 0]),
            MultiPoint | NDArray[np.object_],
        ),
        np.ndarray,
        dtype=MultiPoint,
    )
    check(
        assert_type(
            shapely.multipoints(np.array((p1, None)), out=np.array([None], dtype=object)),
            MultiPoint | NDArray[np.object_],
        ),
        np.ndarray,
        dtype=MultiPoint,
    )
    check(
        assert_type(
            shapely.multipoints(np.array([[0, 0], [2, 2], [3, 3.0]])),
            MultiPoint | NDArray[np.object_],
        ),
        MultiPoint,
    )
    check(
        assert_type(shapely.multipoints(np.array([(p1, None)])), MultiPoint | NDArray[np.object_]),
        np.ndarray,
        dtype=MultiPoint,
    )
    check(
        assert_type(
            shapely.multipoints(np.array([[[0, 0], [2, 2], [3, 3.0]]])),
            MultiPoint | NDArray[np.object_],
        ),
        np.ndarray,
        dtype=MultiPoint,
    )


def test_multilinestrings() -> None:
    ls1 = LineString([[0, 0], [0, 10], [10, 10], [10, 0]])
    ls2 = LineString([[2, 6], [2, 7], [3, 7], [3, 6]])

    check(assert_type(shapely.multilinestrings([None]), MultiLineString), MultiLineString)
    check(assert_type(shapely.multilinestrings([ls1, ls2]), MultiLineString), MultiLineString)
    check(assert_type(shapely.multilinestrings((ls1, None)), MultiLineString), MultiLineString)
    check(
        assert_type(shapely.multilinestrings([[[0, 0], [2, 2], [3, 3.0]]]), MultiLineString),
        MultiLineString,
    )

    check(
        assert_type(shapely.multilinestrings([(ls1, None)]), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiLineString,
    )
    check(
        assert_type(shapely.multilinestrings([[[[0, 0], [2, 2], [3, 3.0]]]]), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiLineString,
    )

    # less precise types
    check(
        assert_type(
            shapely.multilinestrings(np.array((ls1, None))), MultiLineString | NDArray[np.object_]
        ),
        MultiLineString,
    )
    check(
        assert_type(
            shapely.multilinestrings(np.array((ls1, None)), indices=[0, 0]),
            MultiLineString | NDArray[np.object_],
        ),
        np.ndarray,
        dtype=MultiLineString,
    )
    check(
        assert_type(
            shapely.multilinestrings(np.array((ls1, None)), out=np.array([None], dtype=object)),
            MultiLineString | NDArray[np.object_],
        ),
        np.ndarray,
        dtype=MultiLineString,
    )
    check(
        assert_type(
            shapely.multilinestrings(np.array([[[0, 0], [2, 2], [3, 3.0]]])),
            MultiLineString | NDArray[np.object_],
        ),
        MultiLineString,
    )
    check(
        assert_type(
            shapely.multilinestrings(np.array([(ls1, None)])), MultiLineString | NDArray[np.object_]
        ),
        np.ndarray,
        dtype=MultiLineString,
    )
    check(
        assert_type(
            shapely.multilinestrings(np.array([[[[0, 0], [2, 2], [3, 3.0]]]])),
            MultiLineString | NDArray[np.object_],
        ),
        np.ndarray,
        dtype=MultiLineString,
    )


def test_multipolygons() -> None:
    ...  # TODO multipolygons is not typed yet


def test_geometrycollections() -> None:
    ...  # TODO geometrycollections is not typed yet


def test_prepare() -> None:
    shapely.prepare(P)
    shapely.prepare(None)
    shapely.prepare([P])
    shapely.prepare([None])
    shapely.prepare((P, None))
    shapely.prepare(np.array((P, None)))


def test_destroy_prepared() -> None:
    shapely.destroy_prepared(P)
    shapely.destroy_prepared(None)
    shapely.destroy_prepared([P])
    shapely.destroy_prepared([None])
    shapely.destroy_prepared((P, None))
    shapely.destroy_prepared(np.array((P, None)))

    # despite its name, this function doesn't accept PreparedGeometry
    with pytest.raises(Exception):
        shapely.destroy_prepared(PreparedGeometry(P))  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        shapely.destroy_prepared([PreparedGeometry(P)])  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        shapely.destroy_prepared((PreparedGeometry(P), None))  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]


def test_empty() -> None:
    check(assert_type(shapely.empty(0), NDArray[np.object_]), np.ndarray)
    check(
        assert_type(shapely.empty((2, 3), geom_type=GeometryType.POINT), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    gt = int(GeometryType.POINT.value)
    check(
        assert_type(shapely.empty((2, 3), geom_type=gt), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
