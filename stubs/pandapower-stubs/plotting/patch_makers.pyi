from _typeshed import Incomplete, Unused
from collections.abc import Collection

import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, Patch, Rectangle, RegularPolygon
from matplotlib.typing import ColorType
from numpy.typing import NDArray

from pandapower._typing import Float, ScalarOrVector

def node_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    patch_type: str,
    colors: ScalarOrVector[ColorType] | None = None,
    *,
    width: Float = ...,
    height: Float = ...,
    angle: Float = ...,
    **kwargs,
) -> list[Patch]: ...
def ellipse_patches(
    node_coords: Collection[tuple[Float, Float]],
    width: Float,
    height: Float,
    angle: ScalarOrVector[Float] = 0,
    color: ScalarOrVector[ColorType] | None = None,
    **kwargs,
) -> list[Ellipse]: ...
def rectangle_patches(
    node_coords: Collection[tuple[Float, Float]],
    width: Float,
    height: Float,
    color: ScalarOrVector[ColorType] | None = None,
    **kwargs,
) -> list[Rectangle]: ...
def polygon_patches(
    node_coords: Collection[tuple[Float, Float]],
    radius: Float,
    num_edges: int,
    color: ScalarOrVector[ColorType] | None = None,
    **kwargs,
) -> list[RegularPolygon]: ...
def load_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles: ScalarOrVector[Float],
    *,
    offset: Float = ...,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = "w",
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[RegularPolygon], set[str]]: ...
def gen_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles: ScalarOrVector[Float],
    *,
    offset: Float = ...,
    patch_edgecolor: ScalarOrVector[ColorType] = "k",
    patch_facecolor: ScalarOrVector[ColorType] = (1, 0, 0, 0),
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Arc | Circle], set[str]]: ...
def sgen_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles,
    *,
    offset: Float = ...,
    r_triangles: Float = ...,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = "w",
    **kwargs,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Circle | RegularPolygon], set[str]]: ...
def storage_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles: ScalarOrVector[Float],
    *,
    offset: Float = ...,
    r_triangle: Float = ...,
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[RegularPolygon], set[str]]: ...
def ext_grid_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles: ScalarOrVector[Float],
    *,
    offset: Float = ...,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = "w",
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Rectangle], set[str]]: ...
def trafo_patches(
    coords: Collection[tuple[tuple[Float, Float], tuple[Float, Float]]],
    size: Float,
    *,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = (1, 0, 0, 0),
    linewidths: ScalarOrVector[Float] = 2.0,
    **kwargs: Unused,
) -> tuple[list[tuple[NDArray[np.float64], NDArray[np.float64]]], list[Circle], set[str]]: ...
def ward_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles: ScalarOrVector[Float],
    *,
    offset: Float = ...,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = "w",
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Rectangle], set[str]]: ...
def xward_patches(
    node_coords: Collection[Incomplete],
    size: Float,
    angles: ScalarOrVector[Float],
    *,
    offset: Float = ...,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = "w",
    **kwargs: Unused,
) -> tuple[list[tuple[Incomplete, Incomplete]], list[Rectangle], set[str]]: ...
def vsc_patches(
    coords: Collection[tuple[tuple[Float, Float], tuple[Float, Float]]],
    size: Float,
    *,
    patch_edgecolor: ScalarOrVector[ColorType] = "w",
    patch_facecolor: ScalarOrVector[ColorType] = (1, 0, 0, 0),
    linewidths: ScalarOrVector[Float] = 2.0,
    **kwargs: Unused,
) -> tuple[list[tuple[NDArray[np.float64], NDArray[np.float64]]], list[Circle], set[str]]: ...
