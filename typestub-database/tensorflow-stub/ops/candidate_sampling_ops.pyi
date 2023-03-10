from tensorflow.python.framework import random_seed as random_seed
from tensorflow.python.ops import array_ops as array_ops, gen_candidate_sampling_ops as gen_candidate_sampling_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: Any | None = ..., name: Any | None = ...): ...
def log_uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: Any | None = ..., name: Any | None = ...): ...
def learned_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: Any | None = ..., name: Any | None = ...): ...
def fixed_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, vocab_file: str = ..., distortion: float = ..., num_reserved_ids: int = ..., num_shards: int = ..., shard: int = ..., unigrams=..., seed: Any | None = ..., name: Any | None = ...): ...
def all_candidate_sampler(true_classes, num_true, num_sampled, unique, seed: Any | None = ..., name: Any | None = ...): ...
def compute_accidental_hits(true_classes, sampled_candidates, num_true, seed: Any | None = ..., name: Any | None = ...): ...
