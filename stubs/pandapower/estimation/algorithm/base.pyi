from _typeshed import Incomplete

from pandapower.estimation.ppc_conversion import ExtendedPPCI

class BaseAlgorithm:
    tolerance: Incomplete
    max_iterations: Incomplete

    successful: bool
    iterations: Incomplete
    eppci: Incomplete
    pp_meas_indices: Incomplete
    def __init__(self, tolerance, maximum_iterations, logger=...) -> None: ...
    def check_observability(self, eppci: ExtendedPPCI, z): ...
    def check_result(self, current_error, cur_it) -> None: ...
    def initialize(self, eppci: ExtendedPPCI): ...
    def estimate(self, eppci: ExtendedPPCI, **kwargs): ...

class WLSAlgorithm(BaseAlgorithm):
    R_inv: Incomplete
    Gm: Incomplete
    r: Incomplete
    H: Incomplete
    hx: Incomplete
    def __init__(self, tolerance, maximum_iterations, logger=...) -> None: ...
    def estimate(self, eppci: ExtendedPPCI, **kwargs): ...

class WLSZeroInjectionConstraintsAlgorithm(BaseAlgorithm):
    def estimate(self, eppci: ExtendedPPCI, **kwargs): ...

class IRWLSAlgorithm(BaseAlgorithm):
    def estimate(self, eppci: ExtendedPPCI, estimator: str = ..., **kwargs): ...
