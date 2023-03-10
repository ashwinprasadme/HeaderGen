from tensorflow.python.data.experimental.ops import cardinality as cardinality
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.keras.engine import keras_tensor as keras_tensor
from tensorflow.python.keras.utils import object_identity as object_identity, tf_contextlib as tf_contextlib
from tensorflow.python.ops import math_ops as math_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor, ragged_tensor_value as ragged_tensor_value
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def is_tensor_or_tensor_list(v): ...
def get_reachable_from_inputs(inputs, targets: Any | None = ...): ...
def map_structure_with_atomic(is_atomic_fn, map_fn, nested): ...
def get_shapes(tensors): ...
def convert_shapes(input_shape, to_tuples: bool = ...): ...

class ListWrapper:
    def __init__(self, list_to_wrap) -> None: ...
    def as_list(self): ...

def convert_inner_node_data(nested, wrap: bool = ...): ...
def shape_type_conversion(fn): ...
def are_all_symbolic_tensors(tensors): ...
def is_extension_type(tensor): ...
def is_symbolic_tensor(tensor): ...
def register_symbolic_tensor_type(cls) -> None: ...
def type_spec_from_value(value): ...
def is_ragged(tensor): ...
def is_sparse(tensor): ...
def is_tensor_or_variable(x): ...
def assert_no_legacy_layers(layers) -> None: ...
def maybe_init_scope(layer) -> None: ...
def graph_context_for_symbolic_tensors(*args, **kwargs) -> None: ...
def dataset_is_infinite(dataset): ...
def get_tensor_spec(t, dynamic_batch: bool = ..., name: Any | None = ...): ...
def sync_to_numpy_or_python_type(tensors): ...
