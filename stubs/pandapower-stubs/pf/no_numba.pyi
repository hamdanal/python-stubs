from _typeshed import Incomplete
from collections.abc import Callable

def jit[T](*args: Incomplete, **kwargs: Incomplete) -> Callable[[T], T]: ...
def marker(*args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

int32 = marker
