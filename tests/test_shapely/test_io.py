from __future__ import annotations

from types import NoneType

import numpy as np
import shapely
from numpy.typing import NDArray
from shapely import LineString, Point
from shapely.geometry.base import BaseGeometry
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
LS = LineString([(1, 2), (3, 4), (5, 6), (7, 8)])
P_WKT = "POINT (1 2)"
P_WKB = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@"
P_WKB_HEX = (
    "010200000004000000000000000000F03F00000000000000400000000000000840000000000000"
    "1040000000000000144000000000000018400000000000001C400000000000002040"
)
P_GEOJSON = '{"type": "Point", "coordinates": [1.0, 2.0]}'


def test_wkt() -> None:
    check(assert_type(shapely.to_wkt(None), None), NoneType)
    check(assert_type(shapely.to_wkt(P), str), str)
    check(assert_type(shapely.to_wkt([P]), NDArray[np.str_]), np.ndarray, dtype=str)
    check(assert_type(shapely.to_wkt((P, LS, None)), NDArray[np.str_]), np.ndarray, dtype=str)

    check(assert_type(shapely.from_wkt(None), None), NoneType)
    check(
        assert_type(shapely.from_wkt([P_WKT]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(
        assert_type(shapely.from_wkt((P_WKT, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_wkb() -> None:
    check(assert_type(shapely.to_wkb(None), None), NoneType)
    check(assert_type(shapely.to_wkb(P), bytes), bytes)
    check(assert_type(shapely.to_wkb([P]), NDArray[np.bytes_]), np.ndarray, dtype=bytes)
    check(assert_type(shapely.to_wkb((P, LS, None)), NDArray[np.bytes_]), np.ndarray, dtype=bytes)

    check(assert_type(shapely.to_wkb(None, hex=True), None), NoneType)
    check(assert_type(shapely.to_wkb(P, hex=True), str), str)
    check(assert_type(shapely.to_wkb([P], hex=True), NDArray[np.str_]), np.ndarray, dtype=str)
    check(
        assert_type(shapely.to_wkb((P, LS, None), hex=True), NDArray[np.str_]),
        np.ndarray,
        dtype=str,
    )

    check(assert_type(shapely.from_wkb(P_WKB), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.from_wkb(P_WKB_HEX), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.from_wkb(None), None), NoneType)
    check(
        assert_type(shapely.from_wkb([P_WKB]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(
        assert_type(shapely.from_wkb([P_WKB, None]), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.from_wkb((P_WKB, P_WKB_HEX, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_geojson() -> None:
    check(assert_type(shapely.to_geojson(None), None), NoneType)
    check(assert_type(shapely.to_geojson(P), str), str)
    check(assert_type(shapely.to_geojson([P]), NDArray[np.str_]), np.ndarray, dtype=str)
    check(assert_type(shapely.to_geojson((P, LS, None)), NDArray[np.str_]), np.ndarray, dtype=str)

    check(assert_type(shapely.from_geojson(None), None), NoneType)
    check(
        assert_type(shapely.from_geojson([P_GEOJSON]), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.from_geojson((P_GEOJSON, None)), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
