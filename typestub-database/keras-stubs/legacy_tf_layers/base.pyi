from keras import backend as backend
from keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils
from keras.legacy_tf_layers import variable_scope_shim as variable_scope_shim
from keras.mixed_precision import policy as policy
from keras.utils import tf_contextlib as tf_contextlib
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
