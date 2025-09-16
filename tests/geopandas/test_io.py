from __future__ import annotations

from collections import OrderedDict
from pathlib import Path
from typing import TYPE_CHECKING

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.io.file import infer_schema
from shapely import LineString, Point, Polygon
from typing_extensions import assert_type

from tests import check

if TYPE_CHECKING:
    from geopandas.io.file import _Schema
else:
    _Schema = dict

P = Point(1, 2)
LS = LineString([(0, 0), (1, 1)])
PO: Polygon = P.buffer(1)
GDF = gpd.GeoDataFrame({"x": [1, 2], "geometry": [Point(1, 2), Point(3, 4)]}, crs="EPSG:4326")


def test_read_file(tmp_path: Path) -> None:
    file = tmp_path / "test.gpkg"
    GDF.to_file(file, driver="GPKG", layer="test")
    gdf = gpd.read_file(file)
    check(assert_type(gdf, gpd.GeoDataFrame), gpd.GeoDataFrame)
    df = gpd.read_file(file, ignore_geometry=True)
    check(assert_type(df, pd.DataFrame), pd.DataFrame)
    assert not isinstance(df, gpd.GeoDataFrame)

    with pytest.raises(Exception):
        gpd.read_file(file, engine="toto")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]


def test_infer_schema() -> None:
    schema = infer_schema(GDF)
    heterogeneous_schema = infer_schema(gpd.GeoDataFrame({"x": [1, 2], "geometry": [P, LS]}))
    check(
        assert_type(schema, _Schema),
        _Schema,  # pyright: ignore[reportGeneralTypeIssues]
        dtype=str,
    )
    check(assert_type(schema["geometry"], str | list[str]), str)
    check(assert_type(heterogeneous_schema["geometry"], str | list[str]), list, dtype=str)
    check(assert_type(schema["properties"], OrderedDict[str, str]), OrderedDict, dtype=str)
    properties_values = list(schema["properties"].values())
    check(assert_type(properties_values, list[str]), list, dtype=str)
