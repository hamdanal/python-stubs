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

class Text(Mark):
    text: MappableString
    color: MappableColor
    alpha: MappableFloat
    fontsize: MappableFloat
    halign: MappableString
    valign: MappableString
    offset: MappableFloat
    def __init__(self, artist_kws, text, color, alpha, fontsize, halign, valign, offset) -> None: ...
