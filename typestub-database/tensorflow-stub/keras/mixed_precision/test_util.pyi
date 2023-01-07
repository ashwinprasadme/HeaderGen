from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras import regularizers as regularizers
from tensorflow.python.keras.engine import base_layer as base_layer
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, custom_gradient as custom_gradient, math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any

def create_identity_with_grad_check_fn(expected_gradient, expected_dtype: Any | None = ...): ...
def create_identity_with_nan_gradients_fn(have_nan_gradients): ...

class AssertTypeLayer(base_layer.Layer):
    def __init__(self, assert_type: Any | None = ..., **kwargs) -> None: ...
    def assert_input_types(self, inputs) -> None: ...

class MultiplyLayer(AssertTypeLayer):
    def __init__(self, regularizer: Any | None = ..., activity_regularizer: Any | None = ..., use_operator: bool = ..., var_name: str = ..., **kwargs) -> None: ...
    v: Any
    built: bool
    def build(self, _) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class MultiplyLayerWithoutAutoCast(MultiplyLayer):
    v: Any
    built: bool
    def build(self, _) -> None: ...
    def call(self, inputs): ...

class IdentityRegularizer(regularizers.Regularizer):
    def __call__(self, x): ...
    def get_config(self): ...

class ReduceSumRegularizer(regularizers.Regularizer):
    def __call__(self, x): ...
    def get_config(self): ...