from pandapower.auxiliary import pandapowerNet

def create_cigre_network_hv(length_km_6a_6b: float = 0.1) -> pandapowerNet: ...
def create_cigre_network_mv(with_der: bool = False) -> pandapowerNet: ...
def create_cigre_network_lv() -> pandapowerNet: ...
