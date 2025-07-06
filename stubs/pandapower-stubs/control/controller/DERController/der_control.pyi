from pandapower.auxiliary import pandapowerNet
from pandapower.control.controller.pq_control import PQController

class DERController(PQController):
    def __init__(
        self,
        net: pandapowerNet,
        element_index,
        element: str = "sgen",
        q_model=None,
        pqv_area=None,
        saturate_sn_mva=...,
        q_prio=True,
        damping_coef=2,
        max_p_error=1e-6,
        max_q_error=1e-6,
        pq_simultaneity_factor=1.0,
        f_sizing=1.0,
        data_source=None,
        p_profile=None,
        profile_from_name=False,
        profile_scale=1.0,
        in_service=True,
        ts_absolute=True,
        order=0,
        level=0,
        drop_same_existing_ctrl=False,
        matching_params=None,
        **kwargs,
    ) -> None: ...
    def time_step(self, net: pandapowerNet, time) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool: ...
    def control_step(self, net: pandapowerNet) -> None: ...
