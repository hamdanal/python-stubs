from collections.abc import Iterable
from typing import Any

from pandas._typing import Scalar

from pandapower.io_utils import JSONSerializableClass

class DataSource(JSONSerializableClass):
    def get_time_step_value(self, time_step: Scalar, profile_name: str | Iterable[str], scale_factor: float = 1.0) -> Any: ...
