from _typeshed import Incomplete
from collections.abc import Hashable, Iterable, Mapping
from datetime import date, datetime, timedelta
from typing import Any
from typing_extensions import TypeAlias

from matplotlib.colors import Colormap, Normalize
from numpy import ndarray
from pandas import DataFrame, Index, Series, Timedelta, Timestamp

ColumnName: TypeAlias = str | bytes | date | datetime | timedelta | bool | complex | Timestamp | Timedelta
Vector: TypeAlias = Series | Index | ndarray
VariableSpec: TypeAlias = ColumnName | Vector | None
VariableSpecList: TypeAlias = list[VariableSpec] | Index | None
DataSource: TypeAlias = DataFrame | Mapping[Hashable, Vector] | None
OrderSpec: TypeAlias = Iterable | None
NormSpec: TypeAlias = tuple[float | None, float | None] | Normalize | None
PaletteSpec: TypeAlias = str | list | dict | Colormap | None
DiscreteValueSpec: TypeAlias = dict | list | None
ContinuousValueSpec: TypeAlias = tuple[float, float] | list[float] | dict[Any, float] | None

class Default: ...

default: Incomplete
