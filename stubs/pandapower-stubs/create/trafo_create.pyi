from collections.abc import Collection

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet
from pandapower.pp_types import HVLVType, HVMVLVType, TapChangerWithTabularType

def create_transformer(
    net: pandapowerNet,
    hv_bus: Int,
    lv_bus: Int,
    std_type: str,
    name: str | None = None,
    tap_pos: Int | float = ...,  # float because default value is nan
    in_service: Bool = True,
    index: Int | None = None,
    max_loading_percent: Float = ...,
    parallel: Int = 1,
    df: Float = 1.0,
    tap_changer_type: TapChangerWithTabularType | None = None,
    tap_dependency_table: Bool = False,
    id_characteristic_table: Int | None = None,
    pt_percent: Float = ...,
    oltc: Bool = False,
    xn_ohm: Float = ...,
    tap2_pos: Int | float = ...,  # float because default value is nan
    **kwargs,
) -> np.int64: ...
def create_transformers(
    net: pandapowerNet,
    hv_buses: Collection[Int],
    lv_buses: Collection[Int],
    std_type: str,
    name: ScalarOrVector[str] | None = None,
    tap_pos: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    in_service: ScalarOrVector[Bool] = True,
    index: Collection[Int] | None = None,
    max_loading_percent: ScalarOrVector[Float] = ...,
    parallel: ScalarOrVector[Int] = 1,
    df: ScalarOrVector[Float] = 1.0,
    tap_changer_type: ScalarOrVector[TapChangerWithTabularType] | None = None,
    tap_dependency_table: ScalarOrVector[Bool] = False,
    id_characteristic_table: ScalarOrVector[Int] | None = None,
    pt_percent: ScalarOrVector[Float] = ...,
    oltc: ScalarOrVector[Bool] = False,
    xn_ohm: ScalarOrVector[Float] = ...,
    tap2_pos: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    **kwargs,
) -> Array1D[np.int64]: ...
def create_transformer_from_parameters(
    net: pandapowerNet,
    hv_bus: Int,
    lv_bus: Int,
    sn_mva: Float,
    vn_hv_kv: Float,
    vn_lv_kv: Float,
    vkr_percent: Float,
    vk_percent: Float,
    pfe_kw: Float,
    i0_percent: Float,
    shift_degree: Float = 0,
    tap_side: HVLVType | None = None,
    tap_neutral: Int | float = ...,  # float because default value is nan
    tap_max: Int | float = ...,  # float because default value is nan
    tap_min: Int | float = ...,  # float because default value is nan
    tap_step_percent: Float = ...,
    tap_step_degree: Float = ...,
    tap_pos: Int | float = ...,  # float because default value is nan
    tap_changer_type: TapChangerWithTabularType | None = None,
    id_characteristic_table: Int | None = None,
    in_service: Bool = True,
    name: str | None = None,
    vector_group: str | None = None,
    index: Int | None = None,
    max_loading_percent: Float = ...,
    parallel: Int = 1,
    df: Float = 1.0,
    vk0_percent: Float = ...,
    vkr0_percent: Float = ...,
    mag0_percent: Float = ...,
    mag0_rx: Float = ...,
    si0_hv_partial: Float = ...,
    pt_percent: Float = ...,
    oltc: Bool = False,
    tap_dependency_table: Bool = False,
    xn_ohm: Float = ...,
    tap2_side: HVLVType | None = None,
    tap2_neutral: Int | float = ...,  # float because default value is nan
    tap2_max: Int | float = ...,  # float because default value is nan
    tap2_min: Int | float = ...,  # float because default value is nan
    tap2_step_percent: Float = ...,
    tap2_step_degree: Float = ...,
    tap2_pos: Int | float = ...,  # float because default value is nan
    tap2_changer_type: TapChangerWithTabularType | None = None,
    **kwargs,
) -> np.int64: ...
def create_transformers_from_parameters(
    net: pandapowerNet,
    hv_buses: Collection[Int],
    lv_buses: Collection[Int],
    sn_mva: ScalarOrVector[Float],
    vn_hv_kv: ScalarOrVector[Float],
    vn_lv_kv: ScalarOrVector[Float],
    vkr_percent: ScalarOrVector[Float],
    vk_percent: ScalarOrVector[Float],
    pfe_kw: ScalarOrVector[Float],
    i0_percent: ScalarOrVector[Float],
    shift_degree: ScalarOrVector[Float] = 0,
    tap_side: ScalarOrVector[HVLVType] | None = None,
    tap_neutral: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_max: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_min: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_step_percent: ScalarOrVector[Float] = ...,
    tap_step_degree: ScalarOrVector[Float] = ...,
    tap_pos: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_changer_type: ScalarOrVector[TapChangerWithTabularType] | None = None,
    id_characteristic_table: ScalarOrVector[Int] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    name: ScalarOrVector[str] | None = None,
    vector_group: ScalarOrVector[str] | None = None,
    index: Collection[Int] | None = None,
    max_loading_percent: ScalarOrVector[Float] = ...,
    parallel: ScalarOrVector[Int] = 1,
    df: ScalarOrVector[Float] = 1.0,
    vk0_percent: ScalarOrVector[Float] = ...,
    vkr0_percent: ScalarOrVector[Float] = ...,
    mag0_percent: ScalarOrVector[Float] = ...,
    mag0_rx: ScalarOrVector[Float] = ...,
    si0_hv_partial: ScalarOrVector[Float] = ...,
    pt_percent: ScalarOrVector[Float] = ...,
    oltc: ScalarOrVector[Bool] = False,
    tap_dependency_table: ScalarOrVector[Bool] = False,
    xn_ohm: ScalarOrVector[Float] = ...,
    tap2_side: ScalarOrVector[HVLVType] | None = None,
    tap2_neutral: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap2_max: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap2_min: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap2_step_percent: ScalarOrVector[Float] = ...,
    tap2_step_degree: ScalarOrVector[Float] = ...,
    tap2_pos: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap2_changer_type: ScalarOrVector[TapChangerWithTabularType] | None = None,
    **kwargs,
) -> Array1D[np.int64]: ...
def create_transformer3w(
    net: pandapowerNet,
    hv_bus: Int,
    mv_bus: Int,
    lv_bus: Int,
    std_type: str,
    name: str | None = None,
    tap_pos: Int | float = ...,  # float because default value is nan
    in_service: Bool = True,
    index: Int | None = None,
    max_loading_percent: Float = ...,
    tap_changer_type: TapChangerWithTabularType | None = None,
    tap_at_star_point: Bool = False,
    tap_dependency_table: Bool = False,
    id_characteristic_table: Int | None = None,
    **kwargs,
) -> np.int64: ...
def create_transformers3w(
    net: pandapowerNet,
    hv_buses: Collection[Int],
    mv_buses: Collection[Int],
    lv_buses: Collection[Int],
    std_type: str,
    tap_pos: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    name: ScalarOrVector[str] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    index: Collection[Int] | None = None,
    max_loading_percent: ScalarOrVector[Float] = ...,
    tap_at_star_point: ScalarOrVector[Bool] = False,
    tap_changer_type: ScalarOrVector[TapChangerWithTabularType] | None = None,
    tap_dependency_table: ScalarOrVector[Bool] = False,
    id_characteristic_table: ScalarOrVector[Int] | None = None,
    **kwargs,
) -> Array1D[np.int64]: ...
def create_transformer3w_from_parameters(
    net: pandapowerNet,
    hv_bus: Int,
    mv_bus: Int,
    lv_bus: Int,
    vn_hv_kv: Float,
    vn_mv_kv: Float,
    vn_lv_kv: Float,
    sn_hv_mva: Float,
    sn_mv_mva: Float,
    sn_lv_mva: Float,
    vk_hv_percent: Float,
    vk_mv_percent: Float,
    vk_lv_percent: Float,
    vkr_hv_percent: Float,
    vkr_mv_percent: Float,
    vkr_lv_percent: Float,
    pfe_kw: Float,
    i0_percent: Float,
    shift_mv_degree: Float = 0.0,
    shift_lv_degree: Float = 0.0,
    tap_side: HVMVLVType | None = None,
    tap_step_percent: Float = ...,
    tap_step_degree: Float = ...,
    tap_pos: Int | float = ...,  # float because default value is nan
    tap_neutral: Int | float = ...,  # float because default value is nan
    tap_max: Int | float = ...,  # float because default value is nan
    tap_changer_type: TapChangerWithTabularType | None = None,
    tap_min: Int | float = ...,  # float because default value is nan
    name: str | None = None,
    in_service: Bool = True,
    index: Int | None = None,
    max_loading_percent: Float = ...,
    tap_at_star_point: Bool = False,
    vk0_hv_percent: Float = ...,
    vk0_mv_percent: Float = ...,
    vk0_lv_percent: Float = ...,
    vkr0_hv_percent: Float = ...,
    vkr0_mv_percent: Float = ...,
    vkr0_lv_percent: Float = ...,
    vector_group: str | None = None,
    tap_dependency_table: Bool = False,
    id_characteristic_table: Int | None = None,
    **kwargs,
) -> np.int64: ...
def create_transformers3w_from_parameters(
    net: pandapowerNet,
    hv_buses: Collection[Int],
    mv_buses: Collection[Int],
    lv_buses: Collection[Int],
    vn_hv_kv: ScalarOrVector[Float],
    vn_mv_kv: ScalarOrVector[Float],
    vn_lv_kv: ScalarOrVector[Float],
    sn_hv_mva: ScalarOrVector[Float],
    sn_mv_mva: ScalarOrVector[Float],
    sn_lv_mva: ScalarOrVector[Float],
    vk_hv_percent: ScalarOrVector[Float],
    vk_mv_percent: ScalarOrVector[Float],
    vk_lv_percent: ScalarOrVector[Float],
    vkr_hv_percent: ScalarOrVector[Float],
    vkr_mv_percent: ScalarOrVector[Float],
    vkr_lv_percent: ScalarOrVector[Float],
    pfe_kw: ScalarOrVector[Float],
    i0_percent: ScalarOrVector[Float],
    shift_mv_degree: ScalarOrVector[Float] = 0.0,
    shift_lv_degree: ScalarOrVector[Float] = 0.0,
    tap_side: ScalarOrVector[HVMVLVType] | None = None,
    tap_step_percent: ScalarOrVector[Float] = ...,
    tap_step_degree: ScalarOrVector[Float] = ...,
    tap_pos: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_neutral: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_max: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    tap_min: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    name: ScalarOrVector[str] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    index: Collection[Int] | None = None,
    max_loading_percent: ScalarOrVector[Float] = ...,
    tap_at_star_point: ScalarOrVector[Bool] = False,
    tap_changer_type: ScalarOrVector[TapChangerWithTabularType] | None = None,
    vk0_hv_percent: ScalarOrVector[Float] = ...,
    vk0_mv_percent: ScalarOrVector[Float] = ...,
    vk0_lv_percent: ScalarOrVector[Float] = ...,
    vkr0_hv_percent: ScalarOrVector[Float] = ...,
    vkr0_mv_percent: ScalarOrVector[Float] = ...,
    vkr0_lv_percent: ScalarOrVector[Float] = ...,
    vector_group: ScalarOrVector[str] | None = None,
    tap_dependency_table: ScalarOrVector[Bool] = False,
    id_characteristic_table: ScalarOrVector[Int] | None = None,
    **kwargs,
) -> Array1D[np.int64]: ...
