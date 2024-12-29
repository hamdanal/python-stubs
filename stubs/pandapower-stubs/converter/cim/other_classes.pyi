import enum
from typing import Any

from pandapower.converter.cim import interfaces

class ReportCode(enum.Enum):
    INFO = 20
    INFO_PARSING = 21
    INFO_CONVERTING = 22
    INFO_REPAIRING = 23
    WARNING = 30
    WARNING_PARSING = 31
    WARNING_CONVERTING = 32
    WARNING_REPAIRING = 33
    ERROR = 40
    ERROR_PARSING = 41
    ERROR_CONVERTING = 42
    ERROR_REPAIRING = 43
    EXCEPTION = 50
    EXCEPTION_PARSING = 51
    EXCEPTION_CONVERTING = 52
    EXCEPTION_REPAIRING = 53

    @classmethod
    def from_value(cls, value: int) -> ReportCode: ...

class LogLevel(enum.Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    EXCEPTION = "EXCEPTION"

    @classmethod
    def from_value(cls, value: str) -> LogLevel: ...

class Report:
    timestamp: str
    message: str
    code: ReportCode
    level: LogLevel
    def __init__(self, message: str, code: ReportCode, level: LogLevel) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class ReportContainer(interfaces.ReportContainer):
    logs: list[Report]
    def __init__(self, logs: list[Report] | None = None) -> None: ...
    def add_log(self, log: Report) -> None: ...
    def get_logs(self) -> list[Report]: ...
    def extend_log(self, report_container: ReportContainer) -> None: ...
    def serialize(self, path_to_disk: str) -> None: ...
