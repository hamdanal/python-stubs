from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import TypeAlias

from geopandas.geodataframe import GeoDataFrame

_GeoCoder: TypeAlias = Any

def geocode(strings: Iterable[str], provider: str | _GeoCoder | None = None, **kwargs) -> GeoDataFrame: ...
def reverse_geocode(points: Incomplete, provider: str | _GeoCoder | None = None, **kwargs) -> GeoDataFrame: ...
