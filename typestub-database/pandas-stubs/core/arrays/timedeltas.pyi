import numpy as np
from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib, tslibs as tslibs
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, NaTType as NaTType, Period as Period, Tick as Tick, Timedelta as Timedelta, Timestamp as Timestamp, iNaT as iNaT, to_offset as to_offset
from pandas._libs.tslibs.conversion import ensure_timedelta64ns as ensure_timedelta64ns, precision_from_unit as precision_from_unit
from pandas._libs.tslibs.fields import get_timedelta_field as get_timedelta_field
from pandas._libs.tslibs.timedeltas import array_to_timedelta64 as array_to_timedelta64, ints_to_pytimedelta as ints_to_pytimedelta, parse_timedelta_unit as parse_timedelta_unit
from pandas._typing import DtypeObj as DtypeObj, NpDtype as NpDtype
from pandas.core import nanops as nanops
from pandas.core.algorithms import checked_add_with_arr as checked_add_with_arr
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, IntegerArray as IntegerArray, PeriodArray as PeriodArray, datetimelike as dtl
from pandas.core.arrays._ranges import generate_regular_range as generate_regular_range
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.cast import astype_td64_unit_conversion as astype_td64_unit_conversion
from pandas.core.dtypes.common import DT64NS_DTYPE as DT64NS_DTYPE, TD64NS_DTYPE as TD64NS_DTYPE, is_dtype_equal as is_dtype_equal, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype
from pandas.core.dtypes.generic import ABCCategorical as ABCCategorical, ABCMultiIndex as ABCMultiIndex
from pandas.core.dtypes.missing import isna as isna
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.util._validators import validate_endpoints as validate_endpoints
from typing import Union, Any

class TimedeltaArray(dtl.TimelikeOps):
    __array_priority__: int
    @property
    def dtype(self) -> np.dtype: ...
    def __init__(self, values, dtype=..., freq=..., copy: bool = ...) -> None: ...
    def astype(self, dtype, copy: bool = ...): ...
    def __iter__(self): ...
    def sum(self, *, axis: Union[int, None] = ..., dtype: Union[NpDtype, None] = ..., out: Any | None = ..., keepdims: bool = ..., initial: Any | None = ..., skipna: bool = ..., min_count: int = ...): ...
    def std(self, *, axis: Union[int, None] = ..., dtype: Union[NpDtype, None] = ..., out: Any | None = ..., ddof: int = ..., keepdims: bool = ..., skipna: bool = ...): ...
    def __mul__(self, other) -> TimedeltaArray: ...
    __rmul__: Any
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __neg__(self) -> TimedeltaArray: ...
    def __pos__(self) -> TimedeltaArray: ...
    def __abs__(self) -> TimedeltaArray: ...
    def total_seconds(self) -> np.ndarray: ...
    def to_pytimedelta(self) -> np.ndarray: ...
    days: Any
    seconds: Any
    microseconds: Any
    nanoseconds: Any
    @property
    def components(self) -> DataFrame: ...

def sequence_to_td64ns(data, copy: bool = ..., unit: Any | None = ..., errors: str = ...) -> tuple[np.ndarray, Union[Tick, None]]: ...
def ints_to_td64ns(data, unit: str = ...): ...
def objects_to_td64ns(data, unit: Any | None = ..., errors: str = ...): ...