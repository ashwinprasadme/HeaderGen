from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, control_flow_util_v2 as control_flow_util_v2, math_ops as math_ops, rnn_cell_impl as rnn_cell_impl, tensor_array_ops as tensor_array_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def bidirectional_dynamic_rnn(cell_fw, cell_bw, inputs, sequence_length: Any | None = ..., initial_state_fw: Any | None = ..., initial_state_bw: Any | None = ..., dtype: Any | None = ..., parallel_iterations: Any | None = ..., swap_memory: bool = ..., time_major: bool = ..., scope: Any | None = ...): ...
def dynamic_rnn(cell, inputs, sequence_length: Any | None = ..., initial_state: Any | None = ..., dtype: Any | None = ..., parallel_iterations: Any | None = ..., swap_memory: bool = ..., time_major: bool = ..., scope: Any | None = ...): ...
def raw_rnn(cell, loop_fn, parallel_iterations: Any | None = ..., swap_memory: bool = ..., scope: Any | None = ...): ...
def static_rnn(cell, inputs, initial_state: Any | None = ..., dtype: Any | None = ..., sequence_length: Any | None = ..., scope: Any | None = ...): ...
def static_state_saving_rnn(cell, inputs, state_saver, state_name, sequence_length: Any | None = ..., scope: Any | None = ...): ...
def static_bidirectional_rnn(cell_fw, cell_bw, inputs, initial_state_fw: Any | None = ..., initial_state_bw: Any | None = ..., dtype: Any | None = ..., sequence_length: Any | None = ..., scope: Any | None = ...): ...
