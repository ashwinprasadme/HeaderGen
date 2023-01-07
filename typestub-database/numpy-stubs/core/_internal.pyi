import ctypes as ct
from numpy import ndarray as ndarray
from typing import Any, Type, overload

class _ctypes:
    @overload
    def __new__(cls, array: ndarray[Any, Any], ptr: None = ...) -> _ctypes[None]: ...
    @overload
    def __new__(cls, array: ndarray[Any, Any], ptr: _PT) -> _ctypes[_PT]: ...
    @property
    def data(self) -> _PT: ...
    @property
    def shape(self) -> ct.Array[ct.c_int64]: ...
    @property
    def strides(self) -> ct.Array[ct.c_int64]: ...
    def data_as(self, obj: Type[_CastT]) -> _CastT: ...
    def shape_as(self, obj: Type[_CT]) -> ct.Array[_CT]: ...
    def strides_as(self, obj: Type[_CT]) -> ct.Array[_CT]: ...