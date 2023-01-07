from tensorflow.python.distribute import sharded_variable as sharded_variable, values_util as values_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_stateful_random_ops as gen_stateful_random_ops, gen_stateless_random_ops_v2 as gen_stateless_random_ops_v2, math_ops as math_ops, stateless_random_ops as stateless_random_ops, variables as variables
from tensorflow.python.ops.stateless_random_ops import Algorithm as Algorithm
from tensorflow.python.training.tracking import tracking as tracking
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

UINT64_HALF_SPAN: Any
MAX_INT64: Any
MIN_INT64: Any
UINT64_SPAN: Any
SEED_TYPE: str
SEED_MIN = MIN_INT64
SEED_MAX = MAX_INT64
SEED_UINT_SPAN = UINT64_SPAN
SEED_TYPE_BITS: int
SEED_BIT_MASK: int
SEED_SIZE: int
STATE_TYPE = SEED_TYPE
ALGORITHM_TYPE = STATE_TYPE
PHILOX_STATE_SIZE: int
THREEFRY_STATE_SIZE: int
RNG_ALG_PHILOX: Any
RNG_ALG_THREEFRY: Any
DEFAULT_ALGORITHM = RNG_ALG_PHILOX

def non_deterministic_ints(shape, dtype=...): ...
def create_rng_state(seed, alg): ...
def get_replica_id(): ...

class Generator(tracking.AutoTrackable):
    @classmethod
    def from_state(cls, state, alg): ...
    @classmethod
    def from_seed(cls, seed, alg: Any | None = ...): ...
    @classmethod
    def from_non_deterministic_state(cls, alg: Any | None = ...): ...
    @classmethod
    def from_key_counter(cls, key, counter, alg): ...
    def __init__(self, copy_from: Any | None = ..., state: Any | None = ..., alg: Any | None = ...) -> None: ...
    def reset(self, state) -> None: ...
    def reset_from_seed(self, seed) -> None: ...
    def reset_from_key_counter(self, key, counter) -> None: ...
    @property
    def state(self): ...
    @property
    def algorithm(self): ...
    @property
    def key(self): ...
    def skip(self, delta): ...
    def normal(self, shape, mean: float = ..., stddev: float = ..., dtype=..., name: Any | None = ...): ...
    def truncated_normal(self, shape, mean: float = ..., stddev: float = ..., dtype=..., name: Any | None = ...): ...
    def uniform(self, shape, minval: int = ..., maxval: Any | None = ..., dtype=..., name: Any | None = ...): ...
    def uniform_full_int(self, shape, dtype=..., name: Any | None = ...): ...
    def binomial(self, shape, counts, probs, dtype=..., name: Any | None = ...): ...
    def make_seeds(self, count: int = ...): ...
    def split(self, count: int = ...): ...

global_generator: Any

def get_global_generator(): ...
def set_global_generator(generator) -> None: ...