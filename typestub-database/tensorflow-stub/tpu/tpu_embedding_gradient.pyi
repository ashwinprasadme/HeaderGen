from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops

def get_gradients_through_compute_gradients(optimizer, loss, activations): ...
def create_dummy_table_variables(tpu_embedding): ...
def hook_dummy_table_variables_to_activations(tpu_embedding, activations, dummy_table_variables): ...
def get_gradients_through_dummy_table_variables(tpu_embedding): ...
