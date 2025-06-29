from pandapower.auxiliary import pandapowerNet
from pandapower.estimation.ppc_conversion import ExtendedPPCI

def eppci2pp(net: pandapowerNet, ppc, eppci: ExtendedPPCI) -> pandapowerNet: ...
