import logging
from collections.abc import Collection
from typing import Any, Literal, overload

from pandapower.auxiliary import pandapowerNet
from pandapower.estimation.algorithm.base import BaseAlgorithm

ALGORITHM_MAPPING: dict[str, type[BaseAlgorithm]]
ALLOWED_OPT_VAR: set[str]

@overload
def estimate(
    net: pandapowerNet,
    algorithm: Literal["wls", "af-wls"] = "wls",
    init: Literal["flat", "results", "slack"] = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 50,
    zero_injection: Collection[int] | str = "aux_bus",
    fuse_buses_with_bb_switch: Collection[int] | Literal["all"] = "all",
    debug_mode: bool = False,
    **opt_vars,
) -> dict[str, Any]: ...
@overload
def estimate(
    net: pandapowerNet,
    algorithm: Literal["wls_with_zero_constraint", "opt", "irwls", "lp"],
    init: Literal["flat", "results", "slack"] = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 50,
    zero_injection: Collection[int] | str = "aux_bus",
    fuse_buses_with_bb_switch: Collection[int] | Literal["all"] = "all",
    debug_mode: bool = False,
    **opt_vars,
) -> bool: ...
def remove_bad_data(
    net: pandapowerNet,
    init: Literal["flat", "results", "slack"] = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 10,
    calculate_voltage_angles: bool = True,
    rn_max_threshold: float = 3.0,
) -> bool: ...
def chi2_analysis(
    net,
    init: str = "flat",
    tolerance: float = 1e-06,
    maximum_iterations: int = 10,
    calculate_voltage_angles: bool = True,
    chi2_prob_false: float = 0.05,
) -> bool | None: ...

class StateEstimation:
    logger: logging.Logger
    net: pandapowerNet
    solver: BaseAlgorithm
    ppc: dict[str, Any] | None
    eppci: dict[str, Any] | None
    recycle: bool
    algorithm: Literal["wls", "wls_with_zero_constraint", "opt", "irwls", "lp", "af-wls"]
    delta: None  # not currently used
    bad_data_present: bool | None
    def __init__(
        self,
        net: pandapowerNet,
        tolerance: float = 1e-06,
        maximum_iterations: int = 50,
        algorithm: Literal["wls", "wls_with_zero_constraint", "opt", "irwls", "lp", "af-wls"] = "wls",
        logger: logging.Logger | None = None,
        recycle: bool = False,
    ) -> None: ...
    @overload
    def estimate(
        self,
        v_start: Collection[float] | str = "flat",
        delta_start: Collection[float] | str = "flat",
        zero_injection: Collection[int] | str | None = None,
        fuse_buses_with_bb_switch: Collection[int] | Literal["all"] = "all",
        algorithm: Literal["wls", "af-wls"] = "wls",
        debug_mode: bool = False,
        **opt_vars,
    ) -> dict[str, Any]: ...
    @overload  # algorithm positional
    def estimate(
        self,
        v_start: Collection[float] | str,
        delta_start: Collection[float] | str,
        zero_injection: Collection[int] | str | None,
        fuse_buses_with_bb_switch: Collection[int] | Literal["all"],
        algorithm: Literal["wls_with_zero_constraint", "opt", "irwls", "lp"],
        debug_mode: bool = False,
        **opt_vars,
    ) -> bool: ...
    @overload  # algorithm keyword
    def estimate(
        self,
        v_start: Collection[float] | str = "flat",
        delta_start: Collection[float] | str = "flat",
        zero_injection: Collection[int] | str | None = None,
        fuse_buses_with_bb_switch: Collection[int] | Literal["all"] = "all",
        *,
        algorithm: Literal["wls_with_zero_constraint", "opt", "irwls", "lp"],
        debug_mode: bool = False,
        **opt_vars,
    ) -> bool: ...
    def perform_chi2_test(
        self,
        v_in_out: Collection[float] | str | None = None,
        delta_in_out: Collection[float] | str | None = None,
        calculate_voltage_angles: bool = True,
        chi2_prob_false: float = 0.05,
    ) -> bool | None: ...
    def perform_rn_max_test(
        self,
        v_in_out: Collection[float] | str | None = None,
        delta_in_out: Collection[float] | str | None = None,
        calculate_voltage_angles: bool = True,
        rn_max_threshold: float = 3.0,
    ) -> bool: ...
