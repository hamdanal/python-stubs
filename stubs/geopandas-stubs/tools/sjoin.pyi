from typing import overload
from typing_extensions import deprecated

from geopandas.geodataframe import GeoDataFrame

@overload
def sjoin(
    left_df: GeoDataFrame,
    right_df: GeoDataFrame,
    how: str = "inner",
    predicate: str = "intersects",
    lsuffix: str = "left",
    rsuffix: str = "right",
) -> GeoDataFrame: ...
@overload
@deprecated("Parameter `op` is deprecated. Use parameter `predicate` instead.")
def sjoin(
    left_df: GeoDataFrame,
    right_df: GeoDataFrame,
    how: str = "inner",
    predicate: str = "intersects",
    lsuffix: str = "left",
    rsuffix: str = "right",
    *,
    op: str = ...,
) -> GeoDataFrame: ...
def sjoin_nearest(
    left_df: GeoDataFrame,
    right_df: GeoDataFrame,
    how: str = "inner",
    max_distance: float | None = None,
    lsuffix: str = "left",
    rsuffix: str = "right",
    distance_col: str | None = None,
    exclusive: bool = False,
) -> GeoDataFrame: ...
