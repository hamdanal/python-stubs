import logging
from typing_extensions import Self

import pandas as pd

from pandapower.converter.cim.other_classes import ReportContainer

class CimParser:
    logger: logging.Logger
    cim: dict[str, dict[str, pd.DataFrame]]
    file_names: dict[str, str]
    report_container: ReportContainer
    def __init__(self, cim: dict[str, dict[str, pd.DataFrame]] | None = None) -> None: ...
    def parse_files(
        self,
        file_list: str | list[str] | None = None,
        encoding: str = "utf-8",
        prepare_cim_net: bool = False,
        set_data_types: bool = False,
    ) -> Self: ...
    def set_cim_data_types(self) -> Self: ...
    def prepare_cim_net(self) -> Self: ...
    def get_cim_data_structure(self) -> dict[str, dict[str, pd.DataFrame]]: ...
    def get_cim_dict(self) -> dict[str, dict[str, pd.DataFrame]]: ...
    def set_cim_dict(self, cim: dict[str, dict[str, pd.DataFrame]]) -> None: ...
    def get_file_names(self) -> dict[str, str]: ...
    def get_report_container(self) -> ReportContainer: ...
