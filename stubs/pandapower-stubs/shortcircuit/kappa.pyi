import networkx as nx

from pandapower.auxiliary import pandapowerNet

def nxgraph_from_ppc(net: pandapowerNet, ppc) -> nx.MultiGraph: ...
