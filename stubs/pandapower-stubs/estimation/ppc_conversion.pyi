from collections import UserDict
from collections.abc import Collection
from typing import (
    Any,
    Any as csr_matrix,  # scipy.sparse.csr_matrix
    Literal,
)

import numpy as np

from pandapower._typing import Array1D, Array2D
from pandapower.auxiliary import pandapowerNet

ZERO_INJECTION_STD_DEV: float
BR_SIDE: dict[str, dict[str, str]]
BR_MEAS_PPCI_IX: dict[tuple[str, str], dict[str, int]]
BUS_MEAS_PPCI_IX: dict[str, dict[str, int]]

def pp2eppci(
    net: pandapowerNet,
    v_start: Collection[float] | str | None = None,
    delta_start: Collection[float] | str | None = None,
    calculate_voltage_angles: bool = True,
    zero_injection: str = "aux_bus",
    algorithm: str = "wls",
    ppc: dict[str, Any] | None = None,
    eppci: ExtendedPPCI | None = None,
) -> tuple[pandapowerNet, dict[str, Any] | None, ExtendedPPCI]: ...

class ExtendedPPCI(UserDict[str, Any]):
    data: dict[str, Any]
    algorithm: Literal["wls", "wls_with_zero_constraint", "opt", "irwls", "lp", "af-wls"]
    z: Array2D[np.float64] | None
    r_cov: Array2D[np.float64] | None
    pp_meas_indices: Array2D[np.int64] | None
    non_nan_meas_mask: dict[str, Array1D[np.int64]] | None
    non_nan_meas_selector: Array1D[np.int64] | None
    idx_non_imeas: Array1D[np.int64] | None
    any_i_meas: bool
    any_degree_meas: bool
    non_slack_buses: Array1D[np.int64]
    non_slack_bus_mask: Array1D[np.bool]
    num_non_slack_bus: np.int64
    delta_v_bus_mask: Array1D[np.bool]
    delta_v_bus_selector: Array1D[np.int64]
    v_init: Array1D[np.float64]
    delta_init: Array1D[np.float64]
    E_init: Array1D[np.float64]
    v: Array1D[np.float64]
    delta: Array1D[np.float64]
    E: Array1D[np.float64]
    def __init__(
        self, ppci: dict[str, Any], algorithm: Literal["wls", "wls_with_zero_constraint", "opt", "irwls", "lp", "af-wls"]
    ) -> None: ...
    def update_meas(self) -> None: ...
    @property
    def V(self) -> Array1D[np.complex128]: ...
    def reset(self) -> None: ...
    def update_E(self, E: Array1D[np.float64]) -> None: ...
    def E2V(self, E: Array1D[np.float64]) -> Array1D[np.complex128]: ...
    def get_Y(self) -> tuple[csr_matrix, csr_matrix, csr_matrix]: ...
