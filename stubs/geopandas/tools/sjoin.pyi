from geopandas.geodataframe import GeoDataFrame

def sjoin(
    left_df: GeoDataFrame,
    right_df: GeoDataFrame,
    how: str = "inner",
    predicate: str = "intersects",
    lsuffix: str = "left",
    rsuffix: str = "right",
    op: str = ...,  # deprecated alias to predicate
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
