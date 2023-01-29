from _typeshed import Incomplete

from matplotlib.textpath import TextPath

MATPLOTLIB_INSTALLED: bool

class CustomTextPath(TextPath):
    s: Incomplete
    usetex: Incomplete
    prop: Incomplete
    def __init__(
        self,
        xy,
        s,
        size: Incomplete | None = ...,
        prop: Incomplete | None = ...,
        _interpolation_steps: int = ...,
        usetex: bool = ...,
    ) -> None: ...
    def __deepcopy__(self, memo: Incomplete | None = ...): ...

def create_annotation_collection(texts, coords, size, prop: Incomplete | None = ..., **kwargs): ...
def add_cmap_to_collection(collection, cmap, norm, z, cbar_title, plot_colormap: bool = ..., clim: Incomplete | None = ...): ...
def create_bus_collection(
    net,
    buses: Incomplete | None = ...,
    size: int = ...,
    patch_type: str = ...,
    color: Incomplete | None = ...,
    z: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    infofunc: Incomplete | None = ...,
    picker: bool = ...,
    bus_geodata: Incomplete | None = ...,
    cbar_title: str = ...,
    **kwargs,
): ...
def create_line_collection(
    net,
    lines: Incomplete | None = ...,
    line_geodata: Incomplete | None = ...,
    bus_geodata: Incomplete | None = ...,
    use_bus_geodata: bool = ...,
    infofunc: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    picker: bool = ...,
    z: Incomplete | None = ...,
    cbar_title: str = ...,
    clim: Incomplete | None = ...,
    plot_colormap: bool = ...,
    **kwargs,
): ...
def create_dcline_collection(
    net,
    dclines: Incomplete | None = ...,
    bus_geodata: Incomplete | None = ...,
    infofunc: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    picker: bool = ...,
    z: Incomplete | None = ...,
    cbar_title: str = ...,
    clim: Incomplete | None = ...,
    plot_colormap: bool = ...,
    **kwargs,
): ...
def create_impedance_collection(
    net,
    impedances: Incomplete | None = ...,
    bus_geodata: Incomplete | None = ...,
    infofunc: Incomplete | None = ...,
    picker: bool = ...,
    **kwargs,
): ...
def create_trafo_connection_collection(
    net,
    trafos: Incomplete | None = ...,
    bus_geodata: Incomplete | None = ...,
    infofunc: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    clim: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    z: Incomplete | None = ...,
    cbar_title: str = ...,
    picker: bool = ...,
    **kwargs,
): ...
def create_trafo3w_connection_collection(
    net, trafos: Incomplete | None = ..., bus_geodata: Incomplete | None = ..., infofunc: Incomplete | None = ..., **kwargs
): ...
def create_trafo_collection(
    net,
    trafos: Incomplete | None = ...,
    picker: bool = ...,
    size: Incomplete | None = ...,
    infofunc: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    z: Incomplete | None = ...,
    clim: Incomplete | None = ...,
    cbar_title: str = ...,
    plot_colormap: bool = ...,
    bus_geodata: Incomplete | None = ...,
    **kwargs,
): ...
def create_trafo3w_collection(
    net,
    trafo3ws: Incomplete | None = ...,
    picker: bool = ...,
    infofunc: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    z: Incomplete | None = ...,
    clim: Incomplete | None = ...,
    cbar_title: str = ...,
    plot_colormap: bool = ...,
    bus_geodata: Incomplete | None = ...,
    **kwargs,
): ...
def create_busbar_collection(
    net,
    buses: Incomplete | None = ...,
    infofunc: Incomplete | None = ...,
    cmap: Incomplete | None = ...,
    norm: Incomplete | None = ...,
    picker: bool = ...,
    z: Incomplete | None = ...,
    cbar_title: str = ...,
    clim: Incomplete | None = ...,
    **kwargs,
): ...
def create_load_collection(
    net,
    loads: Incomplete | None = ...,
    size: float = ...,
    infofunc: Incomplete | None = ...,
    orientation=...,
    picker: bool = ...,
    **kwargs,
): ...
def create_gen_collection(
    net,
    gens: Incomplete | None = ...,
    size: float = ...,
    infofunc: Incomplete | None = ...,
    orientation=...,
    picker: bool = ...,
    **kwargs,
): ...
def create_sgen_collection(
    net,
    sgens: Incomplete | None = ...,
    size: float = ...,
    infofunc: Incomplete | None = ...,
    orientation=...,
    picker: bool = ...,
    **kwargs,
): ...
def create_storage_collection(
    net,
    storages: Incomplete | None = ...,
    size: float = ...,
    infofunc: Incomplete | None = ...,
    orientation=...,
    picker: bool = ...,
    **kwargs,
): ...
def create_ext_grid_collection(
    net,
    size: float = ...,
    infofunc: Incomplete | None = ...,
    orientation: int = ...,
    picker: bool = ...,
    ext_grids: Incomplete | None = ...,
    ext_grid_buses: Incomplete | None = ...,
    **kwargs,
): ...
def create_line_switch_collection(net, size: int = ..., distance_to_bus: int = ..., use_line_geodata: bool = ..., **kwargs): ...
def create_bus_bus_switch_collection(
    net, size: float = ..., helper_line_style: str = ..., helper_line_size: float = ..., helper_line_color: str = ..., **kwargs
): ...
def draw_collections(
    collections,
    figsize=...,
    ax: Incomplete | None = ...,
    plot_colorbars: bool = ...,
    set_aspect: bool = ...,
    axes_visible=...,
    copy_collections: bool = ...,
    draw: bool = ...,
): ...
def add_single_collection(c, ax, plot_colorbars, copy_collections) -> None: ...
def add_collections_to_axes(ax, collections, plot_colorbars: bool = ..., copy_collections: bool = ...) -> None: ...
