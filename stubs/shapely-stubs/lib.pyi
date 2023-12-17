from _typeshed import Incomplete as I
from typing import Any, Generic, Literal as L, SupportsIndex, TypeVar, overload, type_check_only
from typing_extensions import Never, TypeAlias, TypeVarTuple, Unpack

import numpy as np
from numpy._typing import DTypeLike, _ArrayLikeBool_co, _ArrayLikeInt_co, _ShapeLike
from numpy._typing._ufunc import _SupportsArrayUFunc
from numpy.typing import ArrayLike, NDArray

_NIn = TypeVar("_NIn", bound=int)
_NOut = TypeVar("_NOut", bound=int)
_Ts = TypeVarTuple("_Ts")

_UFuncOut: TypeAlias = NDArray[Any] | tuple[NDArray[Any], ...] | None

@type_check_only
class UFunc(np.ufunc, Generic[_NIn, _NOut, _Ts]):  # type: ignore[misc] # pyright: ignore
    @property
    def __name__(self) -> str: ...
    @property
    def ntypes(self) -> L[1]: ...  # All shapely funcs checked have `ntypes=1`
    @property
    def identity(self) -> None: ...  # All shapely funcs checked have `identity=None`
    @property
    def nin(self) -> _NIn: ...
    @property
    def nout(self) -> _NOut: ...
    @property
    def nargs(self) -> int: ...  # nargs = nin + nout (I think!)
    @property
    def signature(self) -> str | None: ...
    @overload  # overload 1: `out` is the last positional argument
    def __call__(
        self,
        *x: Unpack[tuple[Unpack[_Ts], _UFuncOut]],
        where: _ArrayLikeBool_co | None = True,
        casting: np._CastingKind = "same_kind",
        order: np._OrderKACF = "K",
        dtype: DTypeLike = None,
        subok: bool = True,
        signature: str | tuple[None | str, ...] = ...,
        extobj: list[Any] = ...,
    ) -> Any: ...
    @overload  # overload 2: `out` is the first keyword argument
    def __call__(
        self,
        *x: Unpack[_Ts],
        out: _UFuncOut = None,
        where: _ArrayLikeBool_co | None = True,
        casting: np._CastingKind = "same_kind",
        order: np._OrderKACF = "K",
        dtype: DTypeLike = None,
        subok: bool = True,
        signature: str | tuple[None | str, ...] = ...,
        extobj: list[Any] = ...,
    ) -> Any: ...
    @overload  # N_in=1, N_out=1
    def at(self: UFunc[L[1], L[1], Unpack[_Ts]], a: _SupportsArrayUFunc, indices: _ArrayLikeInt_co, /) -> None: ...
    @overload  # N_in=2, N_out=1
    def at(self: UFunc[L[2], L[1], Unpack[_Ts]], a: NDArray[Any], indices: _ArrayLikeInt_co, b: ArrayLike, /) -> None: ...
    # N_in=2, N_out=1 only methods
    def reduce(
        self: UFunc[L[2], L[1], Unpack[_Ts]],
        array: ArrayLike,
        axis: _ShapeLike | None = ...,
        dtype: DTypeLike = ...,
        out: NDArray[Any] | None = ...,
        keepdims: bool = ...,
        initial: Any = ...,
        where: _ArrayLikeBool_co = ...,
    ) -> Any: ...
    def accumulate(
        self: UFunc[L[2], L[1], Unpack[_Ts]],
        array: ArrayLike,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: NDArray[Any] | None = ...,
    ) -> NDArray[Any]: ...
    def reduceat(
        self: UFunc[L[2], L[1], Unpack[_Ts]],
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: NDArray[Any] | None = ...,
    ) -> NDArray[Any]: ...
    def outer(
        self: UFunc[L[2], L[1], Unpack[_Ts]],
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        out: NDArray[Any] | tuple[NDArray[Any]] | None = ...,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | tuple[None | str, ...] = ...,
        extobj: list[Any] = ...,
    ) -> Any: ...

