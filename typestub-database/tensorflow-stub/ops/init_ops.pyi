from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops_impl as linalg_ops_impl, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.deprecation import deprecated as deprecated, deprecated_arg_values as deprecated_arg_values, deprecated_args as deprecated_args
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class Initializer:
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class Zeros(Initializer):
    dtype: Any
    def __init__(self, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class Ones(Initializer):
    dtype: Any
    def __init__(self, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class Constant(Initializer):
    value: Any
    dtype: Any
    def __init__(self, value: int = ..., dtype=..., verify_shape: bool = ...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ..., verify_shape: Any | None = ...): ...
    def get_config(self): ...

class RandomUniform(Initializer):
    minval: Any
    maxval: Any
    seed: Any
    dtype: Any
    def __init__(self, minval: float = ..., maxval: Any | None = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class RandomNormal(Initializer):
    mean: Any
    stddev: Any
    seed: Any
    dtype: Any
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class TruncatedNormal(Initializer):
    mean: Any
    stddev: Any
    seed: Any
    dtype: Any
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class UniformUnitScaling(Initializer):
    factor: Any
    seed: Any
    dtype: Any
    def __init__(self, factor: float = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class VarianceScaling(Initializer):
    scale: Any
    mode: Any
    distribution: Any
    seed: Any
    dtype: Any
    def __init__(self, scale: float = ..., mode: str = ..., distribution: str = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class Orthogonal(Initializer):
    gain: Any
    dtype: Any
    seed: Any
    def __init__(self, gain: float = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class ConvolutionDeltaOrthogonal(Initializer):
    gain: Any
    dtype: Any
    seed: Any
    def __init__(self, gain: float = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class ConvolutionOrthogonal(Initializer):
    gain: Any
    dtype: Any
    seed: Any
    def __init__(self, gain: float = ..., seed: Any | None = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...) -> None: ...
    def get_config(self): ...

class ConvolutionOrthogonal2D(ConvolutionOrthogonal):
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...

class ConvolutionOrthogonal1D(ConvolutionOrthogonal):
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...

class ConvolutionOrthogonal3D(ConvolutionOrthogonal):
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...

class Identity(Initializer):
    gain: Any
    dtype: Any
    def __init__(self, gain: float = ..., dtype=...) -> None: ...
    def __call__(self, shape, dtype: Any | None = ..., partition_info: Any | None = ...): ...
    def get_config(self): ...

class GlorotUniform(VarianceScaling):
    def __init__(self, seed: Any | None = ..., dtype=...) -> None: ...
    def get_config(self): ...

class GlorotNormal(VarianceScaling):
    def __init__(self, seed: Any | None = ..., dtype=...) -> None: ...
    def get_config(self): ...
zeros_initializer = Zeros
ones_initializer = Ones
constant_initializer = Constant
random_uniform_initializer = RandomUniform
random_normal_initializer = RandomNormal
truncated_normal_initializer = TruncatedNormal
uniform_unit_scaling_initializer = UniformUnitScaling
variance_scaling_initializer = VarianceScaling
glorot_uniform_initializer = GlorotUniform
glorot_normal_initializer = GlorotNormal
orthogonal_initializer = Orthogonal
identity_initializer = Identity
convolutional_delta_orthogonal = ConvolutionDeltaOrthogonal
convolutional_orthogonal_1d = ConvolutionOrthogonal1D
convolutional_orthogonal_2d = ConvolutionOrthogonal2D
convolutional_orthogonal_3d = ConvolutionOrthogonal3D

def lecun_normal(seed: Any | None = ...): ...
def lecun_uniform(seed: Any | None = ...): ...
def he_normal(seed: Any | None = ...): ...
def he_uniform(seed: Any | None = ...): ...