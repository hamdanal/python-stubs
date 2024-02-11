from typing import Literal

def geom_equals(this, that) -> bool: ...
def geom_almost_equals(this, that) -> bool: ...
def assert_geoseries_equal(
    left,
    right,
    check_dtype: bool = True,
    check_index_type: bool | Literal["equiv"] = False,
    check_series_type: bool | Literal["equiv"] = True,
    check_less_precise: bool = False,
    check_geom_type: bool = False,
    check_crs: bool = True,
    normalize: bool = False,
) -> None: ...
def assert_geodataframe_equal(
    left,
    right,
    check_dtype: bool = True,
    check_index_type: bool | Literal["equiv"] = "equiv",
    check_column_type: bool | Literal["equiv"] = "equiv",
    check_frame_type: bool = True,
    check_like: bool = False,
    check_less_precise: bool = False,
    check_geom_type: bool = False,
    check_crs: bool = True,
    normalize: bool = False,
) -> None: ...
