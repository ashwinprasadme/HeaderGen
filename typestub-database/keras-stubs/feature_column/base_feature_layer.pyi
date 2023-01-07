from keras.engine.base_layer import Layer as Layer
from keras.utils import generic_utils as generic_utils
from typing import Any

class _BaseFeaturesLayer(Layer):
    def __init__(self, feature_columns, expected_column_type, trainable, name, partitioner: Any | None = ..., **kwargs) -> None: ...
    def build(self, _) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...