from tensorflow.python.eager import def_function as def_function
from tensorflow.python.keras import losses as losses, optimizer_v1 as optimizer_v1, optimizers as optimizers
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.utils import generic_utils as generic_utils, version_utils as version_utils
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from tensorflow.python.util import nest as nest
from typing import Any

def extract_model_metrics(model): ...
def model_input_signature(model, keep_original_batch_size: bool = ...): ...
def raise_model_input_error(model) -> None: ...
def trace_model_call(model, input_signature: Any | None = ...): ...
def model_metadata(model, include_optimizer: bool = ..., require_config: bool = ...): ...
def should_overwrite(filepath, overwrite): ...
def compile_args_from_training_config(training_config, custom_objects: Any | None = ...): ...
def try_build_compiled_arguments(model) -> None: ...
def is_hdf5_filepath(filepath): ...
