from __future__ import annotations

from types import NoneType

import numpy as np
import pytest
import shapely
from numpy.typing import NDArray
from shapely import GeometryCollection, LineString, MultiLineString, MultiPoint, Point, Polygon
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
LS = LineString([(0, 0), (1, 1)])
PO: Polygon = P.buffer(1)
MP = MultiPoint([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
MLS = MultiLineString([LS, PO.exterior])


def test_line_interpolate_point() -> None:
    check(assert_type(shapely.line_interpolate_point(LS, 1.0), Point), Point)
    check(assert_type(shapely.line_interpolate_point(MLS, 1.0), Point), Point)
    check(assert_type(shapely.line_interpolate_point(GeometryCollection(MLS), 1.0), Point), Point)
    check(assert_type(shapely.line_interpolate_point(None, 1.0), None), NoneType)
    check(
        assert_type(shapely.line_interpolate_point([MLS, LS], 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.line_interpolate_point((MLS, LS, None), 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.line_interpolate_point(MLS, [1.0]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(assert_type(shapely.line_interpolate_point(LS, 1.0, normalized=True), Point), Point)
    check(
        assert_type(
            shapely.line_interpolate_point([MLS, LS], 1.0, normalized=True), NDArray[np.object_]
        ),
        np.ndarray,
        dtype=Point,
    )
    with pytest.raises(TypeError):
        shapely.line_interpolate_point(P, 1.0)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_line_locate_point() -> None:
    check(assert_type(shapely.line_locate_point(LS, P), float), float)
    check(assert_type(shapely.line_locate_point(MLS, P), float), float)
    check(assert_type(shapely.line_locate_point(GeometryCollection(MLS), P), float), float)
    check(assert_type(shapely.line_locate_point(None, P), float), float)
    check(assert_type(shapely.line_locate_point(LS, None), float), float)
    check(assert_type(shapely.line_locate_point(None, None), float), float)
    check(
        assert_type(shapely.line_locate_point([MLS, LS], P), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.line_locate_point((MLS, LS, None), P), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.line_locate_point(MLS, [P]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(assert_type(shapely.line_locate_point(LS, P, normalized=True), float), float)
    check(
        assert_type(shapely.line_locate_point([MLS, LS], P, normalized=True), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    with pytest.raises(Exception):
        shapely.line_locate_point(P, P)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]

    with pytest.raises(Exception):
        shapely.line_locate_point(MLS, LS)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_line_merge() -> None:
    expected_type = LineString | MultiLineString | GeometryCollection
    check(assert_type(shapely.line_merge(P), expected_type), GeometryCollection)
    check(assert_type(shapely.line_merge(LineString()), expected_type), GeometryCollection)
    check(assert_type(shapely.line_merge(MultiLineString()), expected_type), GeometryCollection)
    check(assert_type(shapely.line_merge(LS), expected_type), LineString)
    check(assert_type(shapely.line_merge(MLS), expected_type), MultiLineString)
    check(assert_type(shapely.line_merge(GeometryCollection(MLS)), expected_type), MultiLineString)
    check(assert_type(shapely.line_merge(None), None), NoneType)
    check(
        assert_type(shapely.line_merge([LS, None]), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )
    check(
        assert_type(shapely.line_merge((MLS, LS, P, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=MultiLineString,
    )
    check(assert_type(shapely.line_merge(LS, directed=True), expected_type), LineString)


def test_shared_paths() -> None:
    check(assert_type(shapely.shared_paths(MLS, LS), GeometryCollection), GeometryCollection)
    check(assert_type(shapely.shared_paths(MLS, None), None), NoneType)
    check(assert_type(shapely.shared_paths(None, MLS), None), NoneType)
    check(assert_type(shapely.shared_paths(None, None), None), NoneType)
    check(
        assert_type(shapely.shared_paths([MLS, LS], LS), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.shared_paths((MLS, None), LS), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.shared_paths(MLS, [LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    check(
        assert_type(shapely.shared_paths([MLS], [LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=GeometryCollection,
    )
    with pytest.raises(Exception):
        shapely.shared_paths(MLS, P)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.shared_paths(P, MLS)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.shared_paths(GeometryCollection(MLS), LS)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_shortest_line() -> None:
    check(assert_type(shapely.shortest_line(MLS, LS), LineString), LineString)
    check(assert_type(shapely.shortest_line(MLS, P), LineString), LineString)
    check(assert_type(shapely.shortest_line(PO, LS), LineString), LineString)
    check(assert_type(shapely.shortest_line(MLS, None), None), NoneType)
    check(assert_type(shapely.shortest_line(None, MLS), None), NoneType)
    check(assert_type(shapely.shortest_line(None, None), None), NoneType)
    check(
        assert_type(shapely.shortest_line([MLS, LS], LS), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )
    check(
        assert_type(shapely.shortest_line((MLS, None), LS), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )
    check(
        assert_type(shapely.shortest_line(MLS, [LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )
    check(
        assert_type(shapely.shortest_line([MLS], [LS]), NDArray[np.object_]),
        np.ndarray,
        dtype=LineString,
    )
