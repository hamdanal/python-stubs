from matplotlib.backend_bases import GraphicsContextBase
from pandapower.plotting.collections import *
from pandapower.plotting.colormaps import *
from pandapower.plotting.generic_geodata import *
from pandapower.plotting.geo import *
from pandapower.plotting.plotly import *
from pandapower.plotting.plotting_toolbox import set_line_geodata_from_bus_geodata as set_line_geodata_from_bus_geodata
from pandapower.plotting.powerflow_results import *
from pandapower.plotting.simple_plot import *
from pandapower.plotting.to_html import to_html as to_html

class GC(GraphicsContextBase):
    def __init__(self) -> None: ...

def custom_new_gc(self): ...
