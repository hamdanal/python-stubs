from _typeshed import Incomplete
from collections.abc import Callable
from typing import Literal

from pandapower.auxiliary import pandapowerNet
from pandapower.io_utils import JSONSerializableClass

class OutputWriter(JSONSerializableClass):
    output_path: str | None
    output_file_type: Literal[".xls", ".xlsx", ".csv", ".p", ".json"]
    write_time: float | None
    log_variables: list[tuple[str, str]] | None
    default_log_variables: list[tuple[str, str]]
    csv_separator: str
    output: dict[str, Incomplete]
    np_results: dict[str, Incomplete]
    output_list: list[tuple[str, str]]
    cur_realtime: float
    time_steps: Incomplete | None
    def __init__(
        self,
        net: pandapowerNet,
        time_steps: Incomplete | None = None,
        output_path: str | None = None,
        output_file_type: Literal[".xls", ".xlsx", ".csv", ".p", ".json"] = ".p",
        write_time: float | None = None,
        log_variables: list[tuple[str, str]] | None = None,
        csv_separator: str = ";",
    ) -> None: ...
    def init_log_variables(self, net: pandapowerNet) -> None: ...
    def init_all(self, net: pandapowerNet) -> None: ...
    def dump_to_file(self, net: pandapowerNet, append: bool = False, recycle_options: Incomplete | None = None) -> None: ...
    def dump(self, net: pandapowerNet, recycle_options: Incomplete | None = None) -> None: ...
    time_step: Incomplete
    def save_results(
        self,
        net: pandapowerNet,
        time_step: Incomplete,
        pf_converged: bool,
        ctrl_converged: bool,
        recycle_options: Incomplete | None = None,
    ) -> None: ...
    def save_to_parameters(self) -> None: ...
    def save_nans_to_parameters(self) -> None: ...
    def remove_log_variable(self, table: str, variable: str | None = None) -> None: ...
    def log_variable(
        self,
        table: str,
        variable: str,
        index: Incomplete | None = None,
        eval_function: Callable[[str, str, Incomplete], Incomplete] | None = None,
        eval_name: str | None = None,
    ) -> None: ...
    time_step_lookup: dict[Incomplete, int]
    def init_timesteps(self, time_steps: Incomplete) -> None: ...
    def get_batch_outputs(self, net: pandapowerNet, recycle_options: Incomplete) -> None: ...
