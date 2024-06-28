from __future__ import annotations

import warnings
from types import NoneType

import geopandas as gpd
import pytest
from geopandas import GeoSeries
from pyproj import CRS
from shapely import LineString, Point, Polygon
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
LS = LineString([(0, 0), (1, 1)])
PO: Polygon = P.buffer(1)
GS = gpd.GeoSeries([Point(1, 2), Point(3, 4)])


def test_geometry() -> None:
    gs = GS.copy()

    # getter
    check(assert_type(gs.geometry, GeoSeries), GeoSeries)


def test_crs() -> None:
    gs = GS.copy()
    crs = CRS("EPSG:4326")

    # getter
    check(assert_type(gs.crs, CRS | None), NoneType)
    gs.set_crs(crs, inplace=True)
    check(assert_type(gs.crs, CRS | None), CRS)

    # setter
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        gs.crs = None
        gs.crs = crs
        gs.crs = "EPSG:4326"  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004
        gs.crs = 4326  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004
        assert isinstance(gs.crs, CRS)
        with pytest.raises(Exception):
            gs.crs = 1.5  # type: ignore[assignment] # pyright: ignore[reportAttributeAccessIssue]

    # set_crs
    check(assert_type(gs.set_crs(crs), GeoSeries), GeoSeries)
    check(assert_type(gs.set_crs(crs, inplace=True), GeoSeries), GeoSeries)
    check(assert_type(gs.set_crs(crs, None, True), GeoSeries), GeoSeries)
    check(assert_type(gs.set_crs("EPSG:4326"), GeoSeries), GeoSeries)
    check(assert_type(gs.set_crs(crs=4326), GeoSeries), GeoSeries)
    check(assert_type(gs.set_crs(epsg=4326), GeoSeries), GeoSeries)
    with pytest.raises(Exception):
        gs.set_crs()  # type: ignore[call-overload] # pyright: ignore[reportCallIssue]
    with pytest.raises(Exception):
        gs.set_crs(None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        gs.set_crs(None, None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]

    # to_crs
    check(assert_type(gs.to_crs(crs), GeoSeries), GeoSeries)
    check(assert_type(gs.to_crs("EPSG:4326"), GeoSeries), GeoSeries)
    check(assert_type(gs.to_crs(crs=4326), GeoSeries), GeoSeries)
    check(assert_type(gs.to_crs(epsg=4326), GeoSeries), GeoSeries)
    with pytest.raises(Exception):
        gs.to_crs()  # type: ignore[call-overload] # pyright: ignore[reportCallIssue]
    with pytest.raises(Exception):
        gs.to_crs(None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        gs.to_crs(None, None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]

    # estimate_utm_crs
    check(assert_type(gs.estimate_utm_crs(), CRS), CRS)
    check(assert_type(gs.estimate_utm_crs("WGS 84"), CRS), CRS)
    with pytest.raises(Exception):
        gs.estimate_utm_crs(84)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        gs.estimate_utm_crs(CRS)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
