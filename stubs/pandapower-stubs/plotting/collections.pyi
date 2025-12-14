from collections.abc import Callable, Collection as abc_Collection, Iterable
from typing import Any, Literal, Self
from typing_extensions import deprecated

import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.collections import Collection, LineCollection, PatchCollection
from matplotlib.colors import Colormap, Normalize
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from matplotlib.typing import ColorType, LineStyleType
from numpy.typing import ArrayLike, NDArray

from pandapower._typing import Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

class CustomTextPath(TextPath):
    s: str
    usetex: bool
    prop: FontProperties
    def __init__(
        self,
        xy: tuple[Float, Float] | NDArray[np.float64],
        s: str,
        size: Float | None = None,
        prop: FontProperties | None = None,
        _interpolation_steps: Int = 1,
        usetex: bool = False,
    ) -> None: ...
    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Self: ...

def create_annotation_collection(
    texts: Iterable[str],
    coords: Iterable[tuple[Float, Float]],
    size: ScalarOrVector[Float],
    prop: FontProperties | None = None,
    **kwargs,
) -> PatchCollection: ...
def add_cmap_to_collection[C: Collection](
    collection: C,
    cmap: Colormap | str | None,
    norm: Normalize | str | None,
    z: ArrayLike,
    cbar_title: str,
    plot_colormap: bool = True,
    clim: Float | tuple[Float, Float] | None = None,
) -> C: ...
def create_bus_collection(
    net: pandapowerNet,
    buses: abc_Collection[Int] | None = None,
    size: Float = 5.0,
    patch_type: str = "circle",
    color: ScalarOrVector[ColorType] | None = None,
    z: ArrayLike | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    picker: bool = False,
    bus_geodata: pd.DataFrame | None = None,
    bus_table: str = "bus",
    cbar_title: str = "Bus Voltage [pu]",
    clim: Float | tuple[Float, Float] | None = None,
    plot_colormap: bool = True,
    **kwargs,
) -> PatchCollection | None: ...
def create_line_collection(
    net: pandapowerNet,
    lines: abc_Collection[Int] | None = None,
    line_geodata: pd.DataFrame | None = None,
    bus_geodata: pd.DataFrame | None = None,
    use_bus_geodata: bool = False,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    picker: bool = False,
    z: ArrayLike | None = None,
    cbar_title: str = "Line Loading [%]",
    clim: Float | tuple[Float, Float] | None = None,
    plot_colormap: bool = True,
    line_table: Literal["line", "line_dc"] = "line",
    **kwargs,
) -> LineCollection | None: ...
def create_dcline_collection(
    net: pandapowerNet,
    dclines: abc_Collection[Int] | None = None,
    line_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    picker: bool = False,
    z: ArrayLike | None = None,
    cbar_title: str = "HVDC-Line Loading [%]",
    clim: Float | tuple[Float, Float] | None = None,
    plot_colormap: bool = True,
    **kwargs,
) -> LineCollection | None: ...
def create_impedance_collection(
    net: pandapowerNet,
    impedances: abc_Collection[Int] | None = None,
    bus_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    picker: bool = False,
    **kwargs,
) -> LineCollection | None: ...
def create_trafo_connection_collection(
    net: pandapowerNet,
    trafos: abc_Collection[Int] | None = None,
    bus_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    clim: Float | tuple[Float, Float] | None = None,
    norm: Normalize | str | None = None,
    z: ArrayLike | None = None,
    cbar_title: str = "Transformer Loading",
    picker: bool = False,
    **kwargs,
) -> LineCollection: ...
def create_trafo3w_connection_collection(
    net: pandapowerNet,
    trafos: abc_Collection[Int] | None = None,
    bus_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    **kwargs,
) -> LineCollection: ...
def create_trafo_collection(
    net: pandapowerNet,
    trafos: abc_Collection[Int] | None = None,
    picker: bool = False,
    size: Float | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    z: ArrayLike | None = None,
    clim: Float | tuple[Float, Float] | None = None,
    cbar_title: str = "Transformer Loading",
    plot_colormap: bool = True,
    bus_geodata: pd.DataFrame | None = None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection] | None: ...
