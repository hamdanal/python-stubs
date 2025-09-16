from __future__ import annotations

import numpy as np
import shapely
from numpy.typing import NDArray
from shapely import LineString, MultiPoint, Point, Polygon
from typing_extensions import assert_type

from tests import check

P = Point(1, 2)
LS = LineString([(0, 0), (1, 1)])
PO: Polygon = P.buffer(1)
MP = MultiPoint([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])


def test_area() -> None:
    check(assert_type(shapely.area(PO), np.float64), np.float64)
    check(assert_type(shapely.area(None), np.float64), np.float64)
    check(assert_type(shapely.area([P, LS]), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.area((P, LS, None)), NDArray[np.float64]), np.ndarray, dtype=float)


def test_distance() -> None:
    check(assert_type(shapely.distance(PO, P), np.float64), np.float64)
    check(assert_type(shapely.distance(PO, None), np.float64), np.float64)
    check(assert_type(shapely.distance(None, PO), np.float64), np.float64)
    check(assert_type(shapely.distance(None, None), np.float64), np.float64)
    check(
        assert_type(shapely.distance([P, LS], None), NDArray[np.float64]), np.ndarray, dtype=float
    )
    check(
        assert_type(shapely.distance((P, LS, None), [PO, None, None]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )


def test_bounds() -> None:
    check(assert_type(shapely.bounds(PO), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.bounds(None), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.bounds([P, LS]), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.bounds((P, LS, None)), NDArray[np.float64]), np.ndarray, dtype=float)


def test_total_bounds() -> None:
    check(assert_type(shapely.total_bounds(PO), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.total_bounds(None), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.total_bounds([P, LS]), NDArray[np.float64]), np.ndarray, dtype=float)
    check(
        assert_type(shapely.total_bounds((P, LS, None)), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )


def test_length() -> None:
    check(assert_type(shapely.length(PO), np.float64), np.float64)
    check(assert_type(shapely.length(None), np.float64), np.float64)
    check(assert_type(shapely.length([P, LS]), NDArray[np.float64]), np.ndarray, dtype=float)
    check(assert_type(shapely.length((P, LS, None)), NDArray[np.float64]), np.ndarray, dtype=float)


def test_hausdorff_distance() -> None:
    check(assert_type(shapely.hausdorff_distance(PO, P), np.float64), np.float64)
    check(assert_type(shapely.hausdorff_distance(P, None), np.float64), np.float64)
    check(assert_type(shapely.hausdorff_distance(PO, P, densify=0.01), np.float64), np.float64)
    check(assert_type(shapely.hausdorff_distance(P, None, densify=0.01), np.float64), np.float64)
    check(assert_type(shapely.hausdorff_distance(None, None), np.float64), np.float64)
    check(
        assert_type(shapely.hausdorff_distance([P], None), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(
            shapely.hausdorff_distance((PO, P, None), (LS, None, None)), NDArray[np.float64]
        ),
        np.ndarray,
        dtype=float,
    )

    check(
        assert_type(shapely.hausdorff_distance(PO, P, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.hausdorff_distance(P, None, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.hausdorff_distance(None, None, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.hausdorff_distance([P], None, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(
            shapely.hausdorff_distance([PO, P, None], [LS, None, None], densify=[0.01, 1, 0.5]),
            NDArray[np.float64],
        ),
        np.ndarray,
        dtype=float,
    )


def test_frechet_distance() -> None:
    check(assert_type(shapely.frechet_distance(PO, P), np.float64), np.float64)
    check(assert_type(shapely.frechet_distance(P, None), np.float64), np.float64)
    check(assert_type(shapely.frechet_distance(PO, P, densify=0.01), np.float64), np.float64)
    check(assert_type(shapely.frechet_distance(P, None, densify=0.01), np.float64), np.float64)
    check(assert_type(shapely.frechet_distance(None, None), np.float64), np.float64)
    check(
        assert_type(shapely.frechet_distance([P], None), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.frechet_distance((PO, P, None), (LS, None, None)), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )

    check(
        assert_type(shapely.frechet_distance(PO, P, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.frechet_distance(P, None, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.frechet_distance(None, None, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.frechet_distance([P], None, densify=[0.01, 1]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(
            shapely.frechet_distance([PO, P, None], [LS, None, None], densify=[0.01, 1, 0.5]),
            NDArray[np.float64],
        ),
        np.ndarray,
        dtype=float,
    )


def test_minimum_clearance() -> None:
    check(assert_type(shapely.minimum_clearance(PO), np.float64), np.float64)
    check(assert_type(shapely.minimum_clearance(None), np.float64), np.float64)
    check(
        assert_type(shapely.minimum_clearance([P, LS]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.minimum_clearance((P, LS, None)), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )


def test_minimum_bounding_radius() -> None:
    check(assert_type(shapely.minimum_bounding_radius(PO), np.float64), np.float64)
    check(assert_type(shapely.minimum_bounding_radius(None), np.float64), np.float64)
    check(
        assert_type(shapely.minimum_bounding_radius([P, LS]), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
    check(
        assert_type(shapely.minimum_bounding_radius((P, LS, None)), NDArray[np.float64]),
        np.ndarray,
        dtype=float,
    )
