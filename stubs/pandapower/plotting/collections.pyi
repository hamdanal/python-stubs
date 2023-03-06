from _typeshed import Incomplete
from collections.abc import Iterable
from typing import TypeVar
from typing_extensions import Self

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import Collection, LineCollection, PatchCollection
from matplotlib.colors import Colormap, Normalize
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from numpy.typing import ArrayLike
from pandapower.auxiliary import pandapowerNet

_CollectionT = TypeVar("_CollectionT", bound=Collection)

MATPLOTLIB_INSTALLED: bool

class CustomTextPath(TextPath):
    s: str
    usetex: bool
    prop: FontProperties
    def __init__(
        self,
        xy: tuple[float, float] | np.ndarray,
        s: str,
        size: float | None = None,
        prop: FontProperties | None = None,
        _interpolation_steps: int = 1,
        usetex: bool = False,
    ) -> None: ...
    def __deepcopy__(self, memo: Incomplete | None = None) -> Self: ...

def create_annotation_collection(
    texts: Iterable[str],
    coords: Iterable[tuple],
    size: float | Iterable[float],
    prop: FontProperties | None = None,
    **kwargs: Incomplete,
) -> PatchCollection: ...
def add_cmap_to_collection(
    collection: _CollectionT,
    cmap: Colormap | str | None,
    norm: Normalize | None,
    z: ArrayLike,
    cbar_title: str,
    plot_colormap: bool = True,
    clim: tuple[float, float] | Iterable[float] | None = None,
) -> _CollectionT: ...
def create_bus_collection(
    net: pandapowerNet,
    buses: Incomplete | None = None,
    size: float = 5,
    patch_type: str = "circle",
    color: Incomplete | None = None,
    z: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    picker: bool = ...,
    bus_geodata: Incomplete | None = None,
    cbar_title: str = ...,
    **kwargs,
) -> PatchCollection | None: ...
def create_line_collection(
    net: pandapowerNet,
    lines: Incomplete | None = None,
    line_geodata: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    use_bus_geodata: bool = ...,
    infofunc: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    picker: bool = ...,
    z: Incomplete | None = None,
    cbar_title: str = ...,
    clim: Incomplete | None = None,
    plot_colormap: bool = True,
    **kwargs,
) -> LineCollection | None: ...
def create_dcline_collection(
    net: pandapowerNet,
    dclines: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    picker: bool = ...,
    z: Incomplete | None = None,
    cbar_title: str = ...,
    clim: Incomplete | None = None,
    plot_colormap: bool = True,
    **kwargs,
) -> LineCollection | None: ...
def create_impedance_collection(
    net: pandapowerNet,
    impedances: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    picker: bool = ...,
    **kwargs,
) -> LineCollection | None: ...
def create_trafo_connection_collection(
    net: pandapowerNet,
    trafos: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    cmap: Incomplete | None = None,
    clim: Incomplete | None = None,
    norm: Incomplete | None = None,
    z: Incomplete | None = None,
    cbar_title: str = ...,
    picker: bool = ...,
    **kwargs,
) -> LineCollection: ...
def create_trafo3w_connection_collection(
    net: pandapowerNet,
    trafos: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    **kwargs,
) -> LineCollection: ...
def create_trafo_collection(
    net: pandapowerNet,
    trafos: Incomplete | None = None,
    picker: bool = ...,
    size: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    z: Incomplete | None = None,
    clim: Incomplete | None = None,
    cbar_title: str = ...,
    plot_colormap: bool = True,
    bus_geodata: Incomplete | None = None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection] | None: ...
def create_trafo3w_collection(
    net: pandapowerNet,
    trafo3ws: Incomplete | None = None,
    picker: bool = ...,
    infofunc: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    z: Incomplete | None = None,
    clim: Incomplete | None = None,
    cbar_title: str = ...,
    plot_colormap: bool = True,
    bus_geodata: Incomplete | None = None,
    **kwargs,
) -> tuple[None, None] | tuple[LineCollection, PatchCollection]: ...
def create_busbar_collection(
    net: pandapowerNet,
    buses: Incomplete | None = None,
    infofunc: Incomplete | None = None,
    cmap: Incomplete | None = None,
    norm: Incomplete | None = None,
    picker: bool = ...,
    z: Incomplete | None = None,
    cbar_title: str = ...,
    clim: Incomplete | None = None,
    **kwargs,
) -> LineCollection | None: ...
def create_load_collection(
    net: pandapowerNet,
    loads: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Incomplete | None = None,
    orientation: float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_gen_collection(
    net: pandapowerNet,
    gens: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Incomplete | None = None,
    orientation: float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_sgen_collection(
    net: pandapowerNet,
    sgens: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Incomplete | None = None,
    orientation: float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_storage_collection(
    net: pandapowerNet,
    storages: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Incomplete | None = None,
    orientation: float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_ext_grid_collection(
    net: pandapowerNet,
    size: float = 1.0,
    infofunc: Incomplete | None = None,
    orientation: float = 0,
    picker: bool = False,
    ext_grids: Incomplete | None = None,
    ext_grid_buses: Incomplete | None = None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_line_switch_collection(
    net: pandapowerNet, size: float = 1.0, distance_to_bus: float = 3, use_line_geodata: bool = False, **kwargs
) -> PatchCollection: ...
def create_bus_bus_switch_collection(
    net: pandapowerNet,
    size: float = 1.0,
    helper_line_style: str = ":",
    helper_line_size: float = 1.0,
    helper_line_color: str = "gray",
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def draw_collections(
    collections: Iterable[Collection],
    figsize: tuple[float, float] = ...,
    ax: Axes | None = None,
    plot_colorbars: bool = True,
    set_aspect: bool = True,
    axes_visible: tuple[bool, bool] = ...,
    copy_collections: bool = True,
    draw: bool = True,
) -> Axes: ...
def add_single_collection(c: Collection, ax: Axes, plot_colorbars: bool, copy_collections: bool) -> None: ...
def add_collections_to_axes(
    ax: Axes, collections: Iterable[Collection], plot_colorbars: bool = True, copy_collections: bool = True
) -> None: ...
