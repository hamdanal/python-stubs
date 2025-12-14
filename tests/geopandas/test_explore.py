from __future__ import annotations

from typing import TYPE_CHECKING, assert_type

import folium
import geopandas as gpd
from geopandas.explore import _explore, _explore_geoseries
from shapely import Point

GDF = gpd.GeoDataFrame({"x": [1, 2], "geometry": [Point(1, 2), Point(3, 4)]})


def test_explore() -> None:
    if TYPE_CHECKING:
        assert_type(GDF.explore(tooltip=False, popup=True, k=4, map_kwds={}), folium.Map)
        assert_type(_explore(GDF, tooltip=False, popup=True, k=4, map_kwds={}), folium.Map)
        GDF.explore(map_kwds=False)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
        _explore(GDF, map_kwds=False)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]


def test_geoseries_explore() -> None:
    if TYPE_CHECKING:
        assert_type(
            GDF.geometry.explore(highlight=False, control_scale=False, map_kwds={}), folium.Map
        )
        assert_type(
            _explore_geoseries(GDF.geometry, highlight=False, control_scale=False, map_kwds={}),
            folium.Map,
        )
        GDF.geometry.explore(map_kwds=False)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
        _explore_geoseries(GDF.geometry, map_kwds=False)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
