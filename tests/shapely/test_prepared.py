from __future__ import annotations

from typing import Literal, assert_type

import shapely
from shapely import Point
from shapely.prepared import PreparedGeometry

from tests import check

PG = PreparedGeometry(shapely.from_wkt("LINESTRING (1 2, 3 4, 5 6, 7 8)"))
P = Point(1, 2)


def test_prepared_geometry() -> None:
    # basics
    check(assert_type(PreparedGeometry(P).context, Point), Point)
    check(assert_type(PreparedGeometry(P).prepared, Literal[True]), bool)
    check(assert_type(PreparedGeometry(PreparedGeometry(P)).context, Point), Point)

    # comparison
    check(assert_type(PG.covers(P), bool), bool)
    check(assert_type(PG.covers(None), bool), bool)
    check(assert_type(PG.contains(P), bool), bool)
    check(assert_type(PG.contains(None), bool), bool)
    check(assert_type(PG.contains_properly(P), bool), bool)
    check(assert_type(PG.contains_properly(None), bool), bool)
    check(assert_type(PG.crosses(P), bool), bool)
    check(assert_type(PG.crosses(None), bool), bool)
    check(assert_type(PG.disjoint(P), bool), bool)
    check(assert_type(PG.disjoint(None), bool), bool)
    check(assert_type(PG.intersects(P), bool), bool)
    check(assert_type(PG.intersects(None), bool), bool)
    check(assert_type(PG.overlaps(P), bool), bool)
    check(assert_type(PG.overlaps(None), bool), bool)
    check(assert_type(PG.touches(P), bool), bool)
    check(assert_type(PG.touches(None), bool), bool)
    check(assert_type(PG.within(P), bool), bool)
    check(assert_type(PG.within(None), bool), bool)
