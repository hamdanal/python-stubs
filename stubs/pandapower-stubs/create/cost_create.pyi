from collections.abc import Collection

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet
from pandapower.pp_types import CostElementType, PWLPowerType

def create_pwl_cost(
    net: pandapowerNet,
    element: Int,
    et: CostElementType,
    points: Collection[Collection[Float]],
    power_type: PWLPowerType = "p",
    index: Int | None = None,
    check: Bool = True,
    **kwargs,
) -> np.int64: ...
def create_pwl_costs(
    net: pandapowerNet,
    elements: Collection[Int],
    et: ScalarOrVector[CostElementType],
    points: ScalarOrVector[Collection[Collection[Float]]],
    power_type: ScalarOrVector[PWLPowerType] = "p",
    index: Collection[Int] | None = None,
    check: ScalarOrVector[Bool] = True,
    **kwargs,
) -> Array1D[np.int64]: ...
def create_poly_cost(
    net: pandapowerNet,
    element: Int,
    et: CostElementType,
    cp1_eur_per_mw: Float,
    cp0_eur: Float = 0,
    cq1_eur_per_mvar: Float = 0,
    cq0_eur: Float = 0,
    cp2_eur_per_mw2: Float = 0,
    cq2_eur_per_mvar2: Float = 0,
    index: Int | None = None,
    check: Bool = True,
    **kwargs,
) -> np.int64: ...
def create_poly_costs(
    net: pandapowerNet,
    elements: Collection[Int],
    et: ScalarOrVector[CostElementType],
    cp1_eur_per_mw: ScalarOrVector[Float],
    cp0_eur: ScalarOrVector[Float] = 0,
    cq1_eur_per_mvar: ScalarOrVector[Float] = 0,
    cq0_eur: ScalarOrVector[Float] = 0,
    cp2_eur_per_mw2: ScalarOrVector[Float] = 0,
    cq2_eur_per_mvar2: ScalarOrVector[Float] = 0,
    index: Collection[Int] | None = None,
    check: ScalarOrVector[Bool] = True,
    **kwargs,
) -> Array1D[np.int64]: ...
