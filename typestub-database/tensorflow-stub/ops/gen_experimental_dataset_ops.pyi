from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def assert_cardinality_dataset(input_dataset, cardinality, output_types, output_shapes, name: Any | None = ...): ...

AssertCardinalityDataset: Any

def assert_cardinality_dataset_eager_fallback(input_dataset, cardinality, output_types, output_shapes, name, ctx): ...
def assert_next_dataset(input_dataset, transformations, output_types, output_shapes, name: Any | None = ...): ...

AssertNextDataset: Any

def assert_next_dataset_eager_fallback(input_dataset, transformations, output_types, output_shapes, name, ctx): ...
def auto_shard_dataset(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy: int = ..., num_replicas: int = ..., name: Any | None = ...): ...

AutoShardDataset: Any

def auto_shard_dataset_eager_fallback(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy, num_replicas, name, ctx): ...
def bytes_produced_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Any | None = ...): ...

BytesProducedStatsDataset: Any

def bytes_produced_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def csv_dataset(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name: Any | None = ...): ...

CSVDataset: Any

def csv_dataset_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name, ctx): ...
def csv_dataset_v2(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, exclude_cols, output_shapes, name: Any | None = ...): ...

CSVDatasetV2: Any

def csv_dataset_v2_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, exclude_cols, output_shapes, name, ctx): ...
def choose_fastest_branch_dataset(input_dataset, ratio_numerator, ratio_denominator, other_arguments, num_elements_per_branch, branches, other_arguments_lengths, output_types, output_shapes, name: Any | None = ...): ...

ChooseFastestBranchDataset: Any

def choose_fastest_branch_dataset_eager_fallback(input_dataset, ratio_numerator, ratio_denominator, other_arguments, num_elements_per_branch, branches, other_arguments_lengths, output_types, output_shapes, name, ctx): ...
def choose_fastest_dataset(input_datasets, num_experiments, output_types, output_shapes, name: Any | None = ...): ...

ChooseFastestDataset: Any

def choose_fastest_dataset_eager_fallback(input_datasets, num_experiments, output_types, output_shapes, name, ctx): ...
def compress_element(components, name: Any | None = ...): ...

CompressElement: Any

def compress_element_eager_fallback(components, name, ctx): ...
def compute_batch_size(input_dataset, name: Any | None = ...): ...

ComputeBatchSize: Any

def compute_batch_size_eager_fallback(input_dataset, name, ctx): ...
def data_service_dataset(dataset_id, processing_mode, address, protocol, job_name, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms: int = ..., data_transfer_protocol: str = ..., target_workers: str = ..., name: Any | None = ...): ...

DataServiceDataset: Any

def data_service_dataset_eager_fallback(dataset_id, processing_mode, address, protocol, job_name, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms, data_transfer_protocol, target_workers, name, ctx): ...
def data_service_dataset_v2(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms: int = ..., data_transfer_protocol: str = ..., target_workers: str = ..., name: Any | None = ...): ...

DataServiceDatasetV2: Any

def data_service_dataset_v2_eager_fallback(dataset_id, processing_mode, address, protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, iteration_counter, output_types, output_shapes, task_refresh_interval_hint_ms, data_transfer_protocol, target_workers, name, ctx): ...
def dataset_from_graph(graph_def, name: Any | None = ...): ...

DatasetFromGraph: Any

def dataset_from_graph_eager_fallback(graph_def, name, ctx): ...
def dataset_to_tf_record(input_dataset, filename, compression_type, name: Any | None = ...): ...

DatasetToTFRecord: Any

def dataset_to_tf_record_eager_fallback(input_dataset, filename, compression_type, name, ctx): ...
def dense_to_sparse_batch_dataset(input_dataset, batch_size, row_shape, output_types, output_shapes, name: Any | None = ...): ...

DenseToSparseBatchDataset: Any

def dense_to_sparse_batch_dataset_eager_fallback(input_dataset, batch_size, row_shape, output_types, output_shapes, name, ctx): ...
def directed_interleave_dataset(selector_input_dataset, data_input_datasets, output_types, output_shapes, stop_on_empty_dataset: bool = ..., name: Any | None = ...): ...

DirectedInterleaveDataset: Any

