from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar

_T = TypeVar("_T")

def jit(*args: Incomplete, **kwargs: Incomplete) -> Callable[[_T], _T]: ...
def marker(*args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

int32 = marker
