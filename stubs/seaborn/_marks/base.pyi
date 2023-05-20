from dataclasses import dataclass
from typing import Any, TypeVar
from typing_extensions import TypeAlias

from numpy import ndarray
from pandas import DataFrame
from seaborn._core.properties import DashPattern, DashPatternWithOffset, RGBATuple
from seaborn._core.scales import Scale

_MarkT = TypeVar("_MarkT", bound=type[Mark])

class Mappable:
    def __init__(
        self, val: Any = None, depend: str | None = None, rc: str | None = None, auto: bool = False, grouping: bool = True
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

@dataclass
class Mark:
    artist_kws: dict = ...

def resolve_properties(mark: Mark, data: DataFrame, scales: dict[str, Scale]) -> dict[str, Any]: ...
def resolve_color(
    mark: Mark, data: DataFrame | dict, prefix: str = "", scales: dict[str, Scale] | None = None
) -> RGBATuple | ndarray: ...
def document_properties(mark: _MarkT) -> _MarkT: ...
