from pandapower.auxiliary import pandapowerNet, ppException

class MapboxTokenMissing(ppException): ...

def geo_data_to_latlong(net: pandapowerNet, projection: str) -> None: ...
def set_mapbox_token(token: str) -> None: ...
