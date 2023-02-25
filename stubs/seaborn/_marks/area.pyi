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

class AreaBase: ...

class Area(AreaBase, Mark):
    color: MappableColor
    alpha: MappableFloat
    fill: MappableBool
    edgecolor: MappableColor
    edgealpha: MappableFloat
    edgewidth: MappableFloat
    edgestyle: MappableStyle
    baseline: MappableFloat
    def __init__(self, artist_kws, color, alpha, fill, edgecolor, edgealpha, edgewidth, edgestyle, baseline) -> None: ...

class Band(AreaBase, Mark):
    color: MappableColor
    alpha: MappableFloat
    fill: MappableBool
    edgecolor: MappableColor
    edgealpha: MappableFloat
    edgewidth: MappableFloat
    edgestyle: MappableFloat
    def __init__(self, artist_kws, color, alpha, fill, edgecolor, edgealpha, edgewidth, edgestyle) -> None: ...
