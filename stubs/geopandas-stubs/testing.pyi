from typing import Literal

from geopandas.array import GeometryArray
from geopandas.base import GeoPandasBase
from geopandas.geodataframe import GeoDataFrame
from geopandas.geoseries import GeoSeries

def geom_equals(this: GeoPandasBase | GeometryArray, that: GeoPandasBase | GeometryArray) -> bool: ...
def geom_almost_equals(this: GeoPandasBase | GeometryArray, that: GeoPandasBase | GeometryArray) -> bool: ...
def assert_geoseries_equal(
    left: GeoSeries,
    right: GeoSeries,
    check_dtype: bool = True,
    check_index_type: bool = False,
    check_series_type: bool = True,
    check_less_precise: bool = False,
    check_geom_type: bool = False,
    check_crs: bool = True,
    normalize: bool = False,
) -> None: ...
def assert_geodataframe_equal(
    left: GeoDataFrame,
    right: GeoDataFrame,
    check_dtype: bool = True,
    check_index_type: bool | Literal["equiv"] = "equiv",
    check_column_type: bool | Literal["equiv"] = "equiv",
    check_frame_type: bool = True,
    check_like: bool = False,
    check_less_precise: bool = False,
    check_geom_type: bool = False,
    check_crs: bool = True,
    normalize: bool = False,
) -> None: ...
