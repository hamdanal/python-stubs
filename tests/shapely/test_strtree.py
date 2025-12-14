from __future__ import annotations

from typing import Any

import numpy as np
import pytest
import shapely
from numpy.typing import NDArray
from shapely import Point
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
POINTS = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
TREE = shapely.STRtree(POINTS)
BOXES = [shapely.box(0, 0, 1, 1), shapely.box(2, 2, 3, 3)]


def test_strtree() -> None:
    with pytest.raises(Exception):
        shapely.STRtree(P)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
    check(assert_type(TREE.geometries, NDArray[np.object_]), np.ndarray, dtype=Point)
    _ = len(TREE)


def test_strtree_query() -> None:
    check(
        assert_type(TREE.query(shapely.box(0, 0, 1, 1)), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(assert_type(TREE.query(None), NDArray[np.int64]), np.ndarray)
    check(
        assert_type(TREE.query((shapely.box(0, 0, 1, 1), None)), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(assert_type(TREE.query(BOXES), NDArray[np.int64]), np.ndarray, dtype=np.int64)
    check(assert_type(TREE.query(np.array(BOXES)), NDArray[np.int64]), np.ndarray, dtype=np.int64)

    tree = shapely.STRtree(
        [shapely.box(0, 0, 0.5, 0.5), shapely.box(0.5, 0.5, 1, 1), shapely.box(1, 1, 2, 2)]
    )
    check(
        assert_type(tree.query(shapely.box(0, 0, 1, 1), predicate="contains"), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(
        assert_type(
            tree.query(Point(0.75, 0.75), predicate="dwithin", distance=0.5), NDArray[np.int64]
        ),
        np.ndarray,
        dtype=np.int64,
    )
    check(
        assert_type(tree.query(BOXES, predicate="dwithin", distance=0.5), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(
        assert_type(tree.query(BOXES, predicate="dwithin", distance=[0.5, 0.6]), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )

    with pytest.raises(Exception):  # needs distance
        tree.query(BOXES, predicate="dwithin")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]

    with pytest.raises(Exception):  # invalid predicate
        tree.query(BOXES, predicate="yes")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType]


def test_strtree_nearest() -> None:
    check(assert_type(TREE.nearest(shapely.box(0, 0, 1, 1)), np.int64 | Any), np.int64)
    check(
        assert_type(TREE.nearest([shapely.box(0, 0, 1, 1)]), NDArray[np.int64] | Any),
        np.ndarray,
        dtype=np.int64,
    )
    check(assert_type(TREE.nearest(BOXES), NDArray[np.int64] | Any), np.ndarray, dtype=np.int64)
    check(
        assert_type(TREE.nearest(np.array(BOXES)), NDArray[np.int64] | Any),
        np.ndarray,
        dtype=np.int64,
    )

    with pytest.raises(Exception):
        TREE.nearest(None)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        TREE.nearest((shapely.box(0, 0, 1, 1), None))  # type: ignore[arg-type] # pyright: ignore[reportCallIssue, reportArgumentType]


def test_strtree_query_nearest() -> None:
    check(
        assert_type(TREE.query_nearest(Point(0.25, 0.25)), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(assert_type(TREE.query_nearest(None), NDArray[np.int64]), np.ndarray)
    check(
        assert_type(TREE.query_nearest([Point(2.25, 2.25), Point(1, 1)]), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(
        assert_type(TREE.query_nearest((Point(2.25, 2.25), None)), NDArray[np.int64]),
        np.ndarray,
        dtype=np.int64,
    )
    check(
        assert_type(
            TREE.query_nearest(shapely.box(1, 1, 3, 3), all_matches=False), NDArray[np.int64]
        ),
        np.ndarray,
        dtype=np.int64,
    )
    with_distance = TREE.query_nearest(Point(0.5, 0.5), return_distance=True)
    check(
        assert_type(with_distance, tuple[NDArray[np.int64], NDArray[np.float64]]),
        tuple,
        dtype=np.ndarray,
    )
    check(assert_type(with_distance[0], NDArray[np.int64]), np.ndarray, dtype=np.int64)
    check(assert_type(with_distance[1], NDArray[np.float64]), np.ndarray, dtype=np.float64)
    check(
        assert_type(
            TREE.query_nearest([Point(0.5, 0.5), Point(1, 1)], return_distance=True),
            tuple[NDArray[np.int64], NDArray[np.float64]],
        ),
        tuple,
        dtype=np.ndarray,
    )

    check(
        assert_type(
            TREE.query_nearest(Point(0.5, 0.5), return_distance=bool(0.5)),
            tuple[NDArray[np.int64], NDArray[np.float64]] | NDArray[np.int64],
        ),
        tuple,
        dtype=np.ndarray,
    )
