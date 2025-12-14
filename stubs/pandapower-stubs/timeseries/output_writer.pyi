from _typeshed import Incomplete
from collections.abc import Callable, Mapping, Sequence
from functools import partial
from typing import Any, Literal

import pandas as pd
from numpy.typing import NDArray

from pandapower.auxiliary import pandapowerNet
from pandapower.io_utils import JSONSerializableClass

class OutputWriter[T: Any](JSONSerializableClass):
    output_path: str | None
    output_file_type: Literal[".xls", ".xlsx", ".csv", ".p", ".json"]
    write_time: float | None
    log_variables: (
        list[tuple[str, str] | tuple[str, str, list[int], Callable[[NDArray[Incomplete]], object] | None, str | None]] | None
    )
    default_log_variables: list[tuple[str, str]]
    csv_separator: str
    output: dict[str, pd.DataFrame]
    np_results: dict[str, NDArray[Incomplete]]
    output_list: list[partial[object]]  # also list[tuple[str, str]] in self.get_batch_outputs
    cur_realtime: float
    time_steps: Sequence[T] | None
    time_step: T
    time_step_lookup: dict[T, int]
    def __init__(
        self,
        net: pandapowerNet,
        time_steps: Sequence[T] | pd.Index[T] | pd.Series[T] | NDArray[Any] | None = None,
        output_path: str | None = None,
        output_file_type: Literal[".xls", ".xlsx", ".csv", ".p", ".json"] = ".p",
        write_time: float | None = None,
        log_variables: list[tuple[str, str]] | None = None,
        csv_separator: str = ";",
    ) -> None: ...
    def init_log_variables(self, net: pandapowerNet) -> None: ...
    def init_all(self, net: pandapowerNet) -> None: ...
    def dump_to_file(
        self, net: pandapowerNet, append: bool = False, recycle_options: Mapping[str, Incomplete] | Literal[False] | None = None
    ) -> None: ...
    def dump(self, net: pandapowerNet, recycle_options: Mapping[str, Incomplete] | Literal[False] | None = None) -> None: ...
    def save_results(
        self,
        net: pandapowerNet,
        time_step: T,
        pf_converged: bool,
        ctrl_converged: bool,
        recycle_options: Mapping[str, Incomplete] | Literal[False] | None = None,
    ) -> None: ...
    def save_to_parameters(self) -> None: ...
    def save_nans_to_parameters(self) -> None: ...
    def remove_log_variable(self, table: str, variable: str | None = None) -> None: ...
    def log_variable(
        self,
        table: str,
        variable: str,
        index: Sequence[int] | None = None,
        eval_function: Callable[[NDArray[Incomplete]], object] | None = None,
        eval_name: str | None = None,
    ) -> None: ...
    def init_timesteps(self, time_steps: Sequence[T]) -> None: ...
    def get_batch_outputs(self, net: pandapowerNet, recycle_options: Mapping[str, Incomplete]) -> None: ...
