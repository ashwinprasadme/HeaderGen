import pyarrow
from pandas.core.arrays.interval import VALID_CLOSED as VALID_CLOSED

def pyarrow_array_to_numpy_and_mask(arr, dtype): ...

class ArrowPeriodType(pyarrow.ExtensionType):
    def __init__(self, freq) -> None: ...
    @property
    def freq(self): ...
    def __arrow_ext_serialize__(self): ...
    @classmethod
    def __arrow_ext_deserialize__(cls, storage_type, serialized): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def to_pandas_dtype(self): ...

class ArrowIntervalType(pyarrow.ExtensionType):
    def __init__(self, subtype, closed) -> None: ...
    @property
    def subtype(self): ...
    @property
    def closed(self): ...
    def __arrow_ext_serialize__(self): ...
    @classmethod
    def __arrow_ext_deserialize__(cls, storage_type, serialized): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def to_pandas_dtype(self): ...
