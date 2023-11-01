from typing import Any

import pandas as pd

from geopandas.geodataframe import GeoDataFrame

version: str
urlbase: str

def countries_override(world_raw): ...
def df_same(new: pd.DataFrame, old: pd.DataFrame, dataset, log: list[str]) -> bool: ...

config: list[dict[str, Any]]
downloads: dict[str, GeoDataFrame]
log: list[str]
