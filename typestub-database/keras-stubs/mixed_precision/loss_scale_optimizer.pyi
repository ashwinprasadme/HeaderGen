import abc
import tensorflow.compat.v2 as tf
from keras import backend as backend, optimizers as optimizers
from keras.optimizer_experimental import optimizer as optimizer_experimental
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from typing import Any

class _UnwrapPreventer:
    value: Any
    def __init__(self, value) -> None: ...

class _DynamicLossScaleState(tf.__internal__.tracking.Trackable):
    def __init__(self, initial_loss_scale, growth_steps, multiplier) -> None: ...
    @property
    def initial_loss_scale(self): ...
    @property
    def growth_steps(self): ...
    @property
    def multiplier(self): ...
    @property
    def current_loss_scale(self): ...
    @property
    def counter(self): ...
    def __call__(self): ...
    def update(self, grads): ...

class LossScaleOptimizer(tf.__internal__.tracking.DelegatingTrackableMixin, optimizer_v2.OptimizerV2):
    def __init__(self, inner_optimizer, dynamic: bool = ..., initial_scale: Any | None = ..., dynamic_growth_steps: Any | None = ...) -> None: ...
    @property
    def dynamic(self): ...
    @property
    def loss_scale(self): ...
    @property
    def dynamic_counter(self): ...
    @property
    def initial_scale(self): ...
    @property
    def dynamic_growth_steps(self): ...
    @property
    def inner_optimizer(self): ...
    def get_scaled_loss(self, loss): ...
    def get_unscaled_gradients(self, grads): ...
    def get_gradients(self, loss, params): ...
    def apply_gradients(self, grads_and_vars, name: Any | None = ..., experimental_aggregate_gradients: bool = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...
    @property
    def iterations(self): ...
    @iterations.setter
    def iterations(self, variable) -> None: ...
    def get_slot_names(self): ...
    def variables(self): ...
    @property
    def weights(self): ...
    def get_weights(self): ...
    def set_weights(self, weights): ...
    @property
    def clipnorm(self): ...
    @clipnorm.setter
    def clipnorm(self, val) -> None: ...
    @property
    def global_clipnorm(self): ...
    @global_clipnorm.setter
    def global_clipnorm(self, val) -> None: ...
    @property
    def clipvalue(self): ...
    @clipvalue.setter
    def clipvalue(self, val) -> None: ...
    def get_slot(self, var, slot_name): ...
    def add_slot(self, var, slot_name, initializer: str = ...): ...
    def __getattribute__(self, name): ...
    def __dir__(self): ...
    def __setattr__(self, name, value) -> None: ...
    @property
    def learning_rate(self): ...
    @learning_rate.setter
    def learning_rate(self, value) -> None: ...
    @property
    def lr(self): ...
    @lr.setter
    def lr(self, value) -> None: ...

class LossScaleOptimizerV1(LossScaleOptimizer):
    def __init__(self, optimizer, loss_scale) -> None: ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class LossScaleOptimizerV3(tf.__internal__.tracking.DelegatingTrackableMixin, optimizer_experimental.Optimizer, metaclass=abc.ABCMeta):
    def __init__(self, inner_optimizer, dynamic: bool = ..., initial_scale: Any | None = ..., dynamic_growth_steps: Any | None = ...) -> None: ...
    @property
    def dynamic(self): ...
    @property
    def loss_scale(self): ...
    @property
    def dynamic_counter(self): ...
    @property
    def initial_scale(self): ...
    @property
    def dynamic_growth_steps(self): ...
    @property
    def inner_optimizer(self): ...
    def get_scaled_loss(self, loss): ...
    def get_unscaled_gradients(self, grads): ...
    def compute_gradients(self, loss, var_list, tape: Any | None = ...): ...
    def apply_gradients(self, grads_and_vars, skip_gradients_aggregation: bool = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...
    @property
    def iterations(self): ...
    @property
    def learning_rate(self): ...
    @learning_rate.setter
    def learning_rate(self, learning_rate) -> None: ...

class FakeOptimizerForRestoration(tf.__internal__.tracking.Trackable):
    def __init__(self, optimizer) -> None: ...
    def get_slot_names(self): ...

def strategy_supports_loss_scaling(): ...
