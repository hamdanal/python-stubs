from typing import ClassVar, Literal

import netaddr

class mac_unix_common(netaddr.mac_eui48):
    word_sep: ClassVar[str]
    word_fmt: ClassVar[str]

class mac_eui64:
    word_size: Literal[8]
    num_words: int
    max_word: int
    word_sep: Literal[":"]
    word_fmt: Literal["%.2x"]
    word_base: Literal[16]
