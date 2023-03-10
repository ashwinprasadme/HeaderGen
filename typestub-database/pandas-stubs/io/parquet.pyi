from pandas import DataFrame as DataFrame, MultiIndex as MultiIndex, get_option as get_option
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import IOHandles as IOHandles, get_handle as get_handle, is_fsspec_url as is_fsspec_url, is_url as is_url, stringify_path as stringify_path
from pandas.util._decorators import doc as doc
from pandas.util.version import Version as Version
from typing import Union, Any

def get_engine(engine: str) -> BaseImpl: ...

class BaseImpl:
    @staticmethod
    def validate_dataframe(df: DataFrame) -> None: ...
    def write(self, df: DataFrame, path, compression, **kwargs): ...
    def read(self, path, columns: Any | None = ..., **kwargs) -> DataFrame: ...

class PyArrowImpl(BaseImpl):
    api: Any
    def __init__(self) -> None: ...
    def write(self, df: DataFrame, path: Union[FilePath, WriteBuffer[bytes]], compression: Union[str, None] = ..., index: Union[bool, None] = ..., storage_options: StorageOptions = ..., partition_cols: Union[list[str], None] = ..., **kwargs) -> None: ...
    def read(self, path, columns: Any | None = ..., use_nullable_dtypes: bool = ..., storage_options: StorageOptions = ..., **kwargs) -> DataFrame: ...

class FastParquetImpl(BaseImpl):
    api: Any
    def __init__(self) -> None: ...
    def write(self, df: DataFrame, path, compression: str = ..., index: Any | None = ..., partition_cols: Any | None = ..., storage_options: StorageOptions = ..., **kwargs) -> None: ...
    def read(self, path, columns: Any | None = ..., storage_options: StorageOptions = ..., **kwargs) -> DataFrame: ...

def to_parquet(df: DataFrame, path: Union[FilePath, WriteBuffer[bytes], None] = ..., engine: str = ..., compression: Union[str, None] = ..., index: Union[bool, None] = ..., storage_options: StorageOptions = ..., partition_cols: Union[list[str], None] = ..., **kwargs) -> Union[bytes, None]: ...
def read_parquet(path, engine: str = ..., columns: Any | None = ..., storage_options: StorageOptions = ..., use_nullable_dtypes: bool = ..., **kwargs) -> DataFrame: ...
