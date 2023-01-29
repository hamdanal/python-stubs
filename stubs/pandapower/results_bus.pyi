from _typeshed import Incomplete
from typing import Any
from typing_extensions import TypeAlias

from numpy import floating, integer
from numpy.typing import ArrayLike, NDArray
from pandapower.auxiliary import pandapowerNet

_PType: TypeAlias = NDArray[floating[Any]]
_QType: TypeAlias = NDArray[floating[Any]]
_BType: TypeAlias = NDArray[integer[Any]]

def write_voltage_dependend_load_results(
    net: pandapowerNet, p: ArrayLike, q: ArrayLike, b: ArrayLike
) -> tuple[NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete]] | None: ...
def write_pq_results_to_element(
    net: pandapowerNet, ppc: Incomplete, element: str, suffix: str | None = None
) -> pandapowerNet: ...
def write_pq_results_to_element_3ph(net: pandapowerNet, element: str) -> pandapowerNet: ...
def get_p_q_b(net: pandapowerNet, element: str, suffix: str | None = None) -> tuple[_PType, _QType, _BType]: ...
def get_p_q_b_3ph(net: pandapowerNet, element: str) -> tuple[_PType, _PType, _PType, _QType, _QType, _QType, _BType]: ...
