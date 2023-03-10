import numpy as np
from collections.abc import Callable as Callable
from pandas import Series as Series
from pandas._libs import lib as lib
from pandas._typing import Dtype as Dtype, NpDtype as NpDtype, PositionalIndexer as PositionalIndexer, Scalar as Scalar, ScalarIndexer as ScalarIndexer, SequenceIndexer as SequenceIndexer, TakeIndexer as TakeIndexer, npt as npt
from pandas.compat import pa_version_under1p01 as pa_version_under1p01, pa_version_under2p0 as pa_version_under2p0, pa_version_under3p0 as pa_version_under3p0, pa_version_under4p0 as pa_version_under4p0
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.arrays.boolean import BooleanDtype as BooleanDtype
from pandas.core.arrays.integer import Int64Dtype as Int64Dtype
from pandas.core.arrays.numeric import NumericDtype as NumericDtype
from pandas.core.arrays.string_ import BaseStringArray as BaseStringArray, StringDtype as StringDtype
from pandas.core.dtypes.common import is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_dtype_equal as is_dtype_equal, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexers import check_array_indexer as check_array_indexer, unpack_tuple_and_ellipses as unpack_tuple_and_ellipses, validate_indices as validate_indices
from pandas.core.strings.object_array import ObjectStringArrayMixin as ObjectStringArrayMixin
from pandas.util._decorators import doc as doc
from typing import Union, Any, overload

ARROW_CMP_FUNCS: Any
ArrowStringScalarOrNAT: Any

class ArrowStringArray(OpsMixin, BaseStringArray, ObjectStringArrayMixin):
    def __init__(self, values) -> None: ...
    @property
    def dtype(self) -> StringDtype: ...
    def __array__(self, dtype: Union[NpDtype, None] = ...) -> np.ndarray: ...
    def __arrow_array__(self, type: Any | None = ...): ...
    def to_numpy(self, dtype: Union[npt.DTypeLike, None] = ..., copy: bool = ..., na_value=...) -> np.ndarray: ...
    def __len__(self) -> int: ...
    def factorize(self, na_sentinel: int = ...) -> tuple[np.ndarray, ExtensionArray]: ...
    @overload
    def __getitem__(self, item: ScalarIndexer) -> ArrowStringScalarOrNAT: ...
    @overload
    def __getitem__(self, item: SequenceIndexer) -> ArrowStringArray: ...
    @property
    def nbytes(self) -> int: ...
    def isna(self) -> np.ndarray: ...
    def copy(self) -> ArrowStringArray: ...
    def insert(self, loc: int, item): ...
    def __setitem__(self, key: Union[int, slice, np.ndarray], value: Any) -> None: ...
    def take(self, indices: TakeIndexer, allow_fill: bool = ..., fill_value: Any = ...): ...
    def isin(self, values): ...
    def value_counts(self, dropna: bool = ...) -> Series: ...
    def astype(self, dtype, copy: bool = ...): ...
