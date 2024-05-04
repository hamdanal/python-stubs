from _typeshed import Incomplete

import networkx as nx  # type: ignore[import-untyped]

from pandapower.auxiliary import pandapowerNet

def nxgraph_from_ppc(net: pandapowerNet, ppc) -> nx.MultiGraph[Incomplete]: ...
