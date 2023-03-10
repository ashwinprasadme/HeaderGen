import abc
from tensorflow.core.framework import dataset_metadata_pb2 as dataset_metadata_pb2, dataset_options_pb2 as dataset_options_pb2, graph_pb2 as graph_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import iterator_ops as iterator_ops
from tensorflow.python.data.util import nest as nest, random_seed as random_seed, structure as structure, traverse as traverse
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import auto_control_deps as auto_control_deps, composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, function as function, ops as ops, smart_cond as smart_cond, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_dataset_ops as gen_dataset_ops, gen_io_ops as gen_io_ops, gen_stateless_random_ops as gen_stateless_random_ops, logging_ops as logging_ops, math_ops as math_ops, random_ops as random_ops, script_ops as script_ops, string_ops as string_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.training.tracking import base as tracking_base, tracking as tracking
from tensorflow.python.util import deprecation as deprecation, function_utils as function_utils, lazy_loader as lazy_loader
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

wrap_function: Any
autograph_ctx: Any
autograph: Any
parsing_ops: Any
AUTOTUNE: int
INFINITE: int
UNKNOWN: int

class DatasetV2(collections_abc.Iterable, tracking_base.Trackable, composite_tensor.CompositeTensor, metaclass=abc.ABCMeta):
    def __init__(self, variant_tensor): ...
    def options(self): ...
    def __iter__(self): ...
    def __bool__(self): ...
    __nonzero__: Any
    def __len__(self): ...
    @property
    @abc.abstractmethod
    def element_spec(self): ...
    def __debug_string__(self): ...
    def as_numpy_iterator(self): ...
    @staticmethod
    def from_tensors(tensors, name: Any | None = ...): ...
    @staticmethod
    def from_tensor_slices(tensors, name: Any | None = ...): ...
    class _GeneratorState:
        def __init__(self, generator) -> None: ...
        def get_next_id(self, *args): ...
        def get_iterator(self, iterator_id): ...
        def iterator_completed(self, iterator_id) -> None: ...
    @staticmethod
    def from_generator(generator, output_types: Any | None = ..., output_shapes: Any | None = ..., args: Any | None = ..., output_signature: Any | None = ..., name: Any | None = ...): ...
    @staticmethod
    def range(*args, **kwargs): ...
    @staticmethod
    def zip(datasets, name: Any | None = ...): ...
    def concatenate(self, dataset, name: Any | None = ...): ...
    def prefetch(self, buffer_size, name: Any | None = ...): ...
    @staticmethod
    def list_files(file_pattern, shuffle: Any | None = ..., seed: Any | None = ..., name: Any | None = ...): ...
    def repeat(self, count: Any | None = ..., name: Any | None = ...): ...
    def enumerate(self, start: int = ..., name: Any | None = ...): ...
    def shuffle(self, buffer_size, seed: Any | None = ..., reshuffle_each_iteration: Any | None = ..., name: Any | None = ...): ...
    def cache(self, filename: str = ..., name: Any | None = ...): ...
    def take(self, count, name: Any | None = ...): ...
    def skip(self, count, name: Any | None = ...): ...
    def shard(self, num_shards, index, name: Any | None = ...): ...
    def batch(self, batch_size, drop_remainder: bool = ..., num_parallel_calls: Any | None = ..., deterministic: Any | None = ..., name: Any | None = ...): ...
    def padded_batch(self, batch_size, padded_shapes: Any | None = ..., padding_values: Any | None = ..., drop_remainder: bool = ..., name: Any | None = ...): ...
    def map(self, map_func, num_parallel_calls: Any | None = ..., deterministic: Any | None = ..., name: Any | None = ...): ...
    def flat_map(self, map_func, name: Any | None = ...): ...
    def interleave(self, map_func, cycle_length: Any | None = ..., block_length: Any | None = ..., num_parallel_calls: Any | None = ..., deterministic: Any | None = ..., name: Any | None = ...): ...
    def filter(self, predicate, name: Any | None = ...): ...
    def apply(self, transformation_func): ...
    def window(self, size, shift: Any | None = ..., stride: int = ..., drop_remainder: bool = ..., name: Any | None = ...): ...
    def reduce(self, initial_state, reduce_func, name: Any | None = ...): ...
    def get_single_element(self, name: Any | None = ...): ...
    def unbatch(self, name: Any | None = ...): ...
    def with_options(self, options, name: Any | None = ...): ...
    def cardinality(self): ...
    def group_by_window(self, key_func, reduce_func, window_size: Any | None = ..., window_size_func: Any | None = ..., name: Any | None = ...): ...
    def bucket_by_sequence_length(self, element_length_func, bucket_boundaries, bucket_batch_sizes, padded_shapes: Any | None = ..., padding_values: Any | None = ..., pad_to_bucket_boundary: bool = ..., no_padding: bool = ..., drop_remainder: bool = ..., name: Any | None = ...): ...
    @staticmethod
    def random(seed: Any | None = ..., name: Any | None = ...): ...
    def snapshot(self, path, compression: str = ..., reader_func: Any | None = ..., shard_func: Any | None = ..., name: Any | None = ...): ...
    def scan(self, initial_state, scan_func, name: Any | None = ...): ...
    def take_while(self, predicate, name: Any | None = ...): ...
    def unique(self, name: Any | None = ...): ...
    def rejection_resample(self, class_func, target_dist, initial_dist: Any | None = ..., seed: Any | None = ..., name: Any | None = ...): ...
    @staticmethod
    def sample_from_datasets(datasets, weights: Any | None = ..., seed: Any | None = ..., stop_on_empty_dataset: bool = ...): ...
    @staticmethod
    def choose_from_datasets(datasets, choice_dataset, stop_on_empty_dataset: bool = ...): ...

