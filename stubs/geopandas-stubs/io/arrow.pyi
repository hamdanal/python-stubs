import os
from _typeshed import SupportsKeysAndGetItem
from collections.abc import Iterable
from typing import Any

from geopandas.geodataframe import GeoDataFrame

METADATA_VERSION: str
SUPPORTED_VERSIONS: list[str]

def _read_parquet(
    path: str | os.PathLike[str],
    columns: Iterable[str] | None = None,
    storage_options: SupportsKeysAndGetItem[str, Any] | None = None,
    **kwargs: Any,  # kwargs passed to pyarrow.parquet.read_table
) -> GeoDataFrame: ...
def _read_feather(
    path: str | os.PathLike[str],
    columns: Iterable[str] | None = None,
    **kwargs: Any,  # kwargs passed to pyarrow.feather.read_table
) -> GeoDataFrame: ...
