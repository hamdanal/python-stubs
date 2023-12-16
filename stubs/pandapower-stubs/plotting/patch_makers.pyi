from _typeshed import Incomplete, Unused
from collections.abc import Collection

import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, Patch, Rectangle, RegularPolygon
from matplotlib.typing import ColorType
from numpy.typing import NDArray

MATPLOTLIB_INSTALLED: bool

def node_patches(
    node_coords: Collection[Incomplete],
    size: float,
    patch_type: str,
    colors: ColorType | Collection[ColorType] | None = None,
    *,
    width: float = ...,
    height: float = ...,
    angle: float = ...,
    **kwargs,
) -> list[Patch]: ...
def ellipse_patches(
    node_coords: Collection[tuple[float, float]],
    width: float,
    height: float,
    angle: float | Collection[float] = 0,
    color: ColorType | Collection[ColorType] | None = None,
    **kwargs,
) -> list[Ellipse]: ...
def rectangle_patches(
    node_coords: Collection[tuple[float, float]],
    width: float,
    height: float,
    color: ColorType | Collection[ColorType] | None = None,
    **kwargs,
) -> list[Rectangle]: ...
def polygon_patches(
    node_coords: Collection[tuple[float, float]],
    radius: float,
    num_edges: int,
    color: ColorType | Collection[ColorType] | None = None,
    **kwargs,
) -> list[RegularPolygon]: ...
def load_patches(
    node_coords: Collection[Incomplete],
    size: float,
    angles: float | Collection[float],
    *,
    offset: float = ...,
    patch_edgecolor: ColorType | Collection[ColorType] = "w",
    patch_facecolor: ColorType | Collection[ColorType] = "w",
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[RegularPolygon], set[str]]: ...
def gen_patches(
    node_coords: Collection[Incomplete],
    size: float,
    angles: float | Collection[float],
    *,
    offset: float = ...,
    patch_edgecolor: ColorType | Collection[ColorType] = "k",
    patch_facecolor: ColorType | Collection[ColorType] = (1, 0, 0, 0),
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Arc | Circle], set[str]]: ...
def sgen_patches(
    node_coords: Collection[Incomplete],
    size: float,
    angles,
    *,
    offset: float = ...,
    r_triangles: float = ...,
    patch_edgecolor: ColorType | Collection[ColorType] = "w",
    patch_facecolor: ColorType | Collection[ColorType] = "w",
    **kwargs,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Circle | RegularPolygon], set[str]]: ...
def storage_patches(
    node_coords: Collection[Incomplete],
    size: float,
    angles: float | Collection[float],
    *,
    offset: float = ...,
    r_triangle: float = ...,
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[RegularPolygon], set[str]]: ...
def ext_grid_patches(
    node_coords: Collection[Incomplete],
    size: float,
    angles: float | Collection[float],
    *,
    offset: float = ...,
    patch_edgecolor: ColorType | Collection[ColorType] = "w",
    patch_facecolor: ColorType | Collection[ColorType] = "w",
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Rectangle], set[str]]: ...
def trafo_patches(
    coords: Collection[tuple[tuple[float, float], tuple[float, float]]],
    size: float,
    *,
    patch_edgecolor: ColorType | Collection[ColorType] = "w",
    patch_facecolor: ColorType | Collection[ColorType] = (1, 0, 0, 0),
    linewidths: float | Collection[float] = 2.0,
    **kwargs: Unused,
) -> tuple[list[tuple[NDArray[np.float64], NDArray[np.float64]]], list[Circle], set[str]]: ...