def directed_interleave_dataset_eager_fallback(selector_input_dataset, data_input_datasets, output_types, output_shapes, stop_on_empty_dataset, name, ctx): ...
def dummy_iteration_counter(name: Any | None = ...): ...

DummyIterationCounter: Any

def dummy_iteration_counter_eager_fallback(name, ctx): ...
def experimental_assert_next_dataset(input_dataset, transformations, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalAssertNextDataset: Any

def experimental_assert_next_dataset_eager_fallback(input_dataset, transformations, output_types, output_shapes, name, ctx): ...
def experimental_auto_shard_dataset(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy: int = ..., name: Any | None = ...): ...

ExperimentalAutoShardDataset: Any

def experimental_auto_shard_dataset_eager_fallback(input_dataset, num_workers, index, output_types, output_shapes, auto_shard_policy, name, ctx): ...
def experimental_bytes_produced_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalBytesProducedStatsDataset: Any

def experimental_bytes_produced_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def experimental_csv_dataset(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name: Any | None = ...): ...

ExperimentalCSVDataset: Any

def experimental_csv_dataset_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name, ctx): ...
def experimental_choose_fastest_dataset(input_datasets, num_experiments, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalChooseFastestDataset: Any

def experimental_choose_fastest_dataset_eager_fallback(input_datasets, num_experiments, output_types, output_shapes, name, ctx): ...
def experimental_dataset_cardinality(input_dataset, name: Any | None = ...): ...

ExperimentalDatasetCardinality: Any

def experimental_dataset_cardinality_eager_fallback(input_dataset, name, ctx): ...
def experimental_dataset_to_tf_record(input_dataset, filename, compression_type, name: Any | None = ...): ...

ExperimentalDatasetToTFRecord: Any

def experimental_dataset_to_tf_record_eager_fallback(input_dataset, filename, compression_type, name, ctx): ...
def experimental_dense_to_sparse_batch_dataset(input_dataset, batch_size, row_shape, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalDenseToSparseBatchDataset: Any

def experimental_dense_to_sparse_batch_dataset_eager_fallback(input_dataset, batch_size, row_shape, output_types, output_shapes, name, ctx): ...
def experimental_directed_interleave_dataset(selector_input_dataset, data_input_datasets, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalDirectedInterleaveDataset: Any

def experimental_directed_interleave_dataset_eager_fallback(selector_input_dataset, data_input_datasets, output_types, output_shapes, name, ctx): ...
def experimental_group_by_reducer_dataset(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalGroupByReducerDataset: Any

def experimental_group_by_reducer_dataset_eager_fallback(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name, ctx): ...
def experimental_group_by_window_dataset(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalGroupByWindowDataset: Any

def experimental_group_by_window_dataset_eager_fallback(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, name, ctx): ...
def experimental_ignore_errors_dataset(input_dataset, output_types, output_shapes, log_warning: bool = ..., name: Any | None = ...): ...

ExperimentalIgnoreErrorsDataset: Any

def experimental_ignore_errors_dataset_eager_fallback(input_dataset, output_types, output_shapes, log_warning, name, ctx): ...
def experimental_iterator_get_device(resource, name: Any | None = ...): ...

ExperimentalIteratorGetDevice: Any

def experimental_iterator_get_device_eager_fallback(resource, name, ctx): ...
def experimental_lmdb_dataset(filenames, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalLMDBDataset: Any

def experimental_lmdb_dataset_eager_fallback(filenames, output_types, output_shapes, name, ctx): ...
def experimental_latency_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalLatencyStatsDataset: Any

def experimental_latency_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def experimental_map_and_batch_dataset(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality: bool = ..., name: Any | None = ...): ...

ExperimentalMapAndBatchDataset: Any

def experimental_map_and_batch_dataset_eager_fallback(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality, name, ctx): ...
def experimental_map_dataset(input_dataset, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism: bool = ..., preserve_cardinality: bool = ..., name: Any | None = ...): ...

ExperimentalMapDataset: Any

def experimental_map_dataset_eager_fallback(input_dataset, other_arguments, f, output_types, output_shapes, use_inter_op_parallelism, preserve_cardinality, name, ctx): ...
def experimental_matching_files_dataset(patterns, name: Any | None = ...): ...

ExperimentalMatchingFilesDataset: Any

def experimental_matching_files_dataset_eager_fallback(patterns, name, ctx): ...
def experimental_max_intra_op_parallelism_dataset(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalMaxIntraOpParallelismDataset: Any

def experimental_max_intra_op_parallelism_dataset_eager_fallback(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name, ctx): ...
def experimental_non_serializable_dataset(input_dataset, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalNonSerializableDataset: Any

def experimental_non_serializable_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def experimental_parallel_interleave_dataset(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalParallelInterleaveDataset: Any

def experimental_parallel_interleave_dataset_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, name, ctx): ...
def experimental_parse_example_dataset(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy: bool = ..., name: Any | None = ...): ...

ExperimentalParseExampleDataset: Any

def experimental_parse_example_dataset_eager_fallback(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy, name, ctx): ...
def experimental_private_thread_pool_dataset(input_dataset, num_threads, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalPrivateThreadPoolDataset: Any

def experimental_private_thread_pool_dataset_eager_fallback(input_dataset, num_threads, output_types, output_shapes, name, ctx): ...
def experimental_random_dataset(seed, seed2, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalRandomDataset: Any

def experimental_random_dataset_eager_fallback(seed, seed2, output_types, output_shapes, name, ctx): ...
def experimental_rebatch_dataset(input_dataset, num_replicas, output_types, output_shapes, use_fallback: bool = ..., name: Any | None = ...): ...

ExperimentalRebatchDataset: Any

def experimental_rebatch_dataset_eager_fallback(input_dataset, num_replicas, output_types, output_shapes, use_fallback, name, ctx): ...
def experimental_scan_dataset(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality: bool = ..., name: Any | None = ...): ...

ExperimentalScanDataset: Any

def experimental_scan_dataset_eager_fallback(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality, name, ctx): ...
def experimental_set_stats_aggregator_dataset(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalSetStatsAggregatorDataset: Any

def experimental_set_stats_aggregator_dataset_eager_fallback(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name, ctx): ...
def experimental_sleep_dataset(input_dataset, sleep_microseconds, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalSleepDataset: Any

def experimental_sleep_dataset_eager_fallback(input_dataset, sleep_microseconds, output_types, output_shapes, name, ctx): ...
def experimental_sliding_window_dataset(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalSlidingWindowDataset: Any

def experimental_sliding_window_dataset_eager_fallback(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, name, ctx): ...
def experimental_sql_dataset(driver_name, data_source_name, query, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalSqlDataset: Any

def experimental_sql_dataset_eager_fallback(driver_name, data_source_name, query, output_types, output_shapes, name, ctx): ...
def experimental_stats_aggregator_handle(container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

ExperimentalStatsAggregatorHandle: Any

def experimental_stats_aggregator_handle_eager_fallback(container, shared_name, name, ctx): ...
def experimental_stats_aggregator_summary(iterator, name: Any | None = ...): ...

ExperimentalStatsAggregatorSummary: Any

def experimental_stats_aggregator_summary_eager_fallback(iterator, name, ctx): ...
def experimental_take_while_dataset(input_dataset, other_arguments, predicate, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalTakeWhileDataset: Any

def experimental_take_while_dataset_eager_fallback(input_dataset, other_arguments, predicate, output_types, output_shapes, name, ctx): ...
def experimental_thread_pool_dataset(input_dataset, thread_pool, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalThreadPoolDataset: Any

def experimental_thread_pool_dataset_eager_fallback(input_dataset, thread_pool, output_types, output_shapes, name, ctx): ...
def experimental_thread_pool_handle(num_threads, display_name, max_intra_op_parallelism: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

ExperimentalThreadPoolHandle: Any

def experimental_thread_pool_handle_eager_fallback(num_threads, display_name, max_intra_op_parallelism, container, shared_name, name, ctx): ...
def experimental_unbatch_dataset(input_dataset, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalUnbatchDataset: Any

def experimental_unbatch_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def experimental_unique_dataset(input_dataset, output_types, output_shapes, name: Any | None = ...): ...

ExperimentalUniqueDataset: Any

def experimental_unique_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def get_element_at_index(dataset, index, output_types, output_shapes, name: Any | None = ...): ...

GetElementAtIndex: Any

def get_element_at_index_eager_fallback(dataset, index, output_types, output_shapes, name, ctx): ...
def group_by_reducer_dataset(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name: Any | None = ...): ...

GroupByReducerDataset: Any

def group_by_reducer_dataset_eager_fallback(input_dataset, key_func_other_arguments, init_func_other_arguments, reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func, reduce_func, finalize_func, output_types, output_shapes, name, ctx): ...
def group_by_window_dataset(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, metadata: str = ..., name: Any | None = ...): ...

GroupByWindowDataset: Any

def group_by_window_dataset_eager_fallback(input_dataset, key_func_other_arguments, reduce_func_other_arguments, window_size_func_other_arguments, key_func, reduce_func, window_size_func, output_types, output_shapes, metadata, name, ctx): ...
def ignore_errors_dataset(input_dataset, output_types, output_shapes, log_warning: bool = ..., name: Any | None = ...): ...

IgnoreErrorsDataset: Any

def ignore_errors_dataset_eager_fallback(input_dataset, output_types, output_shapes, log_warning, name, ctx): ...
def initialize_table_from_dataset(table_handle, dataset, name: Any | None = ...): ...

InitializeTableFromDataset: Any

def initialize_table_from_dataset_eager_fallback(table_handle, dataset, name, ctx): ...
def iterator_get_device(resource, name: Any | None = ...): ...

IteratorGetDevice: Any

def iterator_get_device_eager_fallback(resource, name, ctx): ...
def lmdb_dataset(filenames, output_types, output_shapes, name: Any | None = ...): ...

LMDBDataset: Any

def lmdb_dataset_eager_fallback(filenames, output_types, output_shapes, name, ctx): ...
def latency_stats_dataset(input_dataset, tag, output_types, output_shapes, name: Any | None = ...): ...

LatencyStatsDataset: Any

def latency_stats_dataset_eager_fallback(input_dataset, tag, output_types, output_shapes, name, ctx): ...
def legacy_parallel_interleave_dataset_v2(input_dataset, other_arguments, cycle_length, block_length, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, deterministic: str = ..., metadata: str = ..., name: Any | None = ...): ...

LegacyParallelInterleaveDatasetV2: Any

def legacy_parallel_interleave_dataset_v2_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, deterministic, metadata, name, ctx): ...
def load_dataset(path, reader_func_other_args, output_types, output_shapes, reader_func, compression: str = ..., name: Any | None = ...): ...

LoadDataset: Any

def load_dataset_eager_fallback(path, reader_func_other_args, output_types, output_shapes, reader_func, compression, name, ctx): ...
def map_and_batch_dataset(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality: bool = ..., metadata: str = ..., name: Any | None = ...): ...

MapAndBatchDataset: Any

def map_and_batch_dataset_eager_fallback(input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder, f, output_types, output_shapes, preserve_cardinality, metadata, name, ctx): ...
def matching_files_dataset(patterns, name: Any | None = ...): ...

MatchingFilesDataset: Any

def matching_files_dataset_eager_fallback(patterns, name, ctx): ...
def max_intra_op_parallelism_dataset(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name: Any | None = ...): ...

MaxIntraOpParallelismDataset: Any

def max_intra_op_parallelism_dataset_eager_fallback(input_dataset, max_intra_op_parallelism, output_types, output_shapes, name, ctx): ...
def non_serializable_dataset(input_dataset, output_types, output_shapes, name: Any | None = ...): ...

NonSerializableDataset: Any

def non_serializable_dataset_eager_fallback(input_dataset, output_types, output_shapes, name, ctx): ...
def parallel_interleave_dataset(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, metadata: str = ..., name: Any | None = ...): ...

ParallelInterleaveDataset: Any

def parallel_interleave_dataset_eager_fallback(input_dataset, other_arguments, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes, metadata, name, ctx): ...
def parse_example_dataset(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy: bool = ..., ragged_keys=..., ragged_value_types=..., ragged_split_types=..., name: Any | None = ...): ...

ParseExampleDataset: Any

def parse_example_dataset_eager_fallback(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, sloppy, ragged_keys, ragged_value_types, ragged_split_types, name, ctx): ...
def parse_example_dataset_v2(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, deterministic: str = ..., ragged_keys=..., ragged_value_types=..., ragged_split_types=..., name: Any | None = ...): ...

ParseExampleDatasetV2: Any

def parse_example_dataset_v2_eager_fallback(input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys, sparse_types, dense_shapes, output_types, output_shapes, deterministic, ragged_keys, ragged_value_types, ragged_split_types, name, ctx): ...
def private_thread_pool_dataset(input_dataset, num_threads, output_types, output_shapes, name: Any | None = ...): ...

PrivateThreadPoolDataset: Any

def private_thread_pool_dataset_eager_fallback(input_dataset, num_threads, output_types, output_shapes, name, ctx): ...
def random_dataset(seed, seed2, output_types, output_shapes, metadata: str = ..., name: Any | None = ...): ...

RandomDataset: Any

def random_dataset_eager_fallback(seed, seed2, output_types, output_shapes, metadata, name, ctx): ...
def rebatch_dataset(input_dataset, num_replicas, output_types, output_shapes, use_fallback: bool = ..., name: Any | None = ...): ...

RebatchDataset: Any

def rebatch_dataset_eager_fallback(input_dataset, num_replicas, output_types, output_shapes, use_fallback, name, ctx): ...
def rebatch_dataset_v2(input_dataset, batch_sizes, drop_remainder, output_types, output_shapes, name: Any | None = ...): ...

RebatchDatasetV2: Any

def rebatch_dataset_v2_eager_fallback(input_dataset, batch_sizes, drop_remainder, output_types, output_shapes, name, ctx): ...
def register_dataset(dataset, address, protocol, external_state_policy, element_spec: str = ..., name: Any | None = ...): ...

RegisterDataset: Any

def register_dataset_eager_fallback(dataset, address, protocol, external_state_policy, element_spec, name, ctx): ...
def sampling_dataset(input_dataset, rate, seed, seed2, output_types, output_shapes, name: Any | None = ...): ...

SamplingDataset: Any

def sampling_dataset_eager_fallback(input_dataset, rate, seed, seed2, output_types, output_shapes, name, ctx): ...
def save_dataset(input_dataset, path, shard_func_other_args, shard_func, compression: str = ..., use_shard_func: bool = ..., name: Any | None = ...): ...

SaveDataset: Any

def save_dataset_eager_fallback(input_dataset, path, shard_func_other_args, shard_func, compression, use_shard_func, name, ctx): ...
def save_dataset_v2(input_dataset, path, shard_func_other_args, shard_func, output_types, output_shapes, compression: str = ..., use_shard_func: bool = ..., name: Any | None = ...): ...

SaveDatasetV2: Any

def save_dataset_v2_eager_fallback(input_dataset, path, shard_func_other_args, shard_func, output_types, output_shapes, compression, use_shard_func, name, ctx): ...
def scan_dataset(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality: bool = ..., use_default_device: bool = ..., metadata: str = ..., name: Any | None = ...): ...

ScanDataset: Any

def scan_dataset_eager_fallback(input_dataset, initial_state, other_arguments, f, output_types, output_shapes, preserve_cardinality, use_default_device, metadata, name, ctx): ...
def set_stats_aggregator_dataset(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name: Any | None = ...): ...

SetStatsAggregatorDataset: Any

def set_stats_aggregator_dataset_eager_fallback(input_dataset, stats_aggregator, tag, counter_prefix, output_types, output_shapes, name, ctx): ...
def sleep_dataset(input_dataset, sleep_microseconds, output_types, output_shapes, name: Any | None = ...): ...

SleepDataset: Any

def sleep_dataset_eager_fallback(input_dataset, sleep_microseconds, output_types, output_shapes, name, ctx): ...
def sliding_window_dataset(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, name: Any | None = ...): ...

SlidingWindowDataset: Any

def sliding_window_dataset_eager_fallback(input_dataset, window_size, window_shift, window_stride, output_types, output_shapes, name, ctx): ...
def snapshot_dataset(input_dataset, path, output_types, output_shapes, compression: str = ..., reader_path_prefix: str = ..., writer_path_prefix: str = ..., shard_size_bytes: int = ..., pending_snapshot_expiry_seconds: int = ..., num_reader_threads: int = ..., reader_buffer_size: int = ..., num_writer_threads: int = ..., writer_buffer_size: int = ..., shuffle_on_read: bool = ..., seed: int = ..., seed2: int = ..., mode: str = ..., snapshot_name: str = ..., name: Any | None = ...): ...

SnapshotDataset: Any

def snapshot_dataset_eager_fallback(input_dataset, path, output_types, output_shapes, compression, reader_path_prefix, writer_path_prefix, shard_size_bytes, pending_snapshot_expiry_seconds, num_reader_threads, reader_buffer_size, num_writer_threads, writer_buffer_size, shuffle_on_read, seed, seed2, mode, snapshot_name, name, ctx): ...
def snapshot_dataset_reader(shard_dir, start_index, output_types, output_shapes, version, compression: str = ..., name: Any | None = ...): ...

SnapshotDatasetReader: Any

def snapshot_dataset_reader_eager_fallback(shard_dir, start_index, output_types, output_shapes, version, compression, name, ctx): ...
def snapshot_dataset_v2(input_dataset, path, reader_func_other_args, shard_func_other_args, output_types, output_shapes, reader_func, shard_func, compression: str = ..., reader_prefix: str = ..., writer_prefix: str = ..., hash_valid: bool = ..., hash: int = ..., metadata: str = ..., name: Any | None = ...): ...

SnapshotDatasetV2: Any

def snapshot_dataset_v2_eager_fallback(input_dataset, path, reader_func_other_args, shard_func_other_args, output_types, output_shapes, reader_func, shard_func, compression, reader_prefix, writer_prefix, hash_valid, hash, metadata, name, ctx): ...
def snapshot_nested_dataset_reader(inputs, output_types, output_shapes, name: Any | None = ...): ...

SnapshotNestedDatasetReader: Any

def snapshot_nested_dataset_reader_eager_fallback(inputs, output_types, output_shapes, name, ctx): ...
def sql_dataset(driver_name, data_source_name, query, output_types, output_shapes, name: Any | None = ...): ...

SqlDataset: Any

def sql_dataset_eager_fallback(driver_name, data_source_name, query, output_types, output_shapes, name, ctx): ...
def stats_aggregator_handle(container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

StatsAggregatorHandle: Any

def stats_aggregator_handle_eager_fallback(container, shared_name, name, ctx): ...
def stats_aggregator_handle_v2(container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

StatsAggregatorHandleV2: Any

def stats_aggregator_handle_v2_eager_fallback(container, shared_name, name, ctx): ...
def stats_aggregator_set_summary_writer(stats_aggregator, summary, name: Any | None = ...): ...

StatsAggregatorSetSummaryWriter: Any

def stats_aggregator_set_summary_writer_eager_fallback(stats_aggregator, summary, name, ctx): ...
def stats_aggregator_summary(iterator, name: Any | None = ...): ...

StatsAggregatorSummary: Any

def stats_aggregator_summary_eager_fallback(iterator, name, ctx): ...
def take_while_dataset(input_dataset, other_arguments, predicate, output_types, output_shapes, metadata: str = ..., name: Any | None = ...): ...

TakeWhileDataset: Any

def take_while_dataset_eager_fallback(input_dataset, other_arguments, predicate, output_types, output_shapes, metadata, name, ctx): ...
def thread_pool_dataset(input_dataset, thread_pool, output_types, output_shapes, name: Any | None = ...): ...

ThreadPoolDataset: Any

def thread_pool_dataset_eager_fallback(input_dataset, thread_pool, output_types, output_shapes, name, ctx): ...
def thread_pool_handle(num_threads, display_name, max_intra_op_parallelism: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

ThreadPoolHandle: Any

def thread_pool_handle_eager_fallback(num_threads, display_name, max_intra_op_parallelism, container, shared_name, name, ctx): ...
def unbatch_dataset(input_dataset, output_types, output_shapes, metadata: str = ..., name: Any | None = ...): ...

UnbatchDataset: Any

def unbatch_dataset_eager_fallback(input_dataset, output_types, output_shapes, metadata, name, ctx): ...
def uncompress_element(compressed, output_types, output_shapes, name: Any | None = ...): ...

UncompressElement: Any

def uncompress_element_eager_fallback(compressed, output_types, output_shapes, name, ctx): ...
def unique_dataset(input_dataset, output_types, output_shapes, metadata: str = ..., name: Any | None = ...): ...

UniqueDataset: Any

def unique_dataset_eager_fallback(input_dataset, output_types, output_shapes, metadata, name, ctx): ...
