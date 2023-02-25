from matplotlib.artist import Artist as Artist
from seaborn._core.scales import Scale as Scale
from seaborn._marks.base import (
    Mappable as Mappable,
    MappableBool as MappableBool,
    MappableColor as MappableColor,
    MappableFloat as MappableFloat,
    MappableString as MappableString,
    MappableStyle as MappableStyle,
    Mark as Mark,
    document_properties as document_properties,
    resolve_color as resolve_color,
    resolve_properties as resolve_properties,
)

class DotBase(Mark): ...

class Dot(DotBase):
    marker: MappableString
    pointsize: MappableFloat
    stroke: MappableFloat
    color: MappableColor
    alpha: MappableFloat
    fill: MappableBool
    edgecolor: MappableColor
    edgealpha: MappableFloat
    edgewidth: MappableFloat
    edgestyle: MappableStyle
    def __init__(
        self, artist_kws, marker, pointsize, stroke, color, alpha, fill, edgecolor, edgealpha, edgewidth, edgestyle
    ) -> None: ...

class Dots(DotBase):
    marker: MappableString
    pointsize: MappableFloat
    stroke: MappableFloat
    color: MappableColor
    alpha: MappableFloat
    fill: MappableBool
    fillcolor: MappableColor
    fillalpha: MappableFloat
    def __init__(self, artist_kws, marker, pointsize, stroke, color, alpha, fill, fillcolor, fillalpha) -> None: ...
