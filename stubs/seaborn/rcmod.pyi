from _typeshed import Incomplete

def set_theme(
    context: str = ...,
    style: str = ...,
    palette: str = ...,
    font: str = ...,
    font_scale: int = ...,
    color_codes: bool = ...,
    rc: Incomplete | None = ...,
) -> None: ...
def set(*args, **kwargs) -> None: ...
def reset_defaults() -> None: ...
def reset_orig() -> None: ...
def axes_style(style: Incomplete | None = ..., rc: Incomplete | None = ...): ...
def set_style(style: Incomplete | None = ..., rc: Incomplete | None = ...) -> None: ...
def plotting_context(context: Incomplete | None = ..., font_scale: int = ..., rc: Incomplete | None = ...): ...
def set_context(context: Incomplete | None = ..., font_scale: int = ..., rc: Incomplete | None = ...) -> None: ...

class _RCAesthetics(dict):
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, exc_tb) -> None: ...
    def __call__(self, func): ...

class _AxesStyle(_RCAesthetics): ...
class _PlottingContext(_RCAesthetics): ...

def set_palette(palette, n_colors: Incomplete | None = ..., desat: Incomplete | None = ..., color_codes: bool = ...) -> None: ...
