from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes
from tensorflow.python.keras import backend as backend
from tensorflow.python.ops import array_ops as array_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops as linalg_ops, math_ops as math_ops, random_ops as random_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class Initializer:
    def __call__(self, shape, dtype: Any | None = ..., **kwargs) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class Zeros(Initializer):
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...

class Ones(Initializer):
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...

class Constant(Initializer):
    value: Any
    def __init__(self, value: int = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class RandomUniform(Initializer):
    minval: Any
    maxval: Any
    seed: Any
    def __init__(self, minval=..., maxval: float = ..., seed: Any | None = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class RandomNormal(Initializer):
    mean: Any
    stddev: Any
    seed: Any
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Any | None = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class TruncatedNormal(Initializer):
    mean: Any
    stddev: Any
    seed: Any
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Any | None = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class VarianceScaling(Initializer):
    scale: Any
    mode: Any
    distribution: Any
    seed: Any
    def __init__(self, scale: float = ..., mode: str = ..., distribution: str = ..., seed: Any | None = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class Orthogonal(Initializer):
    gain: Any
    seed: Any
    def __init__(self, gain: float = ..., seed: Any | None = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class Identity(Initializer):
    gain: Any
    def __init__(self, gain: float = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., **kwargs): ...
    def get_config(self): ...

class GlorotUniform(VarianceScaling):
    def __init__(self, seed: Any | None = ...) -> None: ...
    def get_config(self): ...

class GlorotNormal(VarianceScaling):
    def __init__(self, seed: Any | None = ...) -> None: ...
    def get_config(self): ...

class LecunNormal(VarianceScaling):
    def __init__(self, seed: Any | None = ...) -> None: ...
    def get_config(self): ...

class LecunUniform(VarianceScaling):
    def __init__(self, seed: Any | None = ...) -> None: ...
    def get_config(self): ...

class HeNormal(VarianceScaling):
    def __init__(self, seed: Any | None = ...) -> None: ...
    def get_config(self): ...

class HeUniform(VarianceScaling):
    def __init__(self, seed: Any | None = ...) -> None: ...
    def get_config(self): ...

class _RandomGenerator:
    seed: Any
    def __init__(self, seed: Any | None = ...) -> None: ...
    def random_normal(self, shape, mean: float = ..., stddev: int = ..., dtype=...): ...
    def random_uniform(self, shape, minval, maxval, dtype): ...
    def truncated_normal(self, shape, mean, stddev, dtype): ...
