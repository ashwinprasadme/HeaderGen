from abc import ABCMeta, abstractmethod
from pandas import DataFrame as DataFrame
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.io.common import stringify_path as stringify_path
from typing import Union, Any, Hashable, overload

class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def read(self, nrows: Any | None = ...): ...
    @abstractmethod
    def close(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...


@overload
def read_sas(filepath_or_buffer: Union[FilePath, ReadBuffer[bytes]], format: Union[str, None] = ..., index: Union[Hashable, None] = ..., encoding: Union[str, None] = ..., chunksize: int = ..., iterator: bool = ...) -> ReaderBase: ...
@overload
def read_sas(filepath_or_buffer: Union[FilePath, ReadBuffer[bytes]], format: Union[str, None] = ..., index: Union[Hashable, None] = ..., encoding: Union[str, None] = ..., chunksize: None = ..., iterator: bool = ...) -> Union[DataFrame, ReaderBase]: ...
