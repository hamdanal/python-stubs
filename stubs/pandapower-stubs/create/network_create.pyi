from pandapower._typing import Bool, Float
from pandapower.auxiliary import pandapowerNet

def create_empty_network(name: str = "", f_hz: Float = 50.0, sn_mva: Float = 1, add_stdtypes: Bool = True) -> pandapowerNet: ...
