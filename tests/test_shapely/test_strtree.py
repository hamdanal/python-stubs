from __future__ import annotations

import pytest
import shapely.ops
from shapely import Point

P = Point(1, 2)


def test_strtree() -> None:
    with pytest.raises(Exception):
        shapely.STRtree(P)  # type: ignore[arg-type] # pyright: ignore[reportGeneralTypeIssues]
    shapely.STRtree([P])


def test_strtree_query() -> None:
    ...  # TODO query not fully typed yet


def test_strtree_nearest() -> None:
    ...  # TODO nearest not fully typed yet


def test_strtree_query_nearest() -> None:
    ...  # TODO query_nearest not fully typed yet
