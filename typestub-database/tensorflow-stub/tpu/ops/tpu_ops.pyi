from tensorflow.python.ops.gen_tpu_ops import *
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_tpu_ops as gen_tpu_ops
from tensorflow.python.tpu import tpu_function as tpu_function
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def all_to_all(x, concat_dimension, split_dimension, split_count, group_assignment: Any | None = ..., name: Any | None = ...): ...
def cross_replica_sum(x, group_assignment: Any | None = ..., name: Any | None = ...): ...
def collective_permute(x, source_target_pairs, name: Any | None = ...): ...
def infeed_dequeue(dtype, shape, name: Any | None = ...): ...
def infeed_dequeue_tuple(dtypes, shapes, name: Any | None = ...): ...
def send_tpu_embedding_gradients(inputs, config, learning_rates: Any | None = ..., name: Any | None = ...): ...
def enqueue_tpu_embedding_integer_batch(batch, device_ordinal, mode_override: Any | None = ..., name: Any | None = ...): ...
def enqueue_tpu_embedding_sparse_batch(sample_indices, embedding_indices, aggregation_weights, device_ordinal, combiners: Any | None = ..., mode_override: Any | None = ..., name: Any | None = ...): ...
def enqueue_tpu_embedding_sparse_tensor_batch(sample_indices, embedding_indices, aggregation_weights, table_ids, device_ordinal, max_sequence_lengths: Any | None = ..., num_features: Any | None = ..., combiners: Any | None = ..., mode_override: Any | None = ..., name: Any | None = ...): ...
def enqueue_tpu_embedding_ragged_tensor_batch(sample_splits, embedding_indices, aggregation_weights, table_ids, device_ordinal, max_sequence_lengths: Any | None = ..., num_features: Any | None = ..., combiners: Any | None = ..., mode_override: Any | None = ..., name: Any | None = ...): ...
