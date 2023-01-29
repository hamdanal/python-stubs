import enum
from datetime import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta

class PostgresTimePartitionUnit(enum.Enum):
    YEARS: str
    MONTHS: str
    WEEKS: str
    DAYS: str

class PostgresTimePartitionSize:
    unit: PostgresTimePartitionUnit
    value: int
    def __init__(
        self, years: int | None = ..., months: int | None = ..., weeks: int | None = ..., days: int | None = ...
    ) -> None: ...
    def as_delta(self) -> relativedelta: ...
    def start(self, dt: datetime) -> datetime: ...
