from __future__ import annotations

from typing import Literal

import numpy as np
import shapely
from numpy.typing import NDArray
from shapely import Point, Polygon
from shapely.geometry.base import BaseGeometry
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
PO: Polygon = P.buffer(1)
PO2: Polygon = Point(5, 6).buffer(1)

# TODO: complete the tests


def test_has_z() -> None:
    check(assert_type(shapely.has_z(P), bool), np.bool_)
    check(assert_type(shapely.has_z(None), bool), np.bool_)
    check(assert_type(shapely.has_z([P]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(shapely.has_z([None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)


def test_is_ccw() -> None:
    check(assert_type(shapely.is_ccw(P), bool), np.bool_)
    check(assert_type(shapely.is_ccw(None), bool), np.bool_)
    check(assert_type(shapely.is_ccw([P]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(shapely.is_ccw([None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)


def test_is_closed() -> None:
    check(assert_type(shapely.is_closed(P), bool), np.bool_)
    check(assert_type(shapely.is_closed(None), bool), np.bool_)
    check(assert_type(shapely.is_closed([P]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(shapely.is_closed([None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)


def test_is_empty() -> None:
    check(assert_type(shapely.is_empty(P), bool), np.bool_)
    check(assert_type(shapely.is_empty(None), bool), np.bool_)
    check(assert_type(shapely.is_empty([P]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(shapely.is_empty([None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)


def test_is_geometry() -> None:
    check(assert_type(shapely.is_geometry(P), Literal[True]), np.bool_)
    check(assert_type(shapely.is_geometry(None), bool), np.bool_)
    check(assert_type(shapely.is_geometry([P]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)
    check(assert_type(shapely.is_geometry([None]), NDArray[np.bool_]), np.ndarray, dtype=np.bool_)

    x: BaseGeometry | None = [shapely.from_wkt(P.wkt), None][0]
    if shapely.is_geometry(x):
        assert_type(x, BaseGeometry)
