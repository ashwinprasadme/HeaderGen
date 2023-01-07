from tensorflow.python.distribute import distribute_lib as distribute_lib, distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import slot_creator as slot_creator
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any

def assign_moving_average(variable, value, decay, zero_debias: bool = ..., name: Any | None = ...): ...
def weighted_moving_average(value, decay, weight, truediv: bool = ..., collections: Any | None = ..., name: Any | None = ...): ...

class ExponentialMovingAverage:
    def __init__(self, decay, num_updates: Any | None = ..., zero_debias: bool = ..., name: str = ...) -> None: ...
    @property
    def name(self): ...
    def apply(self, var_list: Any | None = ...): ...
    def average(self, var): ...
    def average_name(self, var): ...
    def variables_to_restore(self, moving_avg_variables: Any | None = ...): ...