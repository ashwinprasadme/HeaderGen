from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, types_pb2 as types_pb2
from tensorflow.python.eager import context as context, execute as execute
from tensorflow.python.framework import dtypes as dtypes, op_callbacks as op_callbacks, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.profiler import trace as trace
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def convert_to_eager_tensor(value, ctx, dtype: Any | None = ...): ...
def constant_v1(value, dtype: Any | None = ..., shape: Any | None = ..., name: str = ..., verify_shape: bool = ...): ...
def constant(value, dtype: Any | None = ..., shape: Any | None = ..., name: str = ...): ...
def is_constant(tensor_or_op): ...
