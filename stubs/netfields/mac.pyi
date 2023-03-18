from typing import ClassVar, Literal

import netaddr

class mac_unix_common(netaddr.mac_eui48):
    word_sep: ClassVar[str]
    word_fmt: ClassVar[str]

class mac_eui64:
    word_size: ClassVar[Literal[8]]
    num_words: ClassVar[int]
    max_word: ClassVar[int]
    word_sep: ClassVar[Literal[":"]]
    word_fmt: ClassVar[Literal["%.2x"]]
    word_base: ClassVar[Literal[16]]
