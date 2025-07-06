from _typeshed import Incomplete
from typing import Literal

from pandapower.auxiliary import pandapowerNet
from pandapower.control.controller.const_control import ConstControl

class PQController(ConstControl):
    element_index: Incomplete
    element: str
    bus: Incomplete
    p_mw: Incomplete
    q_mvar: Incomplete
    sn_mva: Incomplete
    element_names: Incomplete
    gen_type: Incomplete
    element_in_service: Incomplete

    sign: Literal[1, -1]
    pq_simultaneity_factor: Incomplete

    converter_sizing_pu: Incomplete

    data_source: Incomplete
    profile_scale: Incomplete
    p_profile: Incomplete
    q_profile: Incomplete
    ts_absolute: Incomplete

    max_p_error: Incomplete
    max_q_error: Incomplete

    p_curtailment: Incomplete

    def __init__(
        self,
        net: pandapowerNet,
        element_index,
        element: str = "sgen",
        max_p_error=0.0001,
        max_q_error=0.0001,
        pq_simultaneity_factor=1.0,
        converter_sizing_pu=1.0,
        data_source=None,
        profile_scale=1.0,
        in_service=True,
        ts_absolute=True,
        order=0,
        level=0,
        **kwargs,
    ) -> None: ...
    def set_p_profile(self, p_profile, profile_from_name: bool) -> None: ...
    def set_q_profile(self, q_profile, profile_from_name: bool) -> None: ...
    def read_profiles(self, time) -> None: ...
    def write_to_net(self, net: pandapowerNet) -> None: ...
    def finalize_control(self, net: pandapowerNet) -> None: ...
    def calc_curtailment(self) -> None: ...
    def limit_to_inverter_sizing(self, p_mw, q_mvar): ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
