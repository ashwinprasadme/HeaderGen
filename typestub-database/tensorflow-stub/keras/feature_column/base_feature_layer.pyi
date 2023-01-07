from tensorflow.python.feature_column import feature_column_v2 as feature_column_v2
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.ops import array_ops as array_ops, variable_scope as variable_scope
from typing import Any

class _BaseFeaturesLayer(Layer):
    def __init__(self, feature_columns, expected_column_type, trainable, name, partitioner: Any | None = ..., **kwargs) -> None: ...
    def build(self, _) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...