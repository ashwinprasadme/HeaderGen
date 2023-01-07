from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.keras.engine import base_layer as base_layer
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, string_ops as string_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class Hashing(base_layer.Layer):
    num_bins: Any
    mask_value: Any
    strong_hash: Any
    salt: Any
    def __init__(self, num_bins, mask_value: Any | None = ..., salt: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_config(self): ...