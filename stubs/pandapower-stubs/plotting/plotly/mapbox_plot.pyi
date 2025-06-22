from typing_extensions import deprecated

from pandapower.auxiliary import pandapowerNet

@deprecated("Use pandapower.geo.convert_crs instead")
def geo_data_to_latlong(net: pandapowerNet, projection: str) -> None: ...
def set_mapbox_token(token: str) -> None: ...
