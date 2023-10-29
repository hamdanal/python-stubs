import os
from _typeshed import SupportsRead
from typing import Any, Literal, overload

import pandas as pd

from ..geodataframe import GeoDataFrame

@overload
def _read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox=None,
    mask=None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: Literal[False] = False,
    **kwargs,
) -> GeoDataFrame: ...
@overload
def _read_file(
    filename: str | os.PathLike[str] | SupportsRead[Any],
    bbox=None,
    mask=None,
    rows: int | slice | None = None,
    engine: Literal["fiona", "pyogrio"] | None = None,
    *,
    ignore_geometry: Literal[True],
    **kwargs,
) -> pd.DataFrame: ...

read_file = _read_file  # deprecated

def to_file(*args, **kwargs) -> None: ...  # deprecated
def infer_schema(df: GeoDataFrame) -> dict[str, Any]: ...
