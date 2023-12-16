from typing import Any
from typing_extensions import deprecated

import pandas as pd

from geopandas.geodataframe import GeoDataFrame

version: str
urlbase: str

@deprecated("Module `geopandas.dataset` is deprecated and will be removed in GeoPandas 1.0.")
def countries_override(world_raw: GeoDataFrame) -> GeoDataFrame: ...
@deprecated("Module `geopandas.dataset` is deprecated and will be removed in GeoPandas 1.0.")
def df_same(new: pd.DataFrame, old: pd.DataFrame, dataset, log: list[str]) -> bool: ...

config: list[dict[str, Any]]
downloads: dict[str, GeoDataFrame]
log: list[str]
