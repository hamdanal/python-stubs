from __future__ import annotations

from types import NoneType
from typing import Literal as L  # noqa: F401

import numpy as np
import shapely
from numpy.typing import NDArray
from shapely import Geometry, Point, Polygon
from shapely.geometry.base import BaseGeometry
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
PO: Polygon = P.buffer(1)
PO2: Polygon = Point(5, 6).buffer(1)


def test_has_z() -> None:
    check(assert_type(shapely.has_z(P), np.bool), np.bool)
    check(assert_type(shapely.has_z(None), np.bool), np.bool)
    check(assert_type(shapely.has_z([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.has_z([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_ccw() -> None:
    check(assert_type(shapely.is_ccw(P), np.bool), np.bool)
    check(assert_type(shapely.is_ccw(None), np.bool), np.bool)
    check(assert_type(shapely.is_ccw([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_ccw([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_closed() -> None:
    check(assert_type(shapely.is_closed(P), np.bool), np.bool)
    check(assert_type(shapely.is_closed(None), np.bool), np.bool)
    check(assert_type(shapely.is_closed([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_closed([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_empty() -> None:
    check(assert_type(shapely.is_empty(P), np.bool), np.bool)
    check(assert_type(shapely.is_empty(None), np.bool), np.bool)
    check(assert_type(shapely.is_empty([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_empty([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_geometry() -> None:
    check(assert_type(shapely.is_geometry(P), "np.bool[L[True]]"), np.bool)
    check(assert_type(shapely.is_geometry(None), "np.bool[L[False]]"), np.bool)
    check(assert_type(shapely.is_geometry([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_geometry([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)

    x: Geometry | str | None = (shapely.from_wkt(P.wkt), "string", None)[min(1, 0)]
    if shapely.is_geometry(x):
        assert_type(x, BaseGeometry)


def test_is_missing() -> None:
    check(assert_type(shapely.is_missing(P), "np.bool[L[False]]"), np.bool)
    check(assert_type(shapely.is_missing(None), "np.bool[L[True]]"), np.bool)
    check(assert_type(shapely.is_missing([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_missing([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)

    x: Geometry | str | None = (shapely.from_wkt(P.wkt), "string", None)[max(1, 2)]
    assert shapely.is_missing(x)
    assert_type(x, None)


def test_is_prepared() -> None:
    check(assert_type(shapely.is_prepared(P), np.bool), np.bool)
    check(assert_type(shapely.is_prepared(None), np.bool), np.bool)
    check(assert_type(shapely.is_prepared([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_prepared([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_valid_input() -> None:
    check(assert_type(shapely.is_valid_input(P), "np.bool[L[True]]"), np.bool)
    check(assert_type(shapely.is_valid_input(None), "np.bool[L[True]]"), np.bool)
    check(assert_type(shapely.is_valid_input([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_valid_input([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)

    x: Geometry | str | None = (shapely.from_wkt(P.wkt), "string", None)[min(1, 0)]
    assert shapely.is_valid_input(x)
    assert_type(x, BaseGeometry | None)


def test_is_ring() -> None:
    check(assert_type(shapely.is_ring(P), np.bool), np.bool)
    check(assert_type(shapely.is_ring(None), np.bool), np.bool)
    check(assert_type(shapely.is_ring([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_ring([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_simple() -> None:
    check(assert_type(shapely.is_simple(P), np.bool), np.bool)
    check(assert_type(shapely.is_simple(None), np.bool), np.bool)
    check(assert_type(shapely.is_simple([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_simple([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_valid() -> None:
    check(assert_type(shapely.is_valid(P), np.bool), np.bool)
    check(assert_type(shapely.is_valid(None), np.bool), np.bool)
    check(assert_type(shapely.is_valid([P]), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(assert_type(shapely.is_valid([None]), NDArray[np.bool]), np.ndarray, dtype=np.bool)


def test_is_valid_reason() -> None:
    check(assert_type(shapely.is_valid_reason(P), str), str)
    check(assert_type(shapely.is_valid_reason(None), None), NoneType)
    check(assert_type(shapely.is_valid_reason([P]), NDArray[np.object_]), np.ndarray, dtype=str)
    check(
        assert_type(shapely.is_valid_reason([None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )


def test_crosses() -> None:
    check(assert_type(shapely.crosses(PO, P), np.bool), np.bool)
    check(assert_type(shapely.crosses(P, None), np.bool), np.bool)
    check(assert_type(shapely.crosses(None, None), np.bool), np.bool)
    check(assert_type(shapely.crosses([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.crosses([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_contains() -> None:
    check(assert_type(shapely.contains(PO, P), np.bool), np.bool)
    check(assert_type(shapely.contains(P, None), np.bool), np.bool)
    check(assert_type(shapely.contains(None, None), np.bool), np.bool)
    check(assert_type(shapely.contains([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.contains([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_contains_properly() -> None:
    check(assert_type(shapely.contains_properly(PO, P), np.bool), np.bool)
    check(assert_type(shapely.contains_properly(P, None), np.bool), np.bool)
    check(assert_type(shapely.contains_properly(None, None), np.bool), np.bool)
    check(
        assert_type(shapely.contains_properly([P], None), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.contains_properly([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_covered_by() -> None:
    check(assert_type(shapely.covered_by(PO, P), np.bool), np.bool)
    check(assert_type(shapely.covered_by(P, None), np.bool), np.bool)
    check(assert_type(shapely.covered_by(None, None), np.bool), np.bool)
    check(assert_type(shapely.covered_by([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.covered_by([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_covers() -> None:
    check(assert_type(shapely.covers(PO, P), np.bool), np.bool)
    check(assert_type(shapely.covers(P, None), np.bool), np.bool)
    check(assert_type(shapely.covers(None, None), np.bool), np.bool)
    check(assert_type(shapely.covers([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.covers([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_disjoint() -> None:
    check(assert_type(shapely.disjoint(PO, P), np.bool), np.bool)
    check(assert_type(shapely.disjoint(P, None), np.bool), np.bool)
    check(assert_type(shapely.disjoint(None, None), np.bool), np.bool)
    check(assert_type(shapely.disjoint([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.disjoint([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_equals() -> None:
    check(assert_type(shapely.equals(PO, P), np.bool), np.bool)
    check(assert_type(shapely.equals(P, None), np.bool), np.bool)
    check(assert_type(shapely.equals(None, None), np.bool), np.bool)
    check(assert_type(shapely.equals([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.equals([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_intersects() -> None:
    check(assert_type(shapely.intersects(PO, P), np.bool), np.bool)
    check(assert_type(shapely.intersects(P, None), np.bool), np.bool)
    check(assert_type(shapely.intersects(None, None), np.bool), np.bool)
    check(assert_type(shapely.intersects([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.intersects([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_overlaps() -> None:
    check(assert_type(shapely.overlaps(PO, P), np.bool), np.bool)
    check(assert_type(shapely.overlaps(P, None), np.bool), np.bool)
    check(assert_type(shapely.overlaps(None, None), np.bool), np.bool)
    check(assert_type(shapely.overlaps([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.overlaps([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_touches() -> None:
    check(assert_type(shapely.touches(PO, P), np.bool), np.bool)
    check(assert_type(shapely.touches(P, None), np.bool), np.bool)
    check(assert_type(shapely.touches(None, None), np.bool), np.bool)
    check(assert_type(shapely.touches([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.touches([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_within() -> None:
    check(assert_type(shapely.within(PO, P), np.bool), np.bool)
    check(assert_type(shapely.within(P, None), np.bool), np.bool)
    check(assert_type(shapely.within(None, None), np.bool), np.bool)
    check(assert_type(shapely.within([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.within([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )


def test_equals_exact() -> None:
    check(assert_type(shapely.equals_exact(PO, P), np.bool), np.bool)
    check(assert_type(shapely.equals_exact(P, None), np.bool), np.bool)
    check(assert_type(shapely.equals_exact(None, None), np.bool), np.bool)
    check(assert_type(shapely.equals_exact([P], None), NDArray[np.bool]), np.ndarray, dtype=np.bool)
    check(
        assert_type(shapely.equals_exact([PO, P, None], [PO2, None, None]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )

    check(
        assert_type(shapely.equals_exact(PO, P, tolerance=[0.01, 1]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.equals_exact(P, None, tolerance=[0.01, 1]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.equals_exact(None, None, tolerance=[0.01, 1]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.equals_exact([P], None, tolerance=[0.01, 1]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.equals_exact([PO, P, None], [PO2, None, None], tolerance=[0.01, 1, 0.5]),
            NDArray[np.bool],
        ),
        np.ndarray,
        dtype=np.bool,
    )


def test_relate() -> None:
    check(assert_type(shapely.relate(PO, P), str), str)
    check(assert_type(shapely.relate(P, None), None), NoneType)
    check(assert_type(shapely.relate(None, None), None), NoneType)
    check(assert_type(shapely.relate([P, None], PO), NDArray[np.object_]), np.ndarray, dtype=str)
    check(
        assert_type(shapely.relate([PO, P, None], [PO2, None, None]), NDArray[np.object_]),
        np.ndarray,
        dtype=str,
    )


def test_relate_pattern() -> None:
    check(assert_type(shapely.relate_pattern(PO, P, pattern="T*F**F***"), np.bool), np.bool)
    check(assert_type(shapely.relate_pattern(P, None, pattern="T*F**F***"), np.bool), np.bool)
    check(assert_type(shapely.relate_pattern(None, None, pattern="T*F**F***"), np.bool), np.bool)
    check(
        assert_type(shapely.relate_pattern([P], None, pattern="T*F**F***"), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.relate_pattern([PO, P, None], [PO2, None, None], pattern="T*F**F***"),
            NDArray[np.bool],
        ),
        np.ndarray,
        dtype=np.bool,
    )


def test_dwithin() -> None:
    check(assert_type(shapely.dwithin(PO, P, distance=0.01), np.bool), np.bool)
    check(assert_type(shapely.dwithin(P, None, distance=0.01), np.bool), np.bool)
    check(assert_type(shapely.dwithin(None, None, distance=0.01), np.bool), np.bool)
    check(
        assert_type(shapely.dwithin([P], None, distance=0.01), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.dwithin([PO, P, None], [PO2, None, None], distance=0.01), NDArray[np.bool]
        ),
        np.ndarray,
        dtype=np.bool,
    )


def test_contains_xy() -> None:
    check(assert_type(shapely.contains_xy(PO, 0.5, 0.5), np.bool), np.bool)
    check(assert_type(shapely.contains_xy(None, 0.5, 0.5), np.bool), np.bool)
    check(
        assert_type(shapely.contains_xy(PO, [0.5], [0.5]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.contains_xy(PO, [0.5], 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.contains_xy(PO, [[0.5, 0.5]]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.contains_xy([P], 0.5, 0.5), NDArray[np.bool]), np.ndarray, dtype=np.bool
    )
    check(
        assert_type(shapely.contains_xy([None], 0.5, 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.contains_xy([P, None], 0.5, 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.contains_xy([PO, P, None], [0.5, 0.4, 0.3], [0.5, 0.4, 0.3]), NDArray[np.bool]
        ),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.contains_xy([PO, P, None], [(0.5, 0.5), (0.4, 0.4), (0.3, 0.3)]),
            NDArray[np.bool],
        ),
        np.ndarray,
        dtype=np.bool,
    )


def test_intersects_xy() -> None:
    check(assert_type(shapely.intersects_xy(PO, 0.5, 0.5), np.bool), np.bool)
    check(assert_type(shapely.intersects_xy(None, 0.5, 0.5), np.bool), np.bool)
    check(
        assert_type(shapely.intersects_xy(PO, [0.5], [0.5]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.intersects_xy(PO, [0.5], 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.intersects_xy(PO, [[0.5, 0.5]]), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.intersects_xy([P], 0.5, 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.intersects_xy([None], 0.5, 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(shapely.intersects_xy([P, None], 0.5, 0.5), NDArray[np.bool]),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.intersects_xy([PO, P, None], [0.5, 0.4, 0.3], [0.5, 0.4, 0.3]), NDArray[np.bool]
        ),
        np.ndarray,
        dtype=np.bool,
    )
    check(
        assert_type(
            shapely.intersects_xy([PO, P, None], [(0.5, 0.5), (0.4, 0.4), (0.3, 0.3)]),
            NDArray[np.bool],
        ),
        np.ndarray,
        dtype=np.bool,
    )
