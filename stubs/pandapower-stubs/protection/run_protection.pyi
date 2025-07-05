from typing import Literal

import pandas as pd

from pandapower.auxiliary import pandapowerNet

def calculate_protection_times(net: pandapowerNet, scenario: Literal["pp", "sc"] = "sc") -> pd.DataFrame: ...
