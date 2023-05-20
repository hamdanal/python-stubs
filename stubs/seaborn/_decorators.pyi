from typing import TypeVar

_T = TypeVar("_T", bound=type)

def share_init_params_with_map(cls: _T) -> _T: ...
