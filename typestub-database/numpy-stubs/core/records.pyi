from . import numerictypes as nt
from typing import Any

class format_parser:
    def __init__(self, formats, names, titles, aligned: bool = ..., byteorder: Any | None = ...) -> None: ...

class record(nt.void):
    __name__: str
    __module__: str
    def __getattribute__(self, attr): ...
    def __setattr__(self, attr, val): ...
    def __getitem__(self, indx): ...
    def pprint(self): ...

class recarray(ndarray):
    __name__: str
    __module__: str
    def __new__(subtype, shape, dtype: Any | None = ..., buf: Any | None = ..., offset: int = ..., strides: Any | None = ..., formats: Any | None = ..., names: Any | None = ..., titles: Any | None = ..., byteorder: Any | None = ..., aligned: bool = ..., order: str = ...): ...
    dtype: Any
    def __array_finalize__(self, obj) -> None: ...
    def __getattribute__(self, attr): ...
    def __setattr__(self, attr, val): ...
    def __getitem__(self, indx): ...
    def field(self, attr, val: Any | None = ...): ...

def fromarrays(arrayList, dtype: Any | None = ..., shape: Any | None = ..., formats: Any | None = ..., names: Any | None = ..., titles: Any | None = ..., aligned: bool = ..., byteorder: Any | None = ...): ...
def fromrecords(recList, dtype: Any | None = ..., shape: Any | None = ..., formats: Any | None = ..., names: Any | None = ..., titles: Any | None = ..., aligned: bool = ..., byteorder: Any | None = ...): ...
def fromstring(datastring, dtype: Any | None = ..., shape: Any | None = ..., offset: int = ..., formats: Any | None = ..., names: Any | None = ..., titles: Any | None = ..., aligned: bool = ..., byteorder: Any | None = ...): ...
def fromfile(fd, dtype: Any | None = ..., shape: Any | None = ..., offset: int = ..., formats: Any | None = ..., names: Any | None = ..., titles: Any | None = ..., aligned: bool = ..., byteorder: Any | None = ...): ...
def array(obj, dtype: Any | None = ..., shape: Any | None = ..., offset: int = ..., strides: Any | None = ..., formats: Any | None = ..., names: Any | None = ..., titles: Any | None = ..., aligned: bool = ..., byteorder: Any | None = ..., copy: bool = ...): ...
