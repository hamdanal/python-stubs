from typing import Any, Literal, overload

from pandapower.auxiliary import ADict
from pandapower.diagnostic.diagnostic_helpers import DiagnosticFunction

log_format_len: int
log_message_sep: str

class Diagnostic:
    kwargs: dict[str, Any]
    net: ADict[Any] | None
    diag_results: dict[str, Any]
    diag_errors: dict[str, Any]
    def __init__(self, add_default_functions: bool = True) -> None: ...
    def register_function(
        self, diagnostic_function: DiagnosticFunction[Any, Any], argument_names: list[str] | None, name: str | None
    ) -> None: ...
    @overload
    def diagnose_network(
        self,
        net: ADict[Any],
        report_style: Literal["detailed", "compact"] | None = "detailed",
        warnings_only: bool = False,
        return_result_dict: Literal[True] = True,
        **kwargs,
    ) -> dict[str, Any]: ...
    @overload
    def diagnose_network(
        self,
        net: ADict[Any],
        *,
        report_style: Literal["detailed", "compact"] | None = "detailed",
        warnings_only: bool = False,
        return_result_dict: Literal[False],
        **kwargs,
    ) -> None: ...
    def compact_report(self, warnings_only: bool = False) -> None: ...
    def detailed_report(self, warnings_only: bool = False) -> None: ...
    def report(self, compact_report: bool = True, warnings_only: bool = False) -> None: ...
