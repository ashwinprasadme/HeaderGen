from tensorflow.python.ops import control_flow_ops as control_flow_ops, variables as variables
from typing import Any

def convert_data_format(data_format, ndim): ...
def normalize_tuple(value, n, name): ...
def normalize_data_format(value): ...
def normalize_padding(value): ...
def conv_output_length(input_length, filter_size, padding, stride, dilation: int = ...): ...
def conv_input_length(output_length, filter_size, padding, stride): ...
def deconv_output_length(input_length, filter_size, padding, stride): ...
def smart_cond(pred, true_fn: Any | None = ..., false_fn: Any | None = ..., name: Any | None = ...): ...
def constant_value(pred): ...