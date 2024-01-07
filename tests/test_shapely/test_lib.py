from typing import Any

import numpy as np
from shapely import Point, lib
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)


def test_ufuncs() -> None:
    # TODO all ufuncs return `Any` now
    check(assert_type(lib.area(P), Any), float)
    check(assert_type(lib.area([P, P]), Any), np.ndarray, float)
