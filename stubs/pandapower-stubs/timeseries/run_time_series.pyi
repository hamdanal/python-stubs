from _typeshed import Incomplete, Unused
from collections.abc import Callable, Iterable, Mapping
from typing import Any, Literal, TypeVar, overload

from pandapower.auxiliary import pandapowerNet

_T = TypeVar("_T")

def init_default_outputwriter(net: pandapowerNet, time_steps: Iterable[Incomplete]) -> None: ...
def init_output_writer(net: pandapowerNet, time_steps: Incomplete) -> None: ...
def controller_not_converged(time_step: object, ts_variables: Mapping[str, Any]) -> None: ...
def pf_not_converged(time_step: object, ts_variables: Mapping[str, Any]) -> None: ...
def control_time_step(controller_order: Iterable[Incomplete], time_step: Incomplete) -> None: ...
def finalize_step(controller_order: Iterable[Incomplete], time_step: Incomplete) -> None: ...
def output_writer_routine(
    net: pandapowerNet, time_step: Incomplete, pf_converged: bool, ctrl_converged: bool, recycle_options: Mapping[str, Any]
) -> None: ...
def run_time_step(
    net: pandapowerNet,
    time_step: Incomplete,
    ts_variables: dict[str, Incomplete],
    run_control_fct: Callable[..., object] = ...,
    output_writer_fct: Callable[[pandapowerNet, Incomplete, bool, bool, dict[str, Incomplete]], object] = ...,
    **kwargs: Incomplete,
) -> None: ...
@overload
def get_recycle_settings(net: pandapowerNet, recycle: Literal[False], **kwargs: Unused) -> Literal[False]: ...
@overload
def get_recycle_settings(net: pandapowerNet, **kwargs: Incomplete) -> dict[str, Any] | Literal[False]: ...
@overload
def init_time_steps(net: pandapowerNet, time_steps: Iterable[_T], **kwargs: Unused) -> Iterable[_T]: ...  # type: ignore[overload-overlap]
@overload
def init_time_steps(net: pandapowerNet, time_steps: None, start_step: int, stop_step: int, **kwargs: Unused) -> range: ...
@overload
def init_time_steps(net: pandapowerNet, time_steps: object, **kwargs: Unused) -> range: ...
def init_time_series(
    net: pandapowerNet,
    time_steps: Iterable[Incomplete] | tuple[int, int] | None,
    continue_on_divergence: bool = False,
    verbose: bool = True,
    **kwargs: Incomplete,
) -> dict[str, Any]: ...
def cleanup(net: pandapowerNet, ts_variables: dict[str, Incomplete]) -> None: ...
def print_progress(i: int, time_step: Incomplete, time_steps: Incomplete, verbose: bool, **kwargs: Incomplete) -> None: ...
def run_loop(
    net: pandapowerNet,
    ts_variables: dict[str, Incomplete],
    run_control_fct: Callable[..., object] = ...,
    output_writer_fct: Callable[[pandapowerNet, Incomplete, bool, bool, dict[str, Incomplete]], object] = ...,
    **kwargs: Incomplete,
) -> None: ...
def run_timeseries(
    net: pandapowerNet,
    time_steps: Incomplete | None = None,
    continue_on_divergence: bool = False,
    verbose: bool = True,
    **kwargs: Incomplete,
) -> None: ...
