from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, function as function, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_functional_ops as gen_functional_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.gen_functional_ops import remote_call as remote_call, symbolic_gradient as symbolic_gradient
from tensorflow.python.util import compat as compat, deprecation as deprecation, dispatch as dispatch, function_utils as function_utils, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def foldl(fn, elems, initializer: Any | None = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Any | None = ...): ...
def foldl_v2(fn, elems, initializer: Any | None = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Any | None = ...): ...
def foldr(fn, elems, initializer: Any | None = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Any | None = ...): ...
def foldr_v2(fn, elems, initializer: Any | None = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Any | None = ...): ...
def scan(fn, elems, initializer: Any | None = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., reverse: bool = ..., name: Any | None = ...): ...
def scan_v2(fn, elems, initializer: Any | None = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., reverse: bool = ..., name: Any | None = ...): ...
def If(cond, inputs, then_branch, else_branch, name: Any | None = ...): ...
def Gradient(inputs, f, name: Any | None = ...): ...
def While(input_, cond, body, name: Any | None = ..., hostmem: Any | None = ...): ...
def For(start, limit, delta, inputs, body, name: Any | None = ..., hostmem: Any | None = ..., rewrite_with_while: Any | None = ...): ...
def partitioned_call(args, f, tout: Any | None = ..., executing_eagerly: Any | None = ..., config: Any | None = ..., executor_type: Any | None = ...): ...