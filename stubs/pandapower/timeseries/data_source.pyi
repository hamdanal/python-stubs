from _typeshed import Incomplete

from pandapower.io_utils import JSONSerializableClass

class DataSource(JSONSerializableClass):
    def get_time_step_value(self, time_step: Incomplete, profile_name: str, scale_factor: float = 1.0) -> Incomplete: ...
