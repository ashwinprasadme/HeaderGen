import numpy as np
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike
from pandas.core.dtypes.common import is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.base import Index as Index
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any

def is_valid_positional_slice(slc: slice) -> bool: ...
def is_list_like_indexer(key) -> bool: ...
def is_scalar_indexer(indexer, ndim: int) -> bool: ...
def is_empty_indexer(indexer, arr_value: ArrayLike) -> bool: ...
def check_setitem_lengths(indexer, value, values) -> bool: ...
def validate_indices(indices: np.ndarray, n: int) -> None: ...
def maybe_convert_indices(indices, n: int, verify: bool = ...): ...
def is_exact_shape_match(target: ArrayLike, value: ArrayLike) -> bool: ...
def length_of_indexer(indexer, target: Any | None = ...) -> int: ...
def deprecate_ndim_indexing(result, stacklevel: int = ...) -> None: ...
def unpack_1tuple(tup): ...
def check_key_length(columns: Index, key, value: DataFrame) -> None: ...
def unpack_tuple_and_ellipses(item: tuple): ...
def check_array_indexer(array: AnyArrayLike, indexer: Any) -> Any: ...