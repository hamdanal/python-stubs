from collections.abc import Iterable
from typing import Any, SupportsIndex as Int

from pandas._typing import Axes, Scalar

from pandapower.auxiliary import pandapowerNet
from pandapower.control.basic_controller import Controller
from pandapower.timeseries.data_source import DataSource

class ConstControl(Controller):
    data_source: DataSource
    element_index: Axes | Scalar
    element: str
    values: Any
    profile_name: str | Iterable[str]
    scale_factor: float
    applied: bool
    def __init__(
        self,
        net: pandapowerNet,
        element: str,
        variable: str,
        element_index: Axes | Scalar,
        profile_name: str | Iterable[str] | None = None,
        data_source: DataSource | None = None,
        scale_factor: float = 1.0,
        in_service: bool = True,
        recycle: bool = True,
        order: Int = -1,
        level: Int = -1,
        drop_same_existing_ctrl: bool = False,
        matching_params: dict[str, Any] | None = None,
        initial_run: bool = False,
        **kwargs,
    ) -> None: ...
    def set_recycle(self, net: pandapowerNet) -> None: ...
    def time_step(self, net: pandapowerNet, time: Any) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool: ...
    def control_step(self, net: pandapowerNet) -> None: ...
