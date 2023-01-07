import threading
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils
from keras.utils import control_flow_util as control_flow_util, tf_contextlib as tf_contextlib, tf_inspect as tf_inspect
from keras.utils.generic_utils import LazyLoader as LazyLoader
from typing import Any

training_lib: Any

def use_wrapped_call(layer, call_fn, default_training_value: Any | None = ..., return_method: bool = ...): ...
def layer_uses_training_bool(layer): ...
def list_all_layers(obj): ...
def list_all_layers_and_sublayers(obj): ...
def maybe_add_training_arg(original_call, wrapped_call, expects_training_arg, default_training_value): ...
def get_training_arg_index(call_fn): ...
def call_is_method(call_fn): ...
def set_training_arg(training, index, args, kwargs): ...
def get_training_arg(index, args, kwargs): ...
def remove_training_arg(index, args, kwargs) -> None: ...

class SaveOptionsContext(threading.local):
    save_traces: bool
    def __init__(self) -> None: ...

def keras_option_scope(save_traces) -> None: ...
def should_save_traces(): ...
def no_automatic_dependency_tracking_scope(obj) -> None: ...