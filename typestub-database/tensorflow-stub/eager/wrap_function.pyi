from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2, struct_pb2 as struct_pb2
from tensorflow.python.eager import context as context, function as function, lift_to_graph as lift_to_graph
from tensorflow.python.framework import composite_tensor as composite_tensor, func_graph as func_graph, importer as importer, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops, variable_scope as variable_scope
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.training.tracking import data_structures as data_structures
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class VariableHolder:
    def __init__(self, fn: Any | None = ..., share_variables: bool = ...) -> None: ...
    @property
    def variables(self): ...
    def variable_creator_scope(self, next_creator, **kwargs): ...
    def __call__(self, *args, **kwargs): ...
    def call_with_variable_creator_scope(self, fn): ...

class WrappedFunction(function.ConcreteFunction):
    def __init__(self, fn_graph, variable_holder, attrs: Any | None = ..., signature: Any | None = ...) -> None: ...
    def prune(self, feeds, fetches, name: Any | None = ..., input_signature: Any | None = ...): ...

class WrappedGraph:
    graph: Any
    def __init__(self, variable_holder: Any | None = ..., **kwargs) -> None: ...
    @property
    def functions(self): ...
    @property
    def variables(self): ...
    def wrap_function(self, fn, signature, name: Any | None = ...): ...

def wrap_function(fn, signature, name: Any | None = ...): ...
def function_from_graph_def(graph_def, inputs, outputs, captures: Any | None = ...): ...