from seaborn._marks.base import (
    Mappable as Mappable,
    MappableColor as MappableColor,
    MappableFloat as MappableFloat,
    MappableString as MappableString,
    Mark as Mark,
    document_properties as document_properties,
    resolve_color as resolve_color,
    resolve_properties as resolve_properties,
)
from seaborn.external.version import Version as Version

class Path(Mark):
    color: MappableColor
    alpha: MappableFloat
    linewidth: MappableFloat
    linestyle: MappableString
    marker: MappableString
    pointsize: MappableFloat
    fillcolor: MappableColor
    edgecolor: MappableColor
    edgewidth: MappableFloat
    def __init__(
        self, artist_kws, color, alpha, linewidth, linestyle, marker, pointsize, fillcolor, edgecolor, edgewidth
    ) -> None: ...

class Line(Path):
    def __init__(
        self, artist_kws, color, alpha, linewidth, linestyle, marker, pointsize, fillcolor, edgecolor, edgewidth
    ) -> None: ...

class Paths(Mark):
    color: MappableColor
    alpha: MappableFloat
    linewidth: MappableFloat
    linestyle: MappableString
    def __post_init__(self) -> None: ...
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle) -> None: ...

class Lines(Paths):
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle) -> None: ...

class Range(Paths):
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle) -> None: ...

class Dash(Paths):
    width: MappableFloat
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle, width) -> None: ...