class DatasetV1(DatasetV2, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    def make_one_shot_iterator(self): ...
    def make_initializable_iterator(self, shared_name: Any | None = ...): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def element_spec(self): ...
    @staticmethod
    def from_tensors(tensors, name: Any | None = ...): ...
    @staticmethod
    def from_tensor_slices(tensors, name: Any | None = ...): ...
    @staticmethod
    def from_sparse_tensor_slices(sparse_tensor): ...
    @staticmethod
    def from_generator(generator, output_types: Any | None = ..., output_shapes: Any | None = ..., args: Any | None = ..., output_signature: Any | None = ..., name: Any | None = ...): ...
    @staticmethod
    def range(*args, **kwargs): ...
    @staticmethod
    def zip(datasets, name: Any | None = ...): ...
    def concatenate(self, dataset, name: Any | None = ...): ...
    def prefetch(self, buffer_size, name: Any | None = ...): ...
    @staticmethod
    def list_files(file_pattern, shuffle: Any | None = ..., seed: Any | None = ..., name: Any | None = ...): ...
    def repeat(self, count: Any | None = ..., name: Any | None = ...): ...
    def shuffle(self, buffer_size, seed: Any | None = ..., reshuffle_each_iteration: Any | None = ..., name: Any | None = ...): ...
    def cache(self, filename: str = ..., name: Any | None = ...): ...
    def take(self, count, name: Any | None = ...): ...
    def skip(self, count, name: Any | None = ...): ...
    def shard(self, num_shards, index, name: Any | None = ...): ...
    def batch(self, batch_size, drop_remainder: bool = ..., num_parallel_calls: Any | None = ..., deterministic: Any | None = ..., name: Any | None = ...): ...
    def padded_batch(self, batch_size, padded_shapes: Any | None = ..., padding_values: Any | None = ..., drop_remainder: bool = ..., name: Any | None = ...): ...
    def map(self, map_func, num_parallel_calls: Any | None = ..., deterministic: Any | None = ..., name: Any | None = ...): ...
    def map_with_legacy_function(self, map_func, num_parallel_calls: Any | None = ..., deterministic: Any | None = ...): ...
    def flat_map(self, map_func, name: Any | None = ...): ...
    def interleave(self, map_func, cycle_length: Any | None = ..., block_length: Any | None = ..., num_parallel_calls: Any | None = ..., deterministic: Any | None = ..., name: Any | None = ...): ...
    def filter(self, predicate, name: Any | None = ...): ...
    def filter_with_legacy_function(self, predicate): ...
    def apply(self, transformation_func): ...
    def window(self, size, shift: Any | None = ..., stride: int = ..., drop_remainder: bool = ..., name: Any | None = ...): ...
    def unbatch(self, name: Any | None = ...): ...
    def with_options(self, options, name: Any | None = ...): ...
Dataset = DatasetV2
Dataset = DatasetV1

class DatasetV1Adapter(DatasetV1):
    def __init__(self, dataset) -> None: ...
    def options(self): ...
    @property
    def element_spec(self): ...
    def __iter__(self): ...

def make_one_shot_iterator(dataset): ...
def make_initializable_iterator(dataset, shared_name: Any | None = ...): ...
def get_structure(dataset_or_iterator): ...
def get_legacy_output_classes(dataset_or_iterator): ...
def get_legacy_output_shapes(dataset_or_iterator): ...
def get_legacy_output_types(dataset_or_iterator): ...

class DatasetSource(DatasetV2, metaclass=abc.ABCMeta): ...

class UnaryDataset(DatasetV2, metaclass=abc.ABCMeta):
    def __init__(self, input_dataset, variant_tensor) -> None: ...

class UnaryUnchangedStructureDataset(UnaryDataset):
    def __init__(self, input_dataset, variant_tensor) -> None: ...
    @property
    def element_spec(self): ...

class _VariantDataset(DatasetV2):
    def __init__(self, dataset_variant, structure) -> None: ...
    @property
    def element_spec(self): ...

class _NestedVariant(composite_tensor.CompositeTensor):
    def __init__(self, variant_tensor, element_spec, dataset_shape) -> None: ...

def from_variant(variant, structure): ...
def to_variant(dataset): ...

class DatasetSpec(type_spec.BatchableTypeSpec):
    def __init__(self, element_spec, dataset_shape=...) -> None: ...
    @property
    def value_type(self): ...
    @property
    def element_spec(self): ...
    @staticmethod
    def from_value(value): ...

class StructuredFunctionWrapper:
    def __init__(self, func, transformation_name, dataset: Any | None = ..., input_classes: Any | None = ..., input_shapes: Any | None = ..., input_types: Any | None = ..., input_structure: Any | None = ..., add_to_graph: bool = ..., use_legacy_function: bool = ..., defun_kwargs: Any | None = ...): ...
    @property
    def output_structure(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def function(self): ...

class _NumpyIterator:
    def __init__(self, dataset) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def next(self): ...

class _VariantTracker(tracking.CapturableResource):
    def __init__(self, variant_tensor, resource_creator) -> None: ...

class TensorDataset(DatasetSource):
    def __init__(self, element, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class TensorSliceDataset(DatasetSource):
    def __init__(self, element, is_files: bool = ..., name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class SparseTensorSliceDataset(DatasetSource):
    def __init__(self, sparse_tensor) -> None: ...
    @property
    def element_spec(self): ...

class _GeneratorDataset(DatasetSource):
    def __init__(self, init_args, init_func, next_func, finalize_func, output_signature, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class ZipDataset(DatasetV2):
    def __init__(self, datasets, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class ConcatenateDataset(DatasetV2):
    def __init__(self, input_dataset, dataset_to_concatenate, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class RepeatDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, count, name: Any | None = ...) -> None: ...

class RangeDataset(DatasetSource):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def element_spec(self): ...

class CacheDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, filename, name: Any | None = ...) -> None: ...

class ShuffleDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, buffer_size, seed: Any | None = ..., reshuffle_each_iteration: Any | None = ..., name: Any | None = ...) -> None: ...

class TakeDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, count, name: Any | None = ...) -> None: ...

class SkipDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, count, name: Any | None = ...) -> None: ...

class ShardDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, num_shards, index, name: Any | None = ...) -> None: ...

class BatchDataset(UnaryDataset):
    def __init__(self, input_dataset, batch_size, drop_remainder, name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class ParallelBatchDataset(UnaryDataset):
    def __init__(self, input_dataset, batch_size, drop_remainder, num_parallel_calls, deterministic, name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class PaddedBatchDataset(UnaryDataset):
    def __init__(self, input_dataset, batch_size, padded_shapes, padding_values, drop_remainder, name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class MapDataset(UnaryDataset):
    def __init__(self, input_dataset, map_func, use_inter_op_parallelism: bool = ..., preserve_cardinality: bool = ..., use_legacy_function: bool = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class ParallelMapDataset(UnaryDataset):
    def __init__(self, input_dataset, map_func, num_parallel_calls, deterministic, use_inter_op_parallelism: bool = ..., preserve_cardinality: bool = ..., use_legacy_function: bool = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class FlatMapDataset(UnaryDataset):
    def __init__(self, input_dataset, map_func, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class InterleaveDataset(UnaryDataset):
    def __init__(self, input_dataset, map_func, cycle_length, block_length, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class ParallelInterleaveDataset(UnaryDataset):
    def __init__(self, input_dataset, map_func, cycle_length, block_length, num_parallel_calls, buffer_output_elements=..., prefetch_input_elements=..., deterministic: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class FilterDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, predicate, use_legacy_function: bool = ..., name: Any | None = ...) -> None: ...

class PrefetchDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, buffer_size, slack_period: Any | None = ..., name: Any | None = ...) -> None: ...

class WindowDataset(UnaryDataset):
    def __init__(self, input_dataset, size, shift, stride, drop_remainder, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class _OptionsDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, options, name: Any | None = ...) -> None: ...

def normalize_to_dense(dataset): ...

class _RestructuredDataset(UnaryDataset):
    def __init__(self, dataset, structure) -> None: ...
    @property
    def element_spec(self): ...

class _UnbatchDataset(UnaryDataset):
    def __init__(self, input_dataset, name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class _GroupByWindowDataset(UnaryDataset):
    def __init__(self, input_dataset, key_func, reduce_func, window_size_func, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class RandomDataset(DatasetSource):
    def __init__(self, seed: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class _TakeWhileDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, predicate, name: Any | None = ...) -> None: ...

class _UniqueDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, name: Any | None = ...) -> None: ...

class _SnapshotDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, path, shard_func, compression: Any | None = ..., reader_func: Any | None = ..., pending_snapshot_expiry_seconds: Any | None = ..., use_legacy_function: bool = ..., name: Any | None = ...): ...

class _ScanDataset(UnaryDataset):
    def __init__(self, input_dataset, initial_state, scan_func, use_default_device: Any | None = ..., name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class _DirectedInterleaveDataset(DatasetV2):
    def __init__(self, selector_input, data_inputs, stop_on_empty_dataset: bool = ...) -> None: ...
    @property
    def element_spec(self): ...

DEBUG_MODE: bool

def enable_debug_mode() -> None: ...
def toggle_debug_mode(debug_mode) -> None: ...