# UFuncs type generator
# ---------------------
# for name in dir(shapely.lib):
#     obj = getattr(shapely.lib, name)
#     if not isinstance(obj, np.ufunc):
#         continue
#     assert obj.ntypes == 1, (obj.__name__, obj.ntypes)
#     assert obj.identity is None, (obj.__name__, obj.identity)
#     assert obj.nargs == obj.nin + obj.nout, (obj.__name__, obj.nargs, obj.nin, obj.nout)
#     out = f"{name}: UFunc[L[{obj.nin!r}], L[{obj.nout!r}]{', I' * obj.nin}]"
#     print(out)
#     print(f'"""{obj.__doc__.strip()}"""\n')

# START GENERATED CODE
area: UFunc[L[1], L[1], I]
"""area(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

boundary: UFunc[L[1], L[1], I]
"""boundary(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

bounds: UFunc[L[1], L[1], I]
"""bounds(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

box: UFunc[L[5], L[1], I, I, I, I, I]
"""box(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

buffer: UFunc[L[7], L[1], I, I, I, I, I, I, I]
"""buffer(x1, x2, x3, x4, x5, x6, x7, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

build_area: UFunc[L[1], L[1], I]
"""build_area(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

centroid: UFunc[L[1], L[1], I]
"""centroid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

clip_by_rect: UFunc[L[5], L[1], I, I, I, I, I]
"""clip_by_rect(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

concave_hull: UFunc[L[3], L[1], I, I, I]
"""concave_hull(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

contains: UFunc[L[2], L[1], I, I]
"""contains(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

contains_properly: UFunc[L[2], L[1], I, I]
"""contains_properly(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

contains_xy: UFunc[L[3], L[1], I, I, I]
"""contains_xy(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

convex_hull: UFunc[L[1], L[1], I]
"""convex_hull(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

coverage_union: UFunc[L[1], L[1], I]
"""coverage_union(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

covered_by: UFunc[L[2], L[1], I, I]
"""covered_by(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

covers: UFunc[L[2], L[1], I, I]
"""covers(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

create_collection: UFunc[L[2], L[1], I, I]
"""create_collection(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

crosses: UFunc[L[2], L[1], I, I]
"""crosses(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

delaunay_triangles: UFunc[L[3], L[1], I, I, I]
"""delaunay_triangles(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

destroy_prepared: UFunc[L[1], L[0], I]
"""destroy_prepared(x, /, out=(), *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

difference: UFunc[L[2], L[1], I, I]
"""difference(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

difference_prec: UFunc[L[3], L[1], I, I, I]
"""difference_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

disjoint: UFunc[L[2], L[1], I, I]
"""disjoint(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

distance: UFunc[L[2], L[1], I, I]
"""distance(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

dwithin: UFunc[L[3], L[1], I, I, I]
"""dwithin(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

envelope: UFunc[L[1], L[1], I]
"""envelope(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

equals: UFunc[L[2], L[1], I, I]
"""equals(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

equals_exact: UFunc[L[3], L[1], I, I, I]
"""equals_exact(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

extract_unique_points: UFunc[L[1], L[1], I]
"""extract_unique_points(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

force_2d: UFunc[L[1], L[1], I]
"""force_2d(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

force_3d: UFunc[L[2], L[1], I, I]
"""force_3d(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

frechet_distance: UFunc[L[2], L[1], I, I]
"""frechet_distance(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

frechet_distance_densify: UFunc[L[3], L[1], I, I, I]
"""frechet_distance_densify(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

from_geojson: UFunc[L[2], L[1], I, I]
"""from_geojson(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

from_wkb: UFunc[L[2], L[1], I, I]
"""from_wkb(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

from_wkt: UFunc[L[2], L[1], I, I]
"""from_wkt(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_coordinate_dimension: UFunc[L[1], L[1], I]
"""get_coordinate_dimension(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_dimensions: UFunc[L[1], L[1], I]
"""get_dimensions(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_exterior_ring: UFunc[L[1], L[1], I]
"""get_exterior_ring(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_geometry: UFunc[L[2], L[1], I, I]
"""get_geometry(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_interior_ring: UFunc[L[2], L[1], I, I]
"""get_interior_ring(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_coordinates: UFunc[L[1], L[1], I]
"""get_num_coordinates(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_geometries: UFunc[L[1], L[1], I]
"""get_num_geometries(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_interior_rings: UFunc[L[1], L[1], I]
"""get_num_interior_rings(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_num_points: UFunc[L[1], L[1], I]
"""get_num_points(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_point: UFunc[L[2], L[1], I, I]
"""get_point(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_precision: UFunc[L[1], L[1], I]
"""get_precision(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_srid: UFunc[L[1], L[1], I]
"""get_srid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_type_id: UFunc[L[1], L[1], I]
"""get_type_id(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_x: UFunc[L[1], L[1], I]
"""get_x(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_y: UFunc[L[1], L[1], I]
"""get_y(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

get_z: UFunc[L[1], L[1], I]
"""get_z(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

has_z: UFunc[L[1], L[1], I]
"""has_z(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

hausdorff_distance: UFunc[L[2], L[1], I, I]
"""hausdorff_distance(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

hausdorff_distance_densify: UFunc[L[3], L[1], I, I, I]
"""hausdorff_distance_densify(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersection: UFunc[L[2], L[1], I, I]
"""intersection(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersection_all: UFunc[L[1], L[1], I]
"""intersection_all(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

intersection_prec: UFunc[L[3], L[1], I, I, I]
"""intersection_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersects: UFunc[L[2], L[1], I, I]
"""intersects(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

intersects_xy: UFunc[L[3], L[1], I, I, I]
"""intersects_xy(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_ccw: UFunc[L[1], L[1], I]
"""is_ccw(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_closed: UFunc[L[1], L[1], I]
"""is_closed(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_empty: UFunc[L[1], L[1], I]
"""is_empty(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_geometry: UFunc[L[1], L[1], I]
"""is_geometry(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_missing: UFunc[L[1], L[1], I]
"""is_missing(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_prepared: UFunc[L[1], L[1], I]
"""is_prepared(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_ring: UFunc[L[1], L[1], I]
"""is_ring(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_simple: UFunc[L[1], L[1], I]
"""is_simple(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_valid: UFunc[L[1], L[1], I]
"""is_valid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_valid_input: UFunc[L[1], L[1], I]
"""is_valid_input(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

is_valid_reason: UFunc[L[1], L[1], I]
"""is_valid_reason(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

length: UFunc[L[1], L[1], I]
"""length(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_interpolate_point: UFunc[L[2], L[1], I, I]
"""line_interpolate_point(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_interpolate_point_normalized: UFunc[L[2], L[1], I, I]
"""line_interpolate_point_normalized(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_locate_point: UFunc[L[2], L[1], I, I]
"""line_locate_point(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_locate_point_normalized: UFunc[L[2], L[1], I, I]
"""line_locate_point_normalized(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_merge: UFunc[L[1], L[1], I]
"""line_merge(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

line_merge_directed: UFunc[L[1], L[1], I]
"""line_merge_directed(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

linearrings: UFunc[L[1], L[1], I]
"""linearrings(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

linestrings: UFunc[L[1], L[1], I]
"""linestrings(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

make_valid: UFunc[L[1], L[1], I]
"""make_valid(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

minimum_bounding_circle: UFunc[L[1], L[1], I]
"""minimum_bounding_circle(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

minimum_bounding_radius: UFunc[L[1], L[1], I]
"""minimum_bounding_radius(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

minimum_clearance: UFunc[L[1], L[1], I]
"""minimum_clearance(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

node: UFunc[L[1], L[1], I]
"""node(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

normalize: UFunc[L[1], L[1], I]
"""normalize(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

offset_curve: UFunc[L[5], L[1], I, I, I, I, I]
"""offset_curve(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

oriented_envelope: UFunc[L[1], L[1], I]
"""oriented_envelope(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

overlaps: UFunc[L[2], L[1], I, I]
"""overlaps(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

point_on_surface: UFunc[L[1], L[1], I]
"""point_on_surface(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

points: UFunc[L[1], L[1], I]
"""points(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

polygonize: UFunc[L[1], L[1], I]
"""polygonize(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

polygonize_full: UFunc[L[1], L[4], I]
"""polygonize_full(x[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

polygons: UFunc[L[2], L[1], I, I]
"""polygons(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

prepare: UFunc[L[1], L[0], I]
"""prepare(x, /, out=(), *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

relate: UFunc[L[2], L[1], I, I]
"""relate(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

relate_pattern: UFunc[L[3], L[1], I, I, I]
"""relate_pattern(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

remove_repeated_points: UFunc[L[2], L[1], I, I]
"""remove_repeated_points(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

reverse: UFunc[L[1], L[1], I]
"""reverse(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

segmentize: UFunc[L[2], L[1], I, I]
"""segmentize(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

set_precision: UFunc[L[3], L[1], I, I, I]
"""set_precision(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

set_srid: UFunc[L[2], L[1], I, I]
"""set_srid(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

shared_paths: UFunc[L[2], L[1], I, I]
"""shared_paths(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

shortest_line: UFunc[L[2], L[1], I, I]
"""shortest_line(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

simplify: UFunc[L[2], L[1], I, I]
"""simplify(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

simplify_preserve_topology: UFunc[L[2], L[1], I, I]
"""simplify_preserve_topology(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

snap: UFunc[L[3], L[1], I, I, I]
"""snap(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

symmetric_difference: UFunc[L[2], L[1], I, I]
"""symmetric_difference(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

symmetric_difference_all: UFunc[L[1], L[1], I]
"""symmetric_difference_all(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])"""

symmetric_difference_prec: UFunc[L[3], L[1], I, I, I]
"""symmetric_difference_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

to_geojson: UFunc[L[2], L[1], I, I]
"""to_geojson(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

to_wkb: UFunc[L[6], L[1], I, I, I, I, I, I]
"""to_wkb(x1, x2, x3, x4, x5, x6, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

to_wkt: UFunc[L[5], L[1], I, I, I, I, I]
"""to_wkt(x1, x2, x3, x4, x5, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

touches: UFunc[L[2], L[1], I, I]
"""touches(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

unary_union: UFunc[L[1], L[1], I]
"""unary_union(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

unary_union_prec: UFunc[L[2], L[1], I, I]
"""unary_union_prec(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

union: UFunc[L[2], L[1], I, I]
"""union(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

union_prec: UFunc[L[3], L[1], I, I, I]
"""union_prec(x1, x2, x3, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

voronoi_polygons: UFunc[L[4], L[1], I, I, I, I]
"""voronoi_polygons(x1, x2, x3, x4, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""

within: UFunc[L[2], L[1], I, I]
"""within(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])"""
# END GENERATED CODE

geos_capi_version: tuple[int, int, int]
geos_capi_version_string: str
geos_version: tuple[int, int, int]
geos_version_string: str
registry: list[Geometry]

class Geometry:
    _geom: int
    _geom_prepared: int
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __ge__(self, other: Never) -> bool: ...
    def __gt__(self, other: Never) -> bool: ...
    def __le__(self, other: Never) -> bool: ...
    def __lt__(self, other: Never) -> bool: ...

class STRtree:
    _ptr: int
    count: int
    @classmethod
    def __init__(cls, geoms: NDArray[Any], node_capacity: SupportsIndex, **kwargs: object) -> None: ...
    def dwithin(self, geoms: NDArray[Any], distances: NDArray[Any], /) -> Any: ...
    def nearest(self, geoms: NDArray[Any], /) -> NDArray[np.int64]: ...
    def query(self, geoms: NDArray[Any], predicate: SupportsIndex, /) -> NDArray[np.int64]: ...
    def query_nearest(
        self, geoms: NDArray[Any], max_distance: float, exclusive: SupportsIndex, all_matches: SupportsIndex, /
    ) -> tuple[NDArray[np.int64], NDArray[np.float64]]: ...

class ShapelyError(Exception): ...
class GEOSException(ShapelyError): ...

def _setup_signal_checks(*args, **kwargs) -> Any: ...
def count_coordinates(geoms: NDArray[Any], /) -> int: ...
def get_coordinates(*args, **kwargs) -> Any: ...
def set_coordinates(*args, **kwargs) -> Any: ...
