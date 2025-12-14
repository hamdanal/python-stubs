from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any

import numpy as np
import pandas as pd
from numpy.typing import NDArray

from pandapower.auxiliary import pandapowerNet

def dataframes_equal(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    ignore_index_order: bool = True,
    assume_geojson_strings: bool = True,
    **kwargs: Incomplete,
) -> bool: ...
def compare_arrays(x: NDArray[Any], y: NDArray[Any]) -> NDArray[np.bool]: ...
def nets_equal(
    net1: pandapowerNet,
    net2: pandapowerNet,
    check_only_results: bool = False,
    check_without_results: bool = False,
    exclude_elms: Iterable[str] | None = None,
    name_selection: Iterable[str] | None = None,
    assume_geojson_strings: bool = True,
    **kwargs,
) -> bool: ...
def nets_equal_keys(
    net1: pandapowerNet,
    net2: pandapowerNet,
    check_only_results: bool,
    check_without_results: bool,
    exclude_elms: Iterable[str] | None,
    name_selection: Iterable[str] | None,
    assume_geojson_strings: bool,
    **kwargs,
) -> tuple[list[str], list[str]] | tuple[set[str], set[str]]: ...
