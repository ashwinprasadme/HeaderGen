from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, sets as sets
from tensorflow.python.util.tf_export import tf_export as tf_export

def assert_broadcastable(weights, values): ...
def broadcast_weights(weights, values): ...
