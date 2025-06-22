import datetime as dt
import enum

from dateutil.relativedelta import relativedelta

__all__ = ["PostgresTimePartitionUnit", "PostgresTimePartitionSize"]

class PostgresTimePartitionUnit(enum.Enum):
    YEARS = "years"
    MONTHS = "months"
    WEEKS = "weeks"
    DAYS = "days"

class PostgresTimePartitionSize:
    unit: PostgresTimePartitionUnit
    value: int
    def __init__(
        self, years: int | None = None, months: int | None = None, weeks: int | None = None, days: int | None = None
    ) -> None: ...
    def as_delta(self) -> relativedelta: ...
    def start(self, dt: dt.datetime) -> dt.datetime: ...
