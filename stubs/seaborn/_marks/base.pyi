from typing import Any
from typing_extensions import TypeAlias

from matplotlib.artist import Artist as Artist
from numpy import ndarray
from pandas import DataFrame as DataFrame
from seaborn._core.exceptions import PlotSpecError as PlotSpecError
from seaborn._core.properties import (
    PROPERTIES as PROPERTIES,
    DashPattern as DashPattern,
    DashPatternWithOffset as DashPatternWithOffset,
    Property as Property,
    RGBATuple as RGBATuple,
)
from seaborn._core.scales import Scale as Scale

class Mappable:
    def __init__(
        self, val: Any = ..., depend: str | None = ..., rc: str | None = ..., auto: bool = ..., grouping: bool = ...
    ) -> None: ...
    @property
    def depend(self) -> Any: ...
    @property
    def grouping(self) -> bool: ...
    @property
    def default(self) -> Any: ...

MappableBool: TypeAlias = bool | Mappable
MappableString: TypeAlias = str | Mappable
MappableFloat: TypeAlias = float | Mappable
MappableColor: TypeAlias = str | tuple | Mappable
MappableStyle: TypeAlias = str | DashPattern | DashPatternWithOffset | Mappable

class Mark:
    artist_kws: dict
    def __init__(self, artist_kws) -> None: ...

def resolve_properties(mark: Mark, data: DataFrame, scales: dict[str, Scale]) -> dict[str, Any]: ...
def resolve_color(
    mark: Mark, data: DataFrame | dict, prefix: str = ..., scales: dict[str, Scale] | None = ...
) -> RGBATuple | ndarray: ...
def document_properties(mark): ...
