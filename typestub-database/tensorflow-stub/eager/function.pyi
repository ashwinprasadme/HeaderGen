from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, function_pb2 as function_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.eager import backprop as backprop, backprop_util as backprop_util, context as context, execute as execute, forwardprop_util as forwardprop_util, monitoring as monitoring, tape as tape
from tensorflow.python.eager.graph_only_ops import graph_placeholder as graph_placeholder
from tensorflow.python.framework import c_api_util as c_api_util, composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, error_interpolation as error_interpolation, errors as errors, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, default_gradient as default_gradient, functional_ops as functional_ops, gradients_util as gradients_util, handle_data_util as handle_data_util, resource_variable_ops as resource_variable_ops
from tensorflow.python.profiler import trace as trace
from tensorflow.python.saved_model import save_context as save_context
from tensorflow.python.types import core as core
from tensorflow.python.util import compat as compat, function_utils as function_utils, lazy_loader as lazy_loader, memory as memory, nest as nest, object_identity as object_identity, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

ag_ctx: Any
np_arrays: Any
FORWARD_FUNCTION_ATTRIBUTE_NAME: str
BACKWARD_FUNCTION_ATTRIBUTE_NAME: str
IMPLEMENTS_ATTRIBUTE_NAME: str
SHARED_RENDEZVOUS_ATTRIBUTE_NAME: str
ENCODE_VARIABLES_BY_RESOURCE_ID: bool

class CacheKey(NamedTuple):
    input_signature: Any
    parent_graph: Any
    device_functions: Any
    colocation_stack: Any
    in_cross_replica_context: Any
    variable_policy: Any
    xla_context_id: Any

def common_shape(x, y): ...
def is_same_structure(structure1, structure2, check_values: bool = ...): ...

class _InterpolateFunctionError:
    def __init__(self, top_level_func) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, typ, exc, tb): ...

def add_function_callback(function_callback) -> None: ...
def remove_function_callback(function_callback) -> None: ...
def clear_function_callbacks() -> None: ...

class _EagerDefinedFunctionDeleter:
    name: Any
    def __init__(self, name) -> None: ...
    def __del__(self) -> None: ...

class FunctionAlreadyGarbageCollectedError(Exception):
    def __init__(self, function_name) -> None: ...

class _EagerDefinedFunction:
    definition: Any
    signature: Any
    grad_func_name: Any
    python_grad_func: Any
    graph: Any
    def __init__(self, name, graph, inputs, outputs, attrs) -> None: ...
    def add_to_graph(self, g: Any | None = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def stateful_ops(self): ...
    def call(self, ctx, args, cancellation_manager: Any | None = ...): ...

class _DelayedRewriteGradientFunctions:
    def __init__(self, func_graph, attrs, func_graph_deleter) -> None: ...
    def forward_backward(self, num_doutputs: Any | None = ...): ...
    def get_gradient_function(self): ...
    def forward(self, inference_args: Any | None = ..., input_tangents: Any | None = ...): ...
    def record(self, flat_outputs, inference_args, input_tangents) -> None: ...

class _ForwardWrapper(NamedTuple):
    graph: Any
    outputs: Any
    output_indices: Any
    output_tangents: Any

class _TapeGradientFunctions:
    def __init__(self, func_graph, attrs, func_graph_deleter, forwardprop_input_indices, delayed_rewrite_functions, need_gradients_for_jvps) -> None: ...
    def forward(self, inference_args, input_tangents): ...
    def record(self, flat_outputs, inference_args, input_tangents) -> None: ...

class _FirstOrderTapeGradientFunctions(_TapeGradientFunctions):
    def __init__(self, func_graph, attrs, func_graph_deleter, forwardprop_input_indices, delayed_rewrite_functions, need_gradients_for_jvps) -> None: ...

class _HigherOrderTapeGradientFunctions(_TapeGradientFunctions): ...

class _ForwardBackwardCall:
    def __init__(self, functions, inference_args, input_tangents, tape_watching) -> None: ...
    def forward(self): ...
    def record(self, flat_outputs) -> None: ...

class ConcreteFunction(core.ConcreteFunction):
    def __init__(self, func_graph, attrs: Any | None = ..., shared_func_graph: bool = ..., function_spec: Any | None = ...) -> None: ...
    @property
    def variables(self): ...
    @property
    def trainable_variables(self): ...
    def __call__(self, *args, **kwargs): ...
    @property
    def name(self): ...
    @property
    def graph(self): ...
    @property
    def inputs(self): ...
    @property
    def structured_input_signature(self): ...
    @property
    def outputs(self): ...
    @property
    def structured_outputs(self): ...
    def set_external_captures(self, captures) -> None: ...
    def replace_capture_with_deferred_capture(self, tensor, closure, spec, placeholder: Any | None = ..., default_value: Any | None = ...) -> None: ...
    @property
    def captured_inputs(self): ...
    @property
    def function_def(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_dtypes(self): ...
    def add_to_graph(self, g: Any | None = ...) -> None: ...
    def add_gradient_functions_to_graph(self, g: Any | None = ...) -> None: ...
    def pretty_printed_signature(self, verbose: bool = ...): ...

class FunctionSpec:
    @staticmethod
    def from_function_and_signature(python_function, input_signature, is_pure: bool = ..., experimental_follow_type_hints: bool = ..., jit_compile: Any | None = ...): ...
    def __init__(self, fullargspec, is_method, input_signature, is_pure: bool = ..., experimental_follow_type_hints: bool = ..., name: Any | None = ..., jit_compile: Any | None = ...) -> None: ...
    @property
    def fullargspec(self): ...
    @property
    def is_method(self): ...
    @property
    def args_to_indices(self): ...
    @property
    def kwargs_to_include(self): ...
    @property
    def input_signature(self): ...
    @property
    def flat_input_signature(self): ...
    @property
    def is_pure(self): ...
    @property
    def jit_compile(self): ...
    @property
    def arg_names(self): ...
    @property
    def vararg_name(self): ...
    @property
    def varkw_name(self): ...
    def signature_summary(self, default_values: bool = ...): ...
    def canonicalize_function_inputs(self, *args, **kwargs): ...

class FunctionCache:
    missed: Any
    primary: Any
    arg_relaxed_specs: Any
    arg_relaxed: Any
    def __init__(self) -> None: ...
    def all_values(self): ...

class Function:
    tracing_count: int
    def __init__(self, python_function, name, input_signature: Any | None = ..., attributes: Any | None = ..., autograph: bool = ..., autograph_options: Any | None = ..., experimental_relax_shapes: bool = ..., capture_by_value: Any | None = ..., jit_compile: Any | None = ..., experimental_follow_type_hints: bool = ...) -> None: ...
    def __call__(self, *args, **kwargs): ...
    @property
    def python_function(self): ...
    @property
    def function_spec(self): ...
    @property
    def input_signature(self): ...
    @property
    def flat_input_signature(self): ...
    def get_concrete_function(self, *args, **kwargs): ...
    def __get__(self, instance, owner): ...

def register(func, *args, **kwargs): ...
def validate_signature(signature) -> None: ...
def validate_python_function(python_function) -> None: ...
def defun(func: Any | None = ..., input_signature: Any | None = ..., autograph: bool = ..., experimental_autograph_options: Any | None = ..., experimental_relax_shapes: bool = ...): ...
def defun_with_attributes(func: Any | None = ..., input_signature: Any | None = ..., attributes: Any | None = ..., autograph: bool = ..., experimental_autograph_options: Any | None = ..., jit_compile: Any | None = ..., experimental_relax_shapes: bool = ..., experimental_follow_type_hints: bool = ...): ...

class TfMethodTarget:
    weakrefself_target__: Any
    weakrefself_func__: Any
    def __init__(self, target, original_python_function) -> None: ...
    @property
    def target(self): ...
    @property
    def target_class(self): ...
    def call(self, args, kwargs): ...

def class_method_to_instance_method(original_function, instance): ...

class _FunctionGarbageCollector:
    def __init__(self, cache) -> None: ...
    def __del__(self) -> None: ...

class ConcreteFunctionGarbageCollector:
    def __init__(self, func_graph) -> None: ...
    def release(self) -> None: ...
    def __del__(self) -> None: ...

class _Marker:
    def __init__(self, s) -> None: ...
