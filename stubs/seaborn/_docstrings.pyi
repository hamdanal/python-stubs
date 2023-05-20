from re import Pattern
from typing_extensions import Self

from .external.docscrape import NumpyDocString as NumpyDocString

class DocstringComponents:
    regexp: Pattern[str]
    entries: dict[str, str]
    def __init__(self, comp_dict: dict[str, str], strip_whitespace: bool = True) -> None: ...
    def __getattr__(self, attr: str) -> str | None: ...
    @classmethod
    def from_nested_components(cls, **kwargs: str) -> Self: ...
    @classmethod
    def from_function_params(cls, func: object) -> Self: ...
