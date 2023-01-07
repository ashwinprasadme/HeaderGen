from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def non_deterministic_ints(shape, dtype=..., name: Any | None = ...): ...

NonDeterministicInts: Any

def non_deterministic_ints_eager_fallback(shape, dtype, name, ctx): ...
def rng_read_and_skip(resource, alg, delta, name: Any | None = ...): ...

RngReadAndSkip: Any

def rng_read_and_skip_eager_fallback(resource, alg, delta, name, ctx): ...
def rng_skip(resource, algorithm, delta, name: Any | None = ...): ...

RngSkip: Any

def rng_skip_eager_fallback(resource, algorithm, delta, name, ctx): ...
def stateful_random_binomial(resource, algorithm, shape, counts, probs, dtype=..., name: Any | None = ...): ...

StatefulRandomBinomial: Any

def stateful_random_binomial_eager_fallback(resource, algorithm, shape, counts, probs, dtype, name, ctx): ...
def stateful_standard_normal(resource, shape, dtype=..., name: Any | None = ...): ...

StatefulStandardNormal: Any

def stateful_standard_normal_eager_fallback(resource, shape, dtype, name, ctx): ...
def stateful_standard_normal_v2(resource, algorithm, shape, dtype=..., name: Any | None = ...): ...

StatefulStandardNormalV2: Any

def stateful_standard_normal_v2_eager_fallback(resource, algorithm, shape, dtype, name, ctx): ...
def stateful_truncated_normal(resource, algorithm, shape, dtype=..., name: Any | None = ...): ...

StatefulTruncatedNormal: Any

def stateful_truncated_normal_eager_fallback(resource, algorithm, shape, dtype, name, ctx): ...
def stateful_uniform(resource, algorithm, shape, dtype=..., name: Any | None = ...): ...

StatefulUniform: Any

def stateful_uniform_eager_fallback(resource, algorithm, shape, dtype, name, ctx): ...
def stateful_uniform_full_int(resource, algorithm, shape, dtype=..., name: Any | None = ...): ...

StatefulUniformFullInt: Any

def stateful_uniform_full_int_eager_fallback(resource, algorithm, shape, dtype, name, ctx): ...
def stateful_uniform_int(resource, algorithm, shape, minval, maxval, name: Any | None = ...): ...

StatefulUniformInt: Any

def stateful_uniform_int_eager_fallback(resource, algorithm, shape, minval, maxval, name, ctx): ...