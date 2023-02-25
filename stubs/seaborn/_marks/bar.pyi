from matplotlib.artist import Artist as Artist
from seaborn._core.scales import Scale as Scale
from seaborn._marks.base import (
    Mappable as Mappable,
    MappableBool as MappableBool,
    MappableColor as MappableColor,
    MappableFloat as MappableFloat,
    MappableStyle as MappableStyle,
    Mark as Mark,
    document_properties as document_properties,
    resolve_color as resolve_color,
    resolve_properties as resolve_properties,
)
from seaborn.external.version import Version as Version

class BarBase(Mark): ...

class Bar(BarBase):
    color: MappableColor
    alpha: MappableFloat
    fill: MappableBool
    edgecolor: MappableColor
    edgealpha: MappableFloat
    edgewidth: MappableFloat
    edgestyle: MappableStyle
    width: MappableFloat
    baseline: MappableFloat
    def __init__(self, artist_kws, color, alpha, fill, edgecolor, edgealpha, edgewidth, edgestyle, width, baseline) -> None: ...

class Bars(BarBase):
    color: MappableColor
    alpha: MappableFloat
    fill: MappableBool
    edgecolor: MappableColor
    edgealpha: MappableFloat
    edgewidth: MappableFloat
    edgestyle: MappableStyle
    width: MappableFloat
    baseline: MappableFloat
    def __init__(self, artist_kws, color, alpha, fill, edgecolor, edgealpha, edgewidth, edgestyle, width, baseline) -> None: ...
