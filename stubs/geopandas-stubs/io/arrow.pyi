import os
from _typeshed import SupportsGetItem, SupportsKeysAndGetItem
from collections.abc import Iterable
from typing import Any, Final

from geopandas.geodataframe import GeoDataFrame

METADATA_VERSION: Final[str]
SUPPORTED_VERSIONS: Final[list[str]]
GEOARROW_ENCODINGS: Final[list[str]]
SUPPORTED_ENCODINGS: Final[list[str]]

def _read_parquet(
    path: str | os.PathLike[str],
    columns: Iterable[str] | None = None,
    storage_options: SupportsKeysAndGetItem[str, Any] | None = None,
    bbox: SupportsGetItem[int, float] | None = None,
    **kwargs: Any,  # kwargs passed to pyarrow.parquet.read_table
) -> GeoDataFrame: ...
def _read_feather(
    path: str | os.PathLike[str],
    columns: Iterable[str] | None = None,
    **kwargs: Any,  # kwargs passed to pyarrow.feather.read_table
) -> GeoDataFrame: ...
