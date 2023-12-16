from _typeshed import Incomplete

from numpy.typing import ArrayLike, NDArray

from pandapower.auxiliary import pandapowerNet

def get_batch_bus_results(
    net: pandapowerNet, vm: ArrayLike, va: ArrayLike
) -> tuple[NDArray[Incomplete], NDArray[Incomplete]]: ...
def get_batch_line_results(
    net: pandapowerNet, i_abs: tuple[ArrayLike, ArrayLike]
) -> tuple[NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete]]: ...
def get_batch_trafo_results(
    net: pandapowerNet, i_abs: tuple[ArrayLike, ArrayLike], s_abs: tuple[ArrayLike, ArrayLike]
) -> tuple[NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete]] | None: ...
def get_batch_trafo3w_results(
    net: pandapowerNet, i_abs: tuple[ArrayLike, ArrayLike], s_abs: tuple[ArrayLike, ArrayLike]
) -> tuple[NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete], NDArray[Incomplete]] | None: ...
def v_to_i_s(
    net: pandapowerNet, vm: ArrayLike, va: ArrayLike
) -> tuple[
    tuple[NDArray[Incomplete], NDArray[Incomplete]],
    tuple[NDArray[Incomplete], NDArray[Incomplete]],
    tuple[NDArray[Incomplete], NDArray[Incomplete]],
]: ...
def polar_to_rad(vm: ArrayLike, va: ArrayLike) -> NDArray[Incomplete]: ...
