from _typeshed import Incomplete
from logging import StreamHandler

class AppHandler(StreamHandler[Incomplete]):
    app: Incomplete
    PrintPlain: Incomplete
    PrintInfo: Incomplete
    PrintWarn: Incomplete
    PrintError: Incomplete
    name: str
    freeze_app_between_messages: Incomplete
    def __init__(self, app, freeze_app_between_messages: bool = False) -> None: ...
    def emit(self, record) -> None: ...

def setup_logger(app, name, level): ...
def set_PF_level(logger, app_handler, level) -> None: ...
