from _typeshed import Incomplete

from pandapower.estimation.algorithm.base import BaseAlgorithm
from pandapower.estimation.ppc_conversion import ExtendedPPCI

DEFAULT_OPT_METHOD: str

class OptAlgorithm(BaseAlgorithm):
    successful: Incomplete
    def estimate(self, eppci: ExtendedPPCI, estimator: str = ..., verbose: bool = ..., **kwargs): ...
