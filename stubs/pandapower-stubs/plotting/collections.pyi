from _typeshed import Incomplete
from collections.abc import Callable, Collection as SizedIterable, Iterable, Sequence
from typing import Any, Literal, TypeVar
from typing_extensions import Self

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import Collection, LineCollection, PatchCollection
from matplotlib.colors import Colormap, Normalize
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from matplotlib.typing import ColorType, LineStyleType
from numpy.typing import ArrayLike, NDArray

from pandapower.auxiliary import pandapowerNet

_CollectionT = TypeVar("_CollectionT", bound=Collection)

MATPLOTLIB_INSTALLED: bool

class CustomTextPath(TextPath):
    s: str
    usetex: bool
    prop: FontProperties
    def __init__(
        self,
        xy: tuple[float, float] | NDArray[np.float64],
        s: str,
        size: float | None = None,
        prop: FontProperties | None = None,
        _interpolation_steps: int = 1,
        usetex: bool = False,
    ) -> None: ...
    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Self: ...

def create_annotation_collection(
    texts: Iterable[str],
    coords: Iterable[tuple[float, float]],
    size: float | Iterable[float],
    prop: FontProperties | None = None,
    **kwargs: Incomplete,
) -> PatchCollection: ...
def add_cmap_to_collection(
    collection: _CollectionT,
    cmap: Colormap | str | None,
    norm: Normalize | str | None,
    z: ArrayLike,
    cbar_title: str,
    plot_colormap: bool = True,
    clim: float | tuple[float, float] | None = None,
) -> _CollectionT: ...
def create_bus_collection(
    net: pandapowerNet,
    buses: Incomplete | None = None,
    size: float = 5,
    patch_type: str = "circle",
    color: ColorType | SizedIterable[ColorType] | None = None,
    z: Incomplete | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    picker: bool = False,
    bus_geodata: Incomplete | None = None,
    cbar_title: str = "Bus Voltage [pu]",
    **kwargs,
) -> PatchCollection | None: ...
def create_line_collection(
    net: pandapowerNet,
    lines: Incomplete | None = None,
    line_geodata: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    use_bus_geodata: bool = False,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    picker: bool = False,
    z: Incomplete | None = None,
    cbar_title: str = "Line Loading [%]",
    clim: Incomplete | None = None,
    plot_colormap: bool = True,
    **kwargs,
) -> LineCollection | None: ...
def create_dcline_collection(
    net: pandapowerNet,
    dclines: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    picker: bool = False,
    z: Incomplete | None = None,
    cbar_title: str = "HVDC-Line Loading [%]",
    clim: Incomplete | None = None,
    plot_colormap: bool = True,
    **kwargs,
) -> LineCollection | None: ...
def create_impedance_collection(
    net: pandapowerNet,
    impedances: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    picker: bool = False,
    **kwargs,
) -> LineCollection | None: ...
def create_trafo_connection_collection(
    net: pandapowerNet,
    trafos: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    cmap: Colormap | str | None = None,
    clim: Incomplete | None = None,
    norm: Normalize | str | None = None,
    z: Incomplete | None = None,
    cbar_title: str = "Transformer Loading",
    picker: bool = False,
    **kwargs,
) -> LineCollection: ...
def create_trafo3w_connection_collection(
    net: pandapowerNet,
    trafos: Incomplete | None = None,
    bus_geodata: Incomplete | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    **kwargs,
) -> LineCollection: ...
def create_trafo_collection(
    net: pandapowerNet,
    trafos: Incomplete | None = None,
    picker: bool = False,
    size: Incomplete | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    z: Incomplete | None = None,
    clim: Incomplete | None = None,
    cbar_title: str = "Transformer Loading",
    plot_colormap: bool = True,
    bus_geodata: Incomplete | None = None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection] | None: ...
def create_trafo3w_collection(
    net: pandapowerNet,
    trafo3ws: Incomplete | None = None,
    picker: bool = False,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    z: Incomplete | None = None,
    clim: Incomplete | None = None,
    cbar_title: str = "3W-Transformer Loading",
    plot_colormap: bool = True,
    bus_geodata: Incomplete | None = None,
    **kwargs,
) -> tuple[None, None] | tuple[LineCollection, PatchCollection]: ...
def create_busbar_collection(
    net: pandapowerNet,
    buses: Incomplete | None = None,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    picker: bool = False,
    z: Incomplete | None = None,
    cbar_title: str = "Bus Voltage [p.u.]",
    clim: Incomplete | None = None,
    **kwargs,
) -> LineCollection | None: ...
def create_load_collection(
    net: pandapowerNet,
    loads: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    orientation: float = 3.14159265,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_gen_collection(
    net: pandapowerNet,
    gens: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    orientation: float = 3.14159265,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_sgen_collection(
    net: pandapowerNet,
    sgens: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    orientation: float = 3.14159265,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_storage_collection(
    net: pandapowerNet,
    storages: Incomplete | None = None,
    size: float = 1.0,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
    orientation: float = 3.14159265,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_ext_grid_collection(
    net: pandapowerNet,
    size: float = 1.0,
    infofunc: Callable[[int], tuple[str, int]] | None = None,
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
    helper_line_style: LineStyleType | Sequence[LineStyleType] = ":",
    helper_line_size: float = 1.0,
    helper_line_color: ColorType | Sequence[ColorType] = "gray",
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def draw_collections(
    collections: Iterable[Collection],
    figsize: tuple[float, float] = (10, 8),
    ax: Axes | None = None,
    plot_colorbars: bool = True,
    set_aspect: bool = True,
    axes_visible: tuple[bool, bool] = (False, False),
    copy_collections: bool = True,
    draw: bool = True,
    aspect: tuple[Literal["auto", "equal"] | float, Literal["box", "datalim"] | None] = ("equal", "datalim"),
    autoscale: tuple[bool | None, bool, bool] = (True, True, True),
) -> Axes: ...
def add_single_collection(c: Collection, ax: Axes, plot_colorbars: bool, copy_collections: bool) -> None: ...
def add_collections_to_axes(
    ax: Axes,
    collections: Iterable[Collection | list[Collection] | tuple[Collection, ...]],
    plot_colorbars: bool = True,
    copy_collections: bool = True,
) -> None: ...
