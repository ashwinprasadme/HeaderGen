import numpy as np
from pandas import Categorical as Categorical, DataFrame as DataFrame, Index as Index, MultiIndex as MultiIndex, Series as Series
from pandas._libs import lib as lib
from pandas._libs.hashing import hash_object_array as hash_object_array
from pandas._typing import ArrayLike as ArrayLike
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries
from typing import Union, Hashable, Iterable, Iterator

def combine_hash_arrays(arrays: Iterator[np.ndarray], num_items: int) -> np.ndarray: ...
def hash_pandas_object(obj: Union[Index, DataFrame, Series], index: bool = ..., encoding: str = ..., hash_key: Union[str, None] = ..., categorize: bool = ...) -> Series: ...
def hash_tuples(vals: Union[MultiIndex, Iterable[tuple[Hashable, ...]]], encoding: str = ..., hash_key: str = ...) -> np.ndarray: ...
def hash_array(vals: ArrayLike, encoding: str = ..., hash_key: str = ..., categorize: bool = ...) -> np.ndarray: ...
