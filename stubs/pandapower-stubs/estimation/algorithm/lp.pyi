from pandapower.estimation.algorithm.base import BaseAlgorithm
from pandapower.estimation.ppc_conversion import ExtendedPPCI

class LPAlgorithm(BaseAlgorithm):
    def estimate(self, eppci: ExtendedPPCI, with_ortools: bool = True, **kwargs): ...
