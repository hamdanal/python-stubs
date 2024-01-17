from __future__ import annotations

from collections.abc import Iterator

import numpy as np
import pytest
import shapely
from shapely import LineString, Point, Polygon
from shapely.geometry.base import BaseGeometry
from typing_extensions import assert_type

from tests import check

BG = shapely.from_wkt("LINESTRING (1 2, 3 4, 5 6, 7 8)")
P = Point(1, 1)
LS = LineString([(1, 3), (1, 1), (4, 1)])
PO = Polygon([(1, 1), (2, 3), (3, 1)])


def test_affine_transform() -> None:
    # fmt: off
    matrix = (+1.5, 0.0, 0.0,
              +0.0, 1.0, 0.0,
              +0.0, 0.0, 1.0,
              -0.5, 2.0, 0.0)
    # fmt: on
    check(assert_type(shapely.affinity.affine_transform(P, matrix), Point), Point)
    check(assert_type(shapely.affinity.affine_transform(PO, matrix), Polygon), Polygon)

    class MatrixCollection:
        def __init__(self, m: tuple[float, ...]) -> None:
            self.m = m

        def __len__(self) -> int:
            return len(self.m)

        def __contains__(self, x: object) -> bool:
            return x in self.m

        def __iter__(self) -> Iterator[float]:
            return iter(self.m)

    check(assert_type(shapely.affinity.affine_transform(P, MatrixCollection(matrix)), Point), Point)
    check(assert_type(shapely.affinity.affine_transform(P, np.array(matrix)), Point), Point)


def test_rotate() -> None:
    check(assert_type(shapely.affinity.rotate(BG, 90), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.affinity.rotate(P, 90), Point), Point)
    check(assert_type(shapely.affinity.rotate(LS, 90), LineString), LineString)
    check(assert_type(shapely.affinity.rotate(LS, 90, use_radians=True), LineString), LineString)
    check(assert_type(shapely.affinity.rotate(LS, 90, origin="centroid"), LineString), LineString)
    check(assert_type(shapely.affinity.rotate(LS, 90, origin="center"), LineString), LineString)
    check(assert_type(shapely.affinity.rotate(LS, 90, origin=LS.centroid), LineString), LineString)
    x, y = LS.centroid.coords[0]
    check(assert_type(shapely.affinity.rotate(LS, 90, origin=(x, y)), LineString), LineString)
    check(assert_type(shapely.affinity.rotate(LS, 90, origin=(x, y, 0)), LineString), LineString)

    with pytest.raises(Exception):
        shapely.affinity.rotate(LS, 90, origin="centred")  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_scale() -> None:
    check(assert_type(shapely.affinity.scale(P), Point), Point)
    check(assert_type(shapely.affinity.scale(PO), Polygon), Polygon)
    check(assert_type(shapely.affinity.scale(PO, xfact=1.5, yfact=-1, zfact=1.0), Polygon), Polygon)
    check(
        assert_type(shapely.affinity.scale(PO, xfact=1.5, yfact=-1, origin="centroid"), Polygon),
        Polygon,
    )
    check(
        assert_type(shapely.affinity.scale(PO, xfact=1.5, yfact=-1, origin="center"), Polygon),
        Polygon,
    )
    check(assert_type(shapely.affinity.scale(PO, xfact=1.5, yfact=-1, origin=P), Polygon), Polygon)
    check(assert_type(shapely.affinity.scale(LS, 90, origin=(1.0, 1)), LineString), LineString)
    check(assert_type(shapely.affinity.scale(LS, 90, origin=(1, 1.0, 0.0)), LineString), LineString)

    with pytest.raises(Exception):
        shapely.affinity.scale(PO, origin="centred")  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_skew() -> None:
    check(assert_type(shapely.affinity.skew(BG, 20), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.affinity.skew(P, 20.0), Point), Point)
    check(assert_type(shapely.affinity.skew(PO, 20), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, ys=30.0), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, use_radians=True), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, origin="centroid"), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, origin="center"), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, origin=PO.centroid), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, origin=(1.0, 1.0)), Polygon), Polygon)
    check(assert_type(shapely.affinity.skew(PO, 20, origin=(1.0, 2.0, 0)), Polygon), Polygon)

    with pytest.raises(Exception):
        shapely.affinity.skew(PO, 20, origin="centred")  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]


def test_translate() -> None:
    check(assert_type(shapely.affinity.translate(BG, 20), BaseGeometry), BaseGeometry)
    check(assert_type(shapely.affinity.translate(P, 20.0), Point), Point)
    check(assert_type(shapely.affinity.translate(PO, 20), Polygon), Polygon)
    check(assert_type(shapely.affinity.translate(PO, 20, 30.0), Polygon), Polygon)
    check(assert_type(shapely.affinity.translate(PO, 20, 30.0, zoff=1.0), Polygon), Polygon)
