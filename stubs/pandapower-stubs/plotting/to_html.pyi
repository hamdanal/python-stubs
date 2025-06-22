from pandapower.auxiliary import pandapowerNet

def to_html(
    net: pandapowerNet,
    filename: str,
    respect_switches: bool = True,
    include_lines: bool = True,
    include_trafos: bool = True,
    show_tables: bool = True,
) -> None: ...

class Raw:
    html: str
    def __init__(self, html: str) -> None: ...

class Tag:
    name: str
    def __init__(self, name: str) -> None: ...
    def __call__(self, *args: object, **kwargs: str) -> Raw: ...
