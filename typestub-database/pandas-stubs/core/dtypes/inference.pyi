from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike
from typing import Union, Any

is_bool: Any
is_integer: Any
is_float: Any
is_complex: Any
is_scalar: Any
is_decimal: Any
is_interval: Any
is_list_like: Any
is_iterator: Any

def is_number(obj) -> bool: ...
def iterable_not_string(obj) -> bool: ...
def is_file_like(obj) -> bool: ...
def is_re(obj) -> bool: ...
def is_re_compilable(obj) -> bool: ...
def is_array_like(obj) -> bool: ...
def is_nested_list_like(obj) -> bool: ...
def is_dict_like(obj) -> bool: ...
def is_named_tuple(obj) -> bool: ...
def is_hashable(obj) -> bool: ...
def is_sequence(obj) -> bool: ...
def is_dataclass(item): ...
def is_inferred_bool_dtype(arr: ArrayLike) -> bool: ...