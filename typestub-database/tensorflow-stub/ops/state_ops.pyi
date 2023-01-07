from tensorflow.python.ops.gen_state_ops import *
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_math_ops as gen_math_ops, gen_resource_variable_ops as gen_resource_variable_ops, gen_state_ops as gen_state_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def variable_op(shape, dtype, name: str = ..., set_shape: bool = ..., container: str = ..., shared_name: str = ...): ...
def variable_op_v2(shape, dtype, name: str = ..., container: str = ..., shared_name: str = ...): ...
def init_variable(v, init, name: str = ...): ...
def is_variable_initialized(ref, name: Any | None = ...): ...
def assign_sub(ref, value, use_locking: Any | None = ..., name: Any | None = ...): ...
def assign_add(ref, value, use_locking: Any | None = ..., name: Any | None = ...): ...
def assign(ref, value, validate_shape: Any | None = ..., use_locking: Any | None = ..., name: Any | None = ...): ...
def count_up_to(ref, limit, name: Any | None = ...): ...
def scatter_update(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_nd_update(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_add(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_nd_add(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_sub(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_nd_sub(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_mul(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_div(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_max(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def scatter_min(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...
def batch_scatter_update(ref, indices, updates, use_locking: bool = ..., name: Any | None = ...): ...