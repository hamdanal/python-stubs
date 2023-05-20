from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, TypeVar
from typing_extensions import Literal, TypeAlias

__all__ = [
    "set_theme",
    "set",
    "reset_defaults",
    "reset_orig",
    "axes_style",
    "set_style",
    "plotting_context",
    "set_context",
    "set_palette",
]

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_F = TypeVar("_F", bound=Callable)

_Context: TypeAlias = Literal["paper", "notebook", "talk", "poster"] | dict[str, Any]
_Style: TypeAlias = Literal["white", "dark", "whitegrid", "darkgrid", "ticks"] | dict[str, Any]

def set_theme(
    context: _Context = "notebook",
    style: _Style = "darkgrid",
    palette: str = "deep",
    font: str = "sans-serif",
    font_scale: float = 1,
    color_codes: bool = True,
    rc: dict[str, Any] | None = None,
) -> None: ...
def set(*args, **kwargs) -> None: ...
def reset_defaults() -> None: ...
def reset_orig() -> None: ...
def axes_style(style: _Style | None = None, rc: dict[str, Any] | None = None): ...
def set_style(style: _Style | None = None, rc: dict[str, Any] | None = None) -> None: ...
def plotting_context(
    context: _Context | None = None, font_scale: float = 1, rc: dict[str, Any] | None = None
) -> _PlottingContext: ...
def set_context(context: _Context | None = None, font_scale: float = 1, rc: dict[str, Any] | None = None) -> None: ...

class _RCAesthetics(dict[_KT, _VT]):
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, exc_tb) -> None: ...
    def __call__(self, func: _F) -> _F: ...

class _AxesStyle(_RCAesthetics[_KT, _VT]): ...
class _PlottingContext(_RCAesthetics[_KT, _VT]): ...

def set_palette(
    palette: Incomplete, n_colors: int | None = None, desat: float | None = None, color_codes: bool = False
) -> None: ...
