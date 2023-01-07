import abc
import tensorflow.compat.v2 as tf
from keras import backend as backend, initializers as initializers
from keras.optimizer_v2 import learning_rate_schedule as learning_rate_schedule
from typing import Any

class _BaseOptimizer(tf.Module, metaclass=abc.ABCMeta):
    def __init__(self, name, clipnorm: Any | None = ..., clipvalue: Any | None = ..., global_clipnorm: Any | None = ..., use_ema: bool = ..., ema_momentum: float = ..., ema_overwrite_frequency: int = ..., jit_compile: bool = ..., **kwargs) -> None: ...
    @abc.abstractmethod
    def update_step(self, gradient, variable): ...
    def compute_gradients(self, loss, var_list, tape: Any | None = ...): ...
    @property
    def iterations(self): ...
    @property
    def learning_rate(self): ...
    @learning_rate.setter
    def learning_rate(self, learning_rate) -> None: ...
    @abc.abstractmethod
    def build(self, var_list): ...
    def add_variable(self, shape, dtype: Any | None = ..., initializer: str = ..., name: Any | None = ...): ...
    def add_variable_from_reference(self, model_variable, variable_name, initial_value: Any | None = ...): ...
    def minimize(self, loss, var_list, tape: Any | None = ...) -> None: ...
    def apply_gradients(self, grads_and_vars) -> None: ...
    def finalize_variable_values(self, var_list) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class Optimizer(_BaseOptimizer, metaclass=abc.ABCMeta):
    def __init__(self, name, clipnorm: Any | None = ..., clipvalue: Any | None = ..., global_clipnorm: Any | None = ..., use_ema: bool = ..., ema_momentum: float = ..., ema_overwrite_frequency: int = ..., jit_compile: bool = ..., **kwargs) -> None: ...
    def add_variable_from_reference(self, model_variable, variable_name, initial_value: Any | None = ...): ...
    def aggregate_gradients(self, grads_and_vars): ...
    def apply_gradients(self, grads_and_vars, skip_gradients_aggregation: bool = ...) -> None: ...

class RestoredOptimizer(Optimizer, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    def get_config(self) -> None: ...