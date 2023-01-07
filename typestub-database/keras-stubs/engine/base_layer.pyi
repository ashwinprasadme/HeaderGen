import tensorflow.compat.v2 as tf
from keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine import base_layer_utils as base_layer_utils, input_spec as input_spec, keras_tensor as keras_tensor
from keras.mixed_precision import autocast_variable as autocast_variable, loss_scale_optimizer as loss_scale_optimizer, policy as policy
from keras.saving.saved_model import layer_serialization as layer_serialization
from keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, object_identity as object_identity, tf_inspect as tf_inspect, tf_utils as tf_utils, traceback_utils as traceback_utils, version_utils as version_utils
from keras.utils.generic_utils import to_snake_case as to_snake_case
from keras.utils.tf_utils import is_tensor_or_tensor_list as is_tensor_or_tensor_list
from typing import Any

metrics_mod: Any
keras_layers_gauge: Any
keras_models_gauge: Any
keras_api_gauge: Any
keras_premade_model_gauge: Any

class Layer(tf.Module, version_utils.LayerVersionSelector):
    built: bool
    def __init__(self, trainable: bool = ..., name: Any | None = ..., dtype: Any | None = ..., dynamic: bool = ..., **kwargs) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inputs, *args, **kwargs): ...
    def add_weight(self, name: Any | None = ..., shape: Any | None = ..., dtype: Any | None = ..., initializer: Any | None = ..., regularizer: Any | None = ..., trainable: Any | None = ..., constraint: Any | None = ..., use_resource: Any | None = ..., synchronization=..., aggregation=..., **kwargs): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_signature): ...
    def compute_mask(self, inputs, mask: Any | None = ...): ...
    def __call__(self, *args, **kwargs): ...
    @property
    def dtype(self): ...
    @property
    def name(self): ...
    @property
    def supports_masking(self): ...
    @supports_masking.setter
    def supports_masking(self, value) -> None: ...
    @property
    def dynamic(self): ...
    @property
    def stateful(self): ...
    @stateful.setter
    def stateful(self, value) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value) -> None: ...
    @property
    def activity_regularizer(self): ...
    @activity_regularizer.setter
    def activity_regularizer(self, regularizer) -> None: ...
    @property
    def input_spec(self): ...
    @input_spec.setter
    def input_spec(self, value) -> None: ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def weights(self): ...
    @property
    def updates(self): ...
    @property
    def losses(self): ...
    def add_loss(self, losses, **kwargs): ...
    @property
    def metrics(self): ...
    def add_metric(self, value, name: Any | None = ..., **kwargs) -> None: ...
    def add_update(self, updates, inputs: Any | None = ...) -> None: ...
    def set_weights(self, weights) -> None: ...
    def get_weights(self): ...
    def finalize_state(self) -> None: ...
    def get_updates_for(self, inputs): ...
    def get_losses_for(self, inputs): ...
    def get_input_mask_at(self, node_index): ...
    def get_output_mask_at(self, node_index): ...
    @property
    def input_mask(self): ...
    @property
    def output_mask(self): ...
    def get_input_shape_at(self, node_index): ...
    def get_output_shape_at(self, node_index): ...
    def get_input_at(self, node_index): ...
    def get_output_at(self, node_index): ...
    @property
    def input(self): ...
    @property
    def output(self): ...
    @property
    def input_shape(self): ...
    def count_params(self): ...
    @property
    def output_shape(self): ...
    @property
    def inbound_nodes(self): ...
    @property
    def outbound_nodes(self): ...
    def apply(self, inputs, *args, **kwargs): ...
    def add_variable(self, *args, **kwargs): ...
    @property
    def variables(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def dtype_policy(self): ...
    @property
    def compute_dtype(self): ...
    @property
    def variable_dtype(self): ...
    def __delattr__(self, name) -> None: ...
    def __setattr__(self, name, value) -> None: ...

class TensorFlowOpLayer(Layer):
    node_def: Any
    constants: Any
    built: bool
    def __init__(self, node_def, name, constants: Any | None = ..., trainable: bool = ..., dtype: Any | None = ...) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class AddLoss(Layer):
    unconditional: Any
    def __init__(self, unconditional, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class AddMetric(Layer):
    aggregation: Any
    metric_name: Any
    def __init__(self, aggregation: Any | None = ..., metric_name: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class BaseRandomLayer(Layer):
    def __init__(self, seed: Any | None = ..., force_generator: bool = ..., **kwargs) -> None: ...
InputSpec = input_spec.InputSpec