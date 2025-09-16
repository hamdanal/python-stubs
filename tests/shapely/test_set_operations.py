from __future__ import annotations

from types import NoneType

import numpy as np
import pytest
import shapely
from numpy.typing import NDArray
from shapely import Point, Polygon
from shapely.geometry.base import BaseGeometry
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
PO: Polygon = P.buffer(1)
PO2: Polygon = Point(5, 6).buffer(1)


def test_difference() -> None:
    check(assert_type(shapely.difference(P, P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.difference(P, None), None), NoneType)
    check(assert_type(shapely.difference(None, P), None), NoneType)
    check(assert_type(shapely.difference(None, None), None), NoneType)
    check(
        assert_type(shapely.difference([P], P), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(
        assert_type(shapely.difference(P, [P]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry
    )
    check(
        assert_type(shapely.difference([P], None), NDArray[np.object_]), np.ndarray, dtype=NoneType
    )
    check(
        assert_type(shapely.difference([P], [None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.difference([None], None), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )


def test_intersection() -> None:
    check(assert_type(shapely.intersection(P, P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.intersection(P, None), None), NoneType)
    check(assert_type(shapely.intersection(None, P), None), NoneType)
    check(assert_type(shapely.intersection(None, None), None), NoneType)
    check(
        assert_type(shapely.intersection([P], P), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.intersection(P, [P]), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.intersection([P], None), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.intersection([P], [None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.intersection([None], None), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )


def test_intersection_all() -> None:
    check(assert_type(shapely.intersection_all(P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.intersection_all(None), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.intersection_all([P]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.intersection_all([None]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.intersection_all([P, P]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.intersection_all([P, None]), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.intersection_all([P], axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(shapely.intersection_all([[P]], axis=0), BaseGeometry | NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.intersection_all([None], axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(shapely.intersection_all([[None]], axis=0), BaseGeometry | NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_symmetric_difference() -> None:
    check(assert_type(shapely.symmetric_difference(P, P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.symmetric_difference(P, None), None), NoneType)
    check(assert_type(shapely.symmetric_difference(None, P), None), NoneType)
    check(assert_type(shapely.symmetric_difference(None, None), None), NoneType)
    check(
        assert_type(shapely.symmetric_difference([P], P), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.symmetric_difference(P, [P]), NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.symmetric_difference([P], None), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.symmetric_difference([P], [None]), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.symmetric_difference([None], None), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )


def test_symmetric_difference_all() -> None:
    with pytest.deprecated_call():
        check(assert_type(shapely.symmetric_difference_all(P), BaseGeometry), BaseGeometry)  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
        check(assert_type(shapely.symmetric_difference_all(None), BaseGeometry), BaseGeometry)  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
        check(assert_type(shapely.symmetric_difference_all([P]), BaseGeometry), BaseGeometry)  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
        check(assert_type(shapely.symmetric_difference_all([None]), BaseGeometry), BaseGeometry)  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
        check(assert_type(shapely.symmetric_difference_all([P, P]), BaseGeometry), BaseGeometry)  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
        check(assert_type(shapely.symmetric_difference_all([P, None]), BaseGeometry), BaseGeometry)  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
        check(
            assert_type(
                shapely.symmetric_difference_all([P], axis=0),  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
                BaseGeometry | NDArray[np.object_],
            ),
            BaseGeometry,
        )
        check(
            assert_type(
                shapely.symmetric_difference_all([[P]], axis=0),  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
                BaseGeometry | NDArray[np.object_],
            ),
            np.ndarray,
            dtype=BaseGeometry,
        )
        check(
            assert_type(
                shapely.symmetric_difference_all([None], axis=0),  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
                BaseGeometry | NDArray[np.object_],
            ),
            BaseGeometry,
        )
        check(
            assert_type(
                shapely.symmetric_difference_all([[None]], axis=0),  # type: ignore[deprecated] # pyright: ignore[reportDeprecated]
                BaseGeometry | NDArray[np.object_],
            ),
            np.ndarray,
            dtype=BaseGeometry,
        )


def test_union() -> None:
    check(assert_type(shapely.union(P, P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.union(P, None), None), NoneType)
    check(assert_type(shapely.union(None, P), None), NoneType)
    check(assert_type(shapely.union(None, None), None), NoneType)
    check(assert_type(shapely.union([P], P), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(shapely.union(P, [P]), NDArray[np.object_]), np.ndarray, dtype=BaseGeometry)
    check(assert_type(shapely.union([P], None), NDArray[np.object_]), np.ndarray, dtype=NoneType)
    check(assert_type(shapely.union([P], [None]), NDArray[np.object_]), np.ndarray, dtype=NoneType)
    check(assert_type(shapely.union([None], None), NDArray[np.object_]), np.ndarray, dtype=NoneType)


def test_union_all() -> None:
    check(assert_type(shapely.union_all(P), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.union_all(None), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.union_all([P]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.union_all([None]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.union_all([P, P]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.union_all([P, None]), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.union_all([P], axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(shapely.union_all([[P]], axis=0), BaseGeometry | NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(
        assert_type(shapely.union_all([None], axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(shapely.union_all([[None]], axis=0), BaseGeometry | NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )


def test_coverage_union() -> None:
    check(assert_type(shapely.coverage_union(PO, PO2), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union(PO, None), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union(None, PO), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union([PO], [PO2]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union([PO], [None]), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.coverage_union(PO, PO2, axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(
            shapely.coverage_union([PO], [PO2], axis=0), BaseGeometry | NDArray[np.object_]
        ),
        np.ndarray,
        dtype=BaseGeometry,
    )
    check(assert_type(shapely.coverage_union(None, None), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union([None], [None]), BaseGeometry), BaseGeometry)


def test_coverage_union_all() -> None:
    check(assert_type(shapely.coverage_union_all(PO), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union_all([PO]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union_all([PO, PO2]), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union_all([PO, None]), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.coverage_union_all([PO], axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(shapely.coverage_union_all([[PO]], axis=0), BaseGeometry | NDArray[np.object_]),
        np.ndarray,
        dtype=BaseGeometry,
    )

    check(assert_type(shapely.coverage_union_all(None), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.coverage_union_all([None]), BaseGeometry), BaseGeometry)
    check(
        assert_type(shapely.coverage_union_all([None], axis=0), BaseGeometry | NDArray[np.object_]),
        BaseGeometry,
    )
    check(
        assert_type(
            shapely.coverage_union_all([[None]], axis=0), BaseGeometry | NDArray[np.object_]
        ),
        np.ndarray,
        dtype=BaseGeometry,
    )
