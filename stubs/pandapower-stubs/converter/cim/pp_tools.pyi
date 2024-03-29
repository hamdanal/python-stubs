import pandas as pd

from pandapower.auxiliary import pandapowerNet

def set_pp_col_types(net: pandapowerNet, ignore_errors: bool = False) -> pandapowerNet: ...
def add_slack_and_lines_to_boundary_nodes(net: pandapowerNet, voltage_levels: list[int] | None = None) -> None: ...
def get_not_existing_column(df: pd.DataFrame) -> str: ...
