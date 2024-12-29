from collections.abc import Iterable
from typing import Any

import pandas as pd
from pandas._typing import Scalar

from pandapower.timeseries.data_source import DataSource

class DFData(DataSource):
    df: pd.DataFrame
    def __init__(self, df: pd.DataFrame, multi: bool = False) -> None: ...
    def get_time_step_value(self, time_step: Scalar, profile_name: str | Iterable[str], scale_factor: float = 1.0) -> Any: ...
    def get_time_steps_len(self) -> int: ...
