from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet

log_message_sep: str

def diagnostic_report(
    net: pandapowerNet,
    diag_results: dict[str, Incomplete],
    diag_errors: dict[str, Incomplete],
    diag_params: dict[str, Incomplete],
    compact_report: bool,
    warnings_only: bool,
) -> None: ...

class DiagnosticReports:
    net: pandapowerNet
    diag_results: dict[str, Incomplete]
    diag_errors: dict[str, Incomplete]
    diag_params: dict[str, Incomplete]
    compact_report: bool
    def __init__(
        self,
        net: pandapowerNet,
        diag_results: dict[str, Incomplete],
        diag_errors: dict[str, Incomplete],
        diag_params: dict[str, Incomplete],
        compact_report: bool,
    ) -> None: ...
    def report_disconnected_elements(self) -> None: ...
    def report_different_voltage_levels_connected(self) -> None: ...
    def report_impedance_values_close_to_zero(self) -> None: ...
    def report_nominal_voltages_dont_match(self) -> None: ...
    def report_invalid_values(self) -> None: ...
    def report_overload(self) -> None: ...
    def report_wrong_switch_configuration(self) -> None: ...
    def report_no_ext_grid(self) -> None: ...
    def report_multiple_voltage_controlling_elements_per_bus(self) -> None: ...
    def report_wrong_reference_system(self) -> None: ...
    def report_deviation_from_std_type(self) -> None: ...
    def report_numba_comparison(self) -> None: ...
    def report_parallel_switches(self) -> None: ...
    def report_missing_bus_indices(self) -> None: ...