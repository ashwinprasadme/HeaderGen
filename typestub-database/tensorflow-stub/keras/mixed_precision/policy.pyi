from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.mixed_precision import device_compatibility_check as device_compatibility_check
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training.experimental import mixed_precision_global_state as mixed_precision_global_state
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class Policy:
    def __init__(self, name) -> None: ...
    @property
    def variable_dtype(self): ...
    @property
    def compute_dtype(self): ...
    @property
    def name(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class PolicyV1(Policy):
    def __init__(self, name, loss_scale: str = ...) -> None: ...
    @property
    def loss_scale(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

def global_policy(): ...
def set_global_policy(policy) -> None: ...
def policy_scope(policy) -> None: ...
def serialize(policy): ...
def deserialize(config, custom_objects: Any | None = ...): ...
