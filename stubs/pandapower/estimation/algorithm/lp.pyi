from pandapower.estimation.algorithm.base import BaseAlgorithm
from pandapower.estimation.ppc_conversion import ExtendedPPCI

ortools_available: bool

class LPAlgorithm(BaseAlgorithm):
    def estimate(self, eppci: ExtendedPPCI, with_ortools: bool = ..., **kwargs): ...
