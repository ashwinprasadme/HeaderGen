from tensorflow.python.framework import tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util import nest as nest

def slice_arrays(arrays, indices, contiguous: bool = ...): ...
def handle_partial_sample_weights(outputs, sample_weights, sample_weight_modes, check_all_flat: bool = ...): ...

class RespectCompiledTrainableState:
    def __init__(self, model) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_arg, value_arg, traceback_arg): ...

def get_input_shape_and_dtype(layer): ...
def get_static_batch_size(layer): ...
def list_to_tuple(maybe_list): ...
