from tensorflow.python.autograph.utils import py_func as py_func, tensors as tensors
from tensorflow.python.data.experimental.ops import cardinality as cardinality
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_parsing_ops as gen_parsing_ops, gen_string_ops as gen_string_ops, list_ops as list_ops, math_ops as math_ops, sort_ops as sort_ops
from tensorflow.python.util import lazy_loader as lazy_loader, nest as nest
from typing import Any

input_lib: Any
parallel_ops: Any
UNSPECIFIED: Any

def overload_of(f): ...
def locals_in_original_context(caller_fn_scope): ...
def globals_in_original_context(caller_fn_scope): ...
def eval_in_original_context(f, args, caller_fn_scope): ...
def super_in_original_context(f, args, caller_fn_scope): ...
def abs_(x): ...
def float_(x: int = ...): ...
def int_(x: int = ..., base=...): ...
def len_(s): ...
def print_(*objects, **kwargs): ...
def range_(start_or_stop, stop=..., step=...): ...
def enumerate_(s, start: int = ...): ...
def zip_(*iterables): ...
def map_(fn, *iterables): ...
def next_(iterator, default=...): ...
def next_tf_iterator(iterator, default=...): ...
def next_py(iterator, default=...): ...
def filter_(function, iterable): ...
def any_(iterable): ...
def all_(iterable): ...
def sorted_(iterable, key=..., reverse=...): ...

SUPPORTED_BUILTINS: Any
BUILTIN_FUNCTIONS_MAP: Any
