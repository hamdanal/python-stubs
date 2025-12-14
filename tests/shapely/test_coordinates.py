from __future__ import annotations

from types import NoneType
from typing import assert_type

import numpy as np
import pytest
import shapely
from numpy.typing import ArrayLike, NDArray
from shapely import Point
from shapely.geometry.base import BaseGeometry

from tests import check

P = Point(1, 2)


def test_transform() -> None:
    check(assert_type(shapely.transform(P, lambda x: x), Point), Point)
    check(assert_type(shapely.transform(P, lambda x: x + 1.0), Point), Point)
    check(assert_type(shapely.transform(None, lambda x: x), None), NoneType)
    check(
        assert_type(shapely.transform(shapely.from_wkt(P.wkt), lambda x: x + 1.0), BaseGeometry),
        Point,
    )

    def transformer(coords: ArrayLike) -> NDArray[np.float64]:
        return np.asarray(coords) + 1

    check(assert_type(shapely.transform(P, transformer), Point), Point)

    check(
        assert_type(shapely.transform([P], lambda x: x + 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.transform([None], lambda x: x + 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=NoneType,
    )
    check(
        assert_type(shapely.transform((P, None), lambda x: x + 1.0), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )


def test_count_coordinates() -> None:
    check(assert_type(shapely.count_coordinates(P), int), int)
    check(assert_type(shapely.count_coordinates(None), int), int)
    check(assert_type(shapely.count_coordinates([P]), int), int)
    check(assert_type(shapely.count_coordinates([None]), int), int)
    check(assert_type(shapely.count_coordinates((P, None)), int), int)


def test_get_coordinates() -> None:
    check(
        assert_type(shapely.get_coordinates(P), NDArray[np.float64]), np.ndarray, dtype=np.float64
    )
    check(assert_type(shapely.get_coordinates(None), NDArray[np.float64]), np.ndarray)
    check(
        assert_type(shapely.get_coordinates([P]), NDArray[np.float64]), np.ndarray, dtype=np.float64
    )
    check(assert_type(shapely.get_coordinates([None]), NDArray[np.float64]), np.ndarray)
    check(
        assert_type(shapely.get_coordinates((P, None)), NDArray[np.float64]),
        np.ndarray,
        dtype=np.float64,
    )
    check(
        assert_type(shapely.get_coordinates(P, include_z=True), NDArray[np.float64]),
        np.ndarray,
        dtype=np.float64,
    )
    with_index = shapely.get_coordinates(P, return_index=True)
    check(
        assert_type(with_index, tuple[NDArray[np.float64], NDArray[np.int64]]),
        tuple,
        dtype=np.ndarray,
    )
    coords, idx = with_index
    check(coords, np.ndarray, dtype=np.float64)
    check(idx, np.ndarray, dtype=np.int64)
    check(
        assert_type(
            shapely.get_coordinates([P, None], return_index=True),
            tuple[NDArray[np.float64], NDArray[np.int64]],
        ),
        tuple,
        dtype=np.ndarray,
    )

    # bool fallback
    check(
        assert_type(
            shapely.get_coordinates(P, return_index=bool(1)),
            tuple[NDArray[np.float64], NDArray[np.int64]] | NDArray[np.float64],
        ),
        tuple,
        dtype=np.ndarray,
    )
    check(
        assert_type(
            shapely.get_coordinates(P, return_index=bool(0)),
            tuple[NDArray[np.float64], NDArray[np.int64]] | NDArray[np.float64],
        ),
        np.ndarray,
        dtype=np.float64,
    )


def test_set_coordinates() -> None:
    check(assert_type(shapely.set_coordinates(P, [1.0, 1]), Point), Point)
    check(assert_type(shapely.set_coordinates(P, [(1, 1.0)]), Point), Point)
    check(
        assert_type(shapely.set_coordinates([P], [[1, 1]]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.set_coordinates([P, None], [[1, 1]]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    check(
        assert_type(shapely.set_coordinates((P, None), [[1, 1]]), NDArray[np.object_]),
        np.ndarray,
        dtype=Point,
    )
    with pytest.raises(Exception):
        shapely.set_coordinates(None, [])  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.set_coordinates(None, [1, 1])  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
    with pytest.raises(Exception):
        shapely.set_coordinates(None, [[1, 1]])  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportArgumentType]
