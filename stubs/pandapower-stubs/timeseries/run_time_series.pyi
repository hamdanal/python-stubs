from _typeshed import Incomplete, SupportsGetItem, Unused
from collections.abc import Callable, Iterable, Mapping
from typing import Any, Literal, overload
from typing_extensions import deprecated

from pandapower.auxiliary import pandapowerNet

def init_default_outputwriter(net: pandapowerNet, time_steps: Iterable[Incomplete]) -> None: ...
def init_output_writer(net: pandapowerNet, time_steps) -> None: ...
def controller_not_converged(time_step: object, ts_variables: SupportsGetItem[str, Any]) -> None: ...
def pf_not_converged(time_step: object, ts_variables: SupportsGetItem[str, Any]) -> None: ...
def control_time_step(controller_order: Iterable[Iterable[tuple[Incomplete, pandapowerNet]]], time_step) -> None: ...
def finalize_step(controller_order: Iterable[Iterable[tuple[Incomplete, pandapowerNet]]], time_step) -> None: ...
def output_writer_routine(
    net: pandapowerNet, time_step, pf_converged: bool, ctrl_converged: bool, recycle_options: Mapping[str, Any]
) -> None: ...
def run_time_step(
    net: pandapowerNet,
    time_step,
    ts_variables: dict[str, Incomplete],
    run_control_fct: Callable[..., object] = ...,
    output_writer_fct: Callable[[pandapowerNet, Incomplete, bool, bool, dict[str, Incomplete]], object] = ...,
    **kwargs,
) -> None: ...
@overload
def get_recycle_settings(net: pandapowerNet, *, recycle: Literal[False], **kwargs: Unused) -> Literal[False]: ...
@overload
def get_recycle_settings(
    net: pandapowerNet, *, recycle: Incomplete | None = None, **kwargs
) -> dict[str, Any] | Literal[False]: ...
@overload
def init_time_steps[T](net: pandapowerNet, time_steps: Iterable[T], **kwargs: Unused) -> Iterable[T]: ...  # type: ignore[overload-overlap]
@overload
@deprecated("start_step and stop_step are deprcated")
def init_time_steps(net: pandapowerNet, time_steps: None, *, start_step: int, stop_step: int, **kwargs: Unused) -> range: ...
@overload
def init_time_steps(net: pandapowerNet, time_steps: object, **kwargs: Unused) -> range: ...
def init_time_series(
    net: pandapowerNet,
    time_steps: Iterable[Incomplete] | tuple[int, int] | None,
    continue_on_divergence: bool = False,
    verbose: bool = True,
    **kwargs,
) -> dict[str, Any]: ...
def cleanup(net: pandapowerNet, ts_variables: dict[str, Incomplete]) -> None: ...
def print_progress(i: int, time_step, time_steps, verbose: bool, **kwargs) -> None: ...
def run_loop(
    net: pandapowerNet,
    ts_variables: dict[str, Incomplete],
    run_control_fct: Callable[..., object] = ...,
    output_writer_fct: Callable[[pandapowerNet, Incomplete, bool, bool, dict[str, Incomplete]], object] = ...,
    **kwargs,
) -> None: ...
def run_timeseries(
    net: pandapowerNet,
    time_steps: Incomplete | None = None,
    continue_on_divergence: bool = False,
    verbose: bool = True,
    check_controllers: bool = True,
    **kwargs,
) -> None: ...
