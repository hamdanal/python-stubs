import enum
from typing import Any

from pandapower.converter.cim import interfaces

class ReportCode(enum.Enum):
    INFO: int
    INFO_PARSING: int
    INFO_CONVERTING: int
    INFO_REPAIRING: int
    WARNING: int
    WARNING_PARSING: int
    WARNING_CONVERTING: int
    WARNING_REPAIRING: int
    ERROR: int
    ERROR_PARSING: int
    ERROR_CONVERTING: int
    ERROR_REPAIRING: int
    EXCEPTION: int
    EXCEPTION_PARSING: int
    EXCEPTION_CONVERTING: int
    EXCEPTION_REPAIRING: int

    @classmethod
    def from_value(cls, value: int) -> ReportCode: ...

class LogLevel(enum.Enum):
    INFO: str
    WARNING: str
    ERROR: str
    EXCEPTION: str

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
