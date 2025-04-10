from dataclasses import (
    dataclass,
)  ## dataclass is a Python decorator that automatically generates special methods for classes


@dataclass
class TextFile:
    filename: str
    content: str
    suffix: str
    source: str
    size: int
    date: str
