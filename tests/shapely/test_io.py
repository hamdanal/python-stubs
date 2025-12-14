from __future__ import annotations

import io
from types import NoneType

import numpy as np
import pytest
import shapely
import shapely.wkb
import shapely.wkt
from numpy.typing import NDArray
from shapely import GeometryType, LineString, Point, Polygon
from shapely.geometry.base import BaseGeometry
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
LS = LineString([(1, 2), (3, 4), (5, 6), (7, 8)])
P_WKT = "POINT (1 2)"
P_WKB = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@"
P_WKB_HEX = "0101000000000000000000F03F0000000000000040"
P_GEOJSON = '{"type": "Point", "coordinates": [1.0, 2.0]}'
PO = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)], holes=[[(2, 2), (3, 2), (2, 3)]])


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


def test_ragged_array() -> None:
    ra = shapely.to_ragged_array([PO])
    check(
        assert_type(ra, tuple[GeometryType, NDArray[np.float64], tuple[NDArray[np.int32], ...]]),
        tuple,
    )
    check(assert_type(ra[0], GeometryType), GeometryType)
    check(assert_type(ra[1], NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(ra[2], tuple[NDArray[np.int32], ...]), tuple, dtype=np.ndarray)
    check(assert_type(ra[2][0], NDArray[np.int32]), np.ndarray, dtype=np.int32)
    check(
        assert_type(
            shapely.to_ragged_array([PO], include_z=True),
            tuple[GeometryType, NDArray[np.float64], tuple[NDArray[np.int32], ...]],
        ),
        tuple,
    )
    shapely.to_ragged_array([PO, None])
    with pytest.raises(Exception):
        shapely.to_ragged_array(PO)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]

    check(
        assert_type(shapely.from_ragged_array(*ra), NDArray[np.object_]), np.ndarray, dtype=Polygon
    )

    check(
        assert_type(shapely.from_ragged_array(*shapely.to_ragged_array([PO])), NDArray[np.object_]),
        np.ndarray,
        dtype=Polygon,
    )
    check(
        assert_type(
            shapely.from_ragged_array(ra[0], coords=tuple(ra[1]), offsets=list(ra[2])),
            NDArray[np.object_],
        ),
        np.ndarray,
        dtype=Polygon,
    )


def test_wkt_module() -> None:
    check(assert_type(shapely.wkt.loads(P_WKT), BaseGeometry), Point)
    check(assert_type(shapely.wkt.dumps(P), str), str)
    check(assert_type(shapely.wkt.dumps(P, trim=True), str), str)
    check(assert_type(shapely.wkt.dumps(P, rounding_precision=5), str), str)

    file = io.StringIO(P_WKT)
    check(assert_type(shapely.wkt.load(file), BaseGeometry), Point)
    check(assert_type(shapely.wkt.dump(P, file), None), NoneType)

    class WktReader:
        def read(self) -> str:
            return P_WKT

    class WktWriter:
        def write(self, wkt: str, /) -> None:
            assert isinstance(wkt, str)

    check(assert_type(shapely.wkt.load(WktReader()), BaseGeometry), Point)
    check(assert_type(shapely.wkt.dump(P, WktWriter()), None), NoneType)


def test_wkb_module() -> None:
    check(assert_type(shapely.wkb.loads(P_WKB), BaseGeometry), Point)
    check(assert_type(shapely.wkb.dumps(P), bytes), bytes)
    check(assert_type(shapely.wkb.dumps(P, hex=True), str), str)
    check(assert_type(shapely.wkb.dumps(P, srid=5), bytes), bytes)

    file = io.BytesIO(P_WKB)
    check(assert_type(shapely.wkb.load(file), BaseGeometry), Point)
    check(assert_type(shapely.wkb.dump(P, file), None), NoneType)

    class WkbReader:
        def read(self) -> bytes:
            return P_WKB

    class WkbHexReader:
        def read(self) -> str:
            return P_WKB_HEX

    class WkbWriter:
        def write(self, wkb: bytes, /) -> None:
            assert isinstance(wkb, bytes)

    class WkbHexWriter:
        def write(self, wkb: str, /) -> None:
            assert isinstance(wkb, str)

    check(assert_type(shapely.wkb.load(WkbReader()), BaseGeometry), Point)
    check(assert_type(shapely.wkb.load(WkbHexReader()), BaseGeometry), Point)
    check(assert_type(shapely.wkb.dump(P, WkbWriter()), None), NoneType)
    check(assert_type(shapely.wkb.dump(P, WkbHexWriter(), hex=True), None), NoneType)

    with pytest.raises(Exception):
        shapely.wkb.dump(P, WkbWriter(), hex=True)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.wkb.dump(P, WkbHexWriter(), hex=False)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
