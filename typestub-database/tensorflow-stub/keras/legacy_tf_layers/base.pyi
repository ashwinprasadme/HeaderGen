from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils
from tensorflow.python.keras.legacy_tf_layers import variable_scope_shim as variable_scope_shim
from tensorflow.python.keras.mixed_precision import policy as policy
from tensorflow.python.keras.utils import tf_contextlib as tf_contextlib
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export, tf_export as tf_export
from typing import Any

InputSpec: Any

def keras_style_scope() -> None: ...
def set_keras_style() -> None: ...

class Layer(base_layer.Layer):
    built: bool
    def __init__(self, trainable: bool = ..., name: Any | None = ..., dtype: Any | None = ..., **kwargs) -> None: ...
    @property
    def graph(self) -> None: ...
    @property
    def scope_name(self): ...
    def add_loss(self, losses, inputs: Any | None = ...) -> None: ...
    def add_weight(self, name, shape, dtype: Any | None = ..., initializer: Any | None = ..., regularizer: Any | None = ..., trainable: Any | None = ..., constraint: Any | None = ..., use_resource: Any | None = ..., synchronization=..., aggregation=..., partitioner: Any | None = ..., **kwargs): ...
    def __call__(self, inputs, *args, **kwargs): ...
    def __deepcopy__(self, memo): ...
    def __setattr__(self, value, name) -> None: ...
