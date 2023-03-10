import abc
from tensorflow.python.distribute import distribute_lib as distribute_lib, distribute_utils as distribute_utils
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gradients as gradients, math_ops as math_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import slot_creator as slot_creator
from tensorflow.python.training.tracking import base as trackable
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def get_filtered_grad_fn(grad_fn): ...

class _OptimizableVariable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def target(self): ...
    @abc.abstractmethod
    def update_op(self, optimizer, g): ...

class _RefVariableProcessor(_OptimizableVariable):
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g): ...

class _DenseReadResourceVariableProcessor(_OptimizableVariable):
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g): ...

class _DenseResourceVariableProcessor(_OptimizableVariable):
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g): ...

class _TensorProcessor(_OptimizableVariable):
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g) -> None: ...

class Optimizer(trackable.Trackable):
    GATE_NONE: int
    GATE_OP: int
    GATE_GRAPH: int
    def __init__(self, use_locking, name) -> None: ...
    def get_name(self): ...
    def minimize(self, loss, global_step: Any | None = ..., var_list: Any | None = ..., gate_gradients=..., aggregation_method: Any | None = ..., colocate_gradients_with_ops: bool = ..., name: Any | None = ..., grad_loss: Any | None = ...): ...
    def compute_gradients(self, loss, var_list: Any | None = ..., gate_gradients=..., aggregation_method: Any | None = ..., colocate_gradients_with_ops: bool = ..., grad_loss: Any | None = ...): ...
    def apply_gradients(self, grads_and_vars, global_step: Any | None = ..., name: Any | None = ...): ...
    def get_slot(self, var, name): ...
    def get_slot_names(self): ...
    def variables(self): ...
