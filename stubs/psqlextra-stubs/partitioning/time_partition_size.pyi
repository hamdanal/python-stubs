import enum
from datetime import datetime

from dateutil.relativedelta import relativedelta

class PostgresTimePartitionUnit(enum.Enum):
    YEARS = "years"
    MONTHS = "months"
    WEEKS = "weeks"
    DAYS = "days"

class PostgresTimePartitionSize:
    unit: PostgresTimePartitionUnit
    value: int
    def __init__(
        self, years: int | None = ..., months: int | None = ..., weeks: int | None = ..., days: int | None = ...
    ) -> None: ...
    def as_delta(self) -> relativedelta: ...
    def start(self, dt: datetime) -> datetime: ...
