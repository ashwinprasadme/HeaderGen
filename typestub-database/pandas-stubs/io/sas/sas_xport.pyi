from collections import abc
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.io.common import get_handle as get_handle
from pandas.io.sas.sasreader import ReaderBase as ReaderBase
from pandas.util._decorators import Appender as Appender
from typing import Union, Any

class XportReader(ReaderBase, abc.Iterator):
    __doc__: Any
    handles: Any
    filepath_or_buffer: Any
    def __init__(self, filepath_or_buffer: Union[FilePath, ReadBuffer[bytes]], index: Any | None = ..., encoding: Union[str, None] = ..., chunksize: Any | None = ...) -> None: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def get_chunk(self, size: Any | None = ...): ...
    def read(self, nrows: Any | None = ...): ...