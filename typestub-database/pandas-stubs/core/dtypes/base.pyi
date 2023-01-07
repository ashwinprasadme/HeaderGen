from pandas._libs.hashtable import object_hash as object_hash
from pandas._typing import DtypeObj as DtypeObj, Shape as Shape, npt as npt, type_t as type_t
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.errors import AbstractMethodError as AbstractMethodError
from typing import Union, Any, TypeVar, overload

ExtensionDtypeT = TypeVar('ExtensionDtypeT', bound='ExtensionDtype')

class ExtensionDtype:
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: Any) -> bool: ...
    @property
    def na_value(self) -> object: ...
    @property
    def type(self) -> type_t[Any]: ...
    @property
    def kind(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def names(self) -> Union[list[str], None]: ...
    @classmethod
    def construct_array_type(cls) -> type_t[ExtensionArray]: ...
    def empty(self, shape: Shape) -> type_t[ExtensionArray]: ...
    @classmethod
    def construct_from_string(cls, string: str) -> ExtensionDtypeT: ...
    @classmethod
    def is_dtype(cls, dtype: object) -> bool: ...

def register_extension_dtype(cls) -> type_t[ExtensionDtypeT]: ...

class Registry:
    dtypes: Any
    def __init__(self) -> None: ...
    def register(self, dtype: type_t[ExtensionDtype]) -> None: ...
    @overload
    def find(self, dtype: type_t[ExtensionDtypeT]) -> type_t[ExtensionDtypeT]: ...
    @overload
    def find(self, dtype: ExtensionDtypeT) -> ExtensionDtypeT: ...
    @overload
    def find(self, dtype: str) -> Union[ExtensionDtype, None]: ...
    @overload
    def find(self, dtype: npt.DTypeLike) -> Union[type_t[ExtensionDtype], ExtensionDtype, None]: ...