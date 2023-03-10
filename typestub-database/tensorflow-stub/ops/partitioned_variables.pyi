from typing import Any

def variable_axis_size_partitioner(max_shard_bytes, axis: int = ..., bytes_per_string_element: int = ..., max_shards: Any | None = ...): ...
def min_max_variable_partitioner(max_partitions: int = ..., axis: int = ..., min_slice_size=..., bytes_per_string_element: int = ...): ...
def fixed_size_partitioner(num_shards, axis: int = ...): ...
def create_partitioned_variables(shape, slicing, initializer, dtype=..., trainable: bool = ..., collections: Any | None = ..., name: Any | None = ..., reuse: Any | None = ...): ...
