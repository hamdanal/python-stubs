from _typeshed import Incomplete

from pandapower.auxiliary import ppException

class MapboxTokenMissing(ppException): ...

def geo_data_to_latlong(net, projection) -> None: ...
def set_mapbox_token(token) -> None: ...
