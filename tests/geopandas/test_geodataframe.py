from __future__ import annotations

import warnings
from types import NoneType

import geopandas as gpd
import pytest
from geopandas import GeoDataFrame, GeoSeries
from pyproj import CRS
from shapely import LineString, Point, Polygon
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
LS = LineString([(0, 0), (1, 1)])
PO: Polygon = P.buffer(1)
GDF = gpd.GeoDataFrame({"x": [1, 2], "geometry": [Point(1, 2), Point(3, 4)]})


def test_geometry() -> None:
    gdf = GDF.copy()
    geo = gdf.geometry

    # getter
    check(assert_type(gdf.geometry, GeoSeries), GeoSeries)

    # setter
    gdf.geometry = geo
    gdf.geometry = geo.values  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004
    gdf.geometry = [Point(1, 2), Point(3, 4)]  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004
    with pytest.raises(Exception):
        gdf.geometry = "geometry"  # type: ignore[assignment] # pyright: ignore[reportAttributeAccessIssue]
    with pytest.raises(Exception):
        gdf.geometry = [1, 2]  # type: ignore[assignment] # pyright: ignore[reportAttributeAccessIssue]

    # set_geometry
    check(assert_type(gdf.set_geometry(geo), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_geometry(geo, inplace=True), None), NoneType)
    check(assert_type(gdf.set_geometry(geo, False, True), None), NoneType)
    check(assert_type(gdf.set_geometry([Point(1, 2), Point(3, 4)]), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_geometry("geometry"), GeoDataFrame), GeoDataFrame)
    with pytest.raises(Exception):
        gdf.set_geometry([1, 2])  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]

    # rename_geometry
    check(assert_type(gdf.rename_geometry("geom"), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.rename_geometry("geom", inplace=True), None), NoneType)
    check(assert_type(gdf.rename_geometry("geometry", True), None), NoneType)


def test_crs() -> None:
    gdf = GDF.copy()
    crs = CRS("EPSG:4326")

    # getter
    check(assert_type(gdf.crs, CRS | None), NoneType)
    gdf.set_crs(crs, inplace=True)
    check(assert_type(gdf.crs, CRS | None), CRS)

    # setter
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        gdf.crs = None
        gdf.crs = crs
        gdf.crs = "EPSG:4326"  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004
        gdf.crs = 4326  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004
        with pytest.raises(Exception):
            gdf.crs = 1.5  # type: ignore[assignment] # pyright: ignore[reportAttributeAccessIssue]

    # set_crs
    check(assert_type(gdf.set_crs(crs), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_crs(crs, inplace=True), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_crs(crs, None, True), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_crs("EPSG:4326"), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_crs(crs=4326), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.set_crs(epsg=4326), GeoDataFrame), GeoDataFrame)
    with pytest.raises(Exception):
        gdf.set_crs()  # type: ignore[call-overload] # pyright: ignore[reportCallIssue]
    with pytest.raises(Exception):
        gdf.set_crs(None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        gdf.set_crs(None, None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]

    # to_crs
    check(assert_type(gdf.to_crs(crs), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.to_crs(crs, inplace=True), None), NoneType)
    check(assert_type(gdf.to_crs(crs, None, True), None), NoneType)
    check(assert_type(gdf.to_crs("EPSG:4326"), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.to_crs(crs=4326), GeoDataFrame), GeoDataFrame)
    check(assert_type(gdf.to_crs(epsg=4326), GeoDataFrame), GeoDataFrame)
    with pytest.raises(Exception):
        gdf.to_crs()  # type: ignore[call-overload] # pyright: ignore[reportCallIssue]
    with pytest.raises(Exception):
        gdf.to_crs(None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        gdf.to_crs(None, None)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
    with pytest.raises(Exception):
        gdf.to_crs(inplace=True)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue]
    with pytest.raises(Exception):
        gdf.to_crs(None, inplace=True)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
    with pytest.raises(Exception):
        gdf.to_crs(None, None, inplace=True)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
    with pytest.raises(Exception):
        gdf.to_crs(None, None, True)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]

    # estimate_utm_crs
    check(assert_type(gdf.estimate_utm_crs(), CRS), CRS)
    check(assert_type(gdf.estimate_utm_crs("WGS 84"), CRS), CRS)
    with pytest.raises(Exception):
        gdf.estimate_utm_crs(84)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
    with pytest.raises(Exception):
        gdf.estimate_utm_crs(CRS)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