def create_trafo3w_collection(
    net: pandapowerNet,
    trafo3ws: abc_Collection[Int] | None = None,
    picker: bool = False,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    z: ArrayLike | None = None,
    clim: Float | tuple[Float, Float] | None = None,
    cbar_title: str = "3W-Transformer Loading",
    plot_colormap: bool = True,
    bus_geodata: pd.DataFrame | None = None,
    **kwargs,
) -> tuple[None, None] | tuple[LineCollection, PatchCollection]: ...
def create_vsc_collection(
    net: pandapowerNet,
    vscs: abc_Collection[Int] | None = None,
    picker: bool = False,
    size: Float | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    z: ArrayLike | None = None,
    clim: Float | tuple[Float, Float] | None = None,
    cbar_title: str = "VSC power",
    plot_colormap=True,
    bus_geodata=None,
    bus_dc_geodata=None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection] | None: ...
def create_vsc_connection_collection(
    net: pandapowerNet,
    vscs: abc_Collection[Int] | None = None,
    bus_geodata: pd.DataFrame | None = None,
    bus_dc_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    clim: Float | tuple[Float, Float] | None = None,
    norm: Normalize | str | None = None,
    z: ArrayLike | None = None,
    cbar_title: str = "Transformer Loading",
    picker: bool = False,
    **kwargs,
) -> LineCollection: ...
@deprecated("Busbar geodata is no longer supported for plotting geodata.")
def create_busbar_collection(
    net: pandapowerNet,
    buses: abc_Collection[Int] | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    cmap: Colormap | str | None = None,
    norm: Normalize | str | None = None,
    picker: bool = False,
    z: ArrayLike | None = None,
    cbar_title: str = "Bus Voltage [p.u.]",
    clim: Float | tuple[Float, Float] | None = None,
    **kwargs,
) -> LineCollection | None: ...
def create_load_collection(
    net: pandapowerNet,
    loads: abc_Collection[Int] | None = None,
    size: Float = 1.0,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    orientation: Float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_gen_collection(
    net: pandapowerNet,
    gens: abc_Collection[Int] | None = None,
    size: Float = 1.0,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    orientation: Float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_sgen_collection(
    net: pandapowerNet,
    sgens: abc_Collection[Int] | None = None,
    size: Float = 1.0,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    orientation: Float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_storage_collection(
    net: pandapowerNet,
    storages: abc_Collection[Int] | None = None,
    size: Float = 1.0,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    orientation: Float = ...,
    picker: bool = False,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_ext_grid_collection(
    net: pandapowerNet,
    ext_grids: abc_Collection[Int] | None = None,
    size: Float = 1.0,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    orientation: Float = 0,
    picker: bool = False,
    ext_grid_buses: abc_Collection[Int] | None = None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_line_switch_collection(
    net: pandapowerNet,
    switches: abc_Collection[Int] | None = None,
    size: Float = 1,
    distance_to_bus: Float = 3,
    use_line_geodata: bool = False,
    **kwargs,
) -> PatchCollection: ...
def create_bus_bus_switch_collection(
    net: pandapowerNet,
    size: Float = 1.0,
    helper_line_style: ScalarOrVector[LineStyleType] = ":",
    helper_line_size: Float = 1.0,
    helper_line_color: ScalarOrVector[ColorType] = "gray",
    switches: abc_Collection[Int] | None = None,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_ward_collection(
    net: pandapowerNet,
    wards: abc_Collection[Int] | None = None,
    ward_buses: abc_Collection[Int] | None = None,
    size: Float = 5.0,
    bus_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    picker: bool = False,
    orientation: Float = 0,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def create_xward_collection(
    net: pandapowerNet,
    xwards: abc_Collection[Int] | None = None,
    xward_buses: abc_Collection[Int] | None = None,
    size: Float = 5.0,
    bus_geodata: pd.DataFrame | None = None,
    infofunc: Callable[[int], tuple[str, Int]] | None = None,
    picker: bool = False,
    orientation: Float = 0,
    **kwargs,
) -> tuple[PatchCollection, LineCollection]: ...
def draw_collections(
    collections: Iterable[Collection],
    figsize: tuple[Float, Float] = (10, 8),
    ax: Axes | None = None,
    plot_colorbars: bool = True,
    set_aspect: bool = True,
    axes_visible: tuple[bool, bool] = (False, False),
    copy_collections: bool = True,
    draw: bool = True,
    aspect: tuple[Literal["auto", "equal"] | Float, Literal["box", "datalim"] | None] = ("equal", "datalim"),
    autoscale: tuple[bool | None, bool, bool] = (True, True, True),
) -> Axes: ...
def add_single_collection(c: Collection, ax: Axes, plot_colorbars: bool, copy_collections: bool) -> None: ...
def add_collections_to_axes(
    ax: Axes,
    collections: Iterable[Collection | list[Collection] | tuple[Collection, ...]],
    plot_colorbars: bool = True,
    copy_collections: bool = True,
) -> None: ...
