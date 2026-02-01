from collections.abc import Collection, Mapping
from typing import Any

import numpy as np

from pandapower._typing import Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def create_group(
    net: pandapowerNet,
    element_types: ScalarOrVector[str],
    element_indices: Collection[Collection[Int | Any]],  # list of lists of indices or any column content
    name: str = "",
    reference_columns: ScalarOrVector[str] | None = None,
    index: Int | None = None,
    **kwargs,
) -> np.int64: ...
def create_group_from_dict(
    net: pandapowerNet,
    elements_dict: Mapping[str, Collection[Int | Any]],  # dict of lists of indices or any column content
    name: str = "",
    reference_column: ScalarOrVector[str] | None = None,
    index: Int | None = None,
    **kwargs,
) -> np.int64: ...
