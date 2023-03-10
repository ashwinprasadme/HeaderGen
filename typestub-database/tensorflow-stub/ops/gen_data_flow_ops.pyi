from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def accumulator_apply_gradient(handle, local_step, gradient, name: Any | None = ...): ...

AccumulatorApplyGradient: Any

def accumulator_apply_gradient_eager_fallback(handle, local_step, gradient, name, ctx) -> None: ...
def accumulator_num_accumulated(handle, name: Any | None = ...): ...

AccumulatorNumAccumulated: Any

def accumulator_num_accumulated_eager_fallback(handle, name, ctx) -> None: ...
def accumulator_set_global_step(handle, new_global_step, name: Any | None = ...): ...

AccumulatorSetGlobalStep: Any

def accumulator_set_global_step_eager_fallback(handle, new_global_step, name, ctx) -> None: ...
def accumulator_take_gradient(handle, num_required, dtype, name: Any | None = ...): ...

AccumulatorTakeGradient: Any

def accumulator_take_gradient_eager_fallback(handle, num_required, dtype, name, ctx) -> None: ...
def barrier(component_types, shapes=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

Barrier: Any

def barrier_eager_fallback(component_types, shapes, capacity, container, shared_name, name, ctx) -> None: ...
def barrier_close(handle, cancel_pending_enqueues: bool = ..., name: Any | None = ...): ...

BarrierClose: Any

def barrier_close_eager_fallback(handle, cancel_pending_enqueues, name, ctx) -> None: ...
def barrier_incomplete_size(handle, name: Any | None = ...): ...

BarrierIncompleteSize: Any

def barrier_incomplete_size_eager_fallback(handle, name, ctx) -> None: ...
def barrier_insert_many(handle, keys, values, component_index, name: Any | None = ...): ...

BarrierInsertMany: Any

def barrier_insert_many_eager_fallback(handle, keys, values, component_index, name, ctx) -> None: ...
def barrier_ready_size(handle, name: Any | None = ...): ...

BarrierReadySize: Any

def barrier_ready_size_eager_fallback(handle, name, ctx) -> None: ...

class _BarrierTakeManyOutput(NamedTuple):
    indices: Any
    keys: Any
    values: Any

def barrier_take_many(handle, num_elements, component_types, allow_small_batch: bool = ..., wait_for_incomplete: bool = ..., timeout_ms: int = ..., name: Any | None = ...): ...

BarrierTakeMany: Any

def barrier_take_many_eager_fallback(handle, num_elements, component_types, allow_small_batch, wait_for_incomplete, timeout_ms, name, ctx) -> None: ...
def conditional_accumulator(dtype, shape, container: str = ..., shared_name: str = ..., reduction_type: str = ..., name: Any | None = ...): ...

ConditionalAccumulator: Any

def conditional_accumulator_eager_fallback(dtype, shape, container, shared_name, reduction_type, name, ctx) -> None: ...
def delete_session_tensor(handle, name: Any | None = ...): ...

DeleteSessionTensor: Any

def delete_session_tensor_eager_fallback(handle, name, ctx): ...
def dynamic_partition(data, partitions, num_partitions, name: Any | None = ...): ...

DynamicPartition: Any

def dynamic_partition_eager_fallback(data, partitions, num_partitions, name, ctx): ...
def dynamic_stitch(indices, data, name: Any | None = ...): ...

DynamicStitch: Any

def dynamic_stitch_eager_fallback(indices, data, name, ctx): ...
def fifo_queue(component_types, shapes=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

FIFOQueue: Any

def fifo_queue_eager_fallback(component_types, shapes, capacity, container, shared_name, name, ctx) -> None: ...
def fifo_queue_v2(component_types, shapes=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

FIFOQueueV2: Any

def fifo_queue_v2_eager_fallback(component_types, shapes, capacity, container, shared_name, name, ctx): ...
def fake_queue(resource, name: Any | None = ...): ...

FakeQueue: Any

def fake_queue_eager_fallback(resource, name, ctx) -> None: ...
def get_session_handle(value, name: Any | None = ...): ...

GetSessionHandle: Any

def get_session_handle_eager_fallback(value, name, ctx): ...
def get_session_handle_v2(value, name: Any | None = ...): ...

GetSessionHandleV2: Any

def get_session_handle_v2_eager_fallback(value, name, ctx): ...
def get_session_tensor(handle, dtype, name: Any | None = ...): ...

GetSessionTensor: Any

def get_session_tensor_eager_fallback(handle, dtype, name, ctx): ...
def map_clear(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapClear: Any

def map_clear_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def map_incomplete_size(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapIncompleteSize: Any

def map_incomplete_size_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def map_peek(key, indices, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapPeek: Any

def map_peek_eager_fallback(key, indices, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def map_size(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapSize: Any

def map_size_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def map_stage(key, indices, values, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapStage: Any

def map_stage_eager_fallback(key, indices, values, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def map_unstage(key, indices, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapUnstage: Any

def map_unstage_eager_fallback(key, indices, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...

class _MapUnstageNoKeyOutput(NamedTuple):
    key: Any
    values: Any

def map_unstage_no_key(indices, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

MapUnstageNoKey: Any

def map_unstage_no_key_eager_fallback(indices, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def ordered_map_clear(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapClear: Any

def ordered_map_clear_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def ordered_map_incomplete_size(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapIncompleteSize: Any

def ordered_map_incomplete_size_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def ordered_map_peek(key, indices, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapPeek: Any

def ordered_map_peek_eager_fallback(key, indices, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def ordered_map_size(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapSize: Any

def ordered_map_size_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def ordered_map_stage(key, indices, values, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapStage: Any

def ordered_map_stage_eager_fallback(key, indices, values, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def ordered_map_unstage(key, indices, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapUnstage: Any

def ordered_map_unstage_eager_fallback(key, indices, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...

class _OrderedMapUnstageNoKeyOutput(NamedTuple):
    key: Any
    values: Any

def ordered_map_unstage_no_key(indices, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

OrderedMapUnstageNoKey: Any

def ordered_map_unstage_no_key_eager_fallback(indices, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def padding_fifo_queue(component_types, shapes=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

PaddingFIFOQueue: Any

def padding_fifo_queue_eager_fallback(component_types, shapes, capacity, container, shared_name, name, ctx) -> None: ...
def padding_fifo_queue_v2(component_types, shapes=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

PaddingFIFOQueueV2: Any

def padding_fifo_queue_v2_eager_fallback(component_types, shapes, capacity, container, shared_name, name, ctx): ...
def parallel_dynamic_stitch(indices, data, name: Any | None = ...): ...

ParallelDynamicStitch: Any

def parallel_dynamic_stitch_eager_fallback(indices, data, name, ctx): ...
def priority_queue(shapes, component_types=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

PriorityQueue: Any

def priority_queue_eager_fallback(shapes, component_types, capacity, container, shared_name, name, ctx) -> None: ...
def priority_queue_v2(shapes, component_types=..., capacity: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

PriorityQueueV2: Any

def priority_queue_v2_eager_fallback(shapes, component_types, capacity, container, shared_name, name, ctx): ...
def queue_close(handle, cancel_pending_enqueues: bool = ..., name: Any | None = ...): ...

QueueClose: Any

def queue_close_eager_fallback(handle, cancel_pending_enqueues, name, ctx) -> None: ...
def queue_close_v2(handle, cancel_pending_enqueues: bool = ..., name: Any | None = ...): ...

QueueCloseV2: Any

def queue_close_v2_eager_fallback(handle, cancel_pending_enqueues, name, ctx): ...
def queue_dequeue(handle, component_types, timeout_ms: int = ..., name: Any | None = ...): ...

QueueDequeue: Any

def queue_dequeue_eager_fallback(handle, component_types, timeout_ms, name, ctx) -> None: ...
def queue_dequeue_many(handle, n, component_types, timeout_ms: int = ..., name: Any | None = ...): ...

QueueDequeueMany: Any

def queue_dequeue_many_eager_fallback(handle, n, component_types, timeout_ms, name, ctx) -> None: ...
def queue_dequeue_many_v2(handle, n, component_types, timeout_ms: int = ..., name: Any | None = ...): ...

QueueDequeueManyV2: Any

def queue_dequeue_many_v2_eager_fallback(handle, n, component_types, timeout_ms, name, ctx): ...
def queue_dequeue_up_to(handle, n, component_types, timeout_ms: int = ..., name: Any | None = ...): ...

QueueDequeueUpTo: Any

def queue_dequeue_up_to_eager_fallback(handle, n, component_types, timeout_ms, name, ctx) -> None: ...
def queue_dequeue_up_to_v2(handle, n, component_types, timeout_ms: int = ..., name: Any | None = ...): ...

QueueDequeueUpToV2: Any

def queue_dequeue_up_to_v2_eager_fallback(handle, n, component_types, timeout_ms, name, ctx): ...
def queue_dequeue_v2(handle, component_types, timeout_ms: int = ..., name: Any | None = ...): ...

QueueDequeueV2: Any

def queue_dequeue_v2_eager_fallback(handle, component_types, timeout_ms, name, ctx): ...
def queue_enqueue(handle, components, timeout_ms: int = ..., name: Any | None = ...): ...

QueueEnqueue: Any

def queue_enqueue_eager_fallback(handle, components, timeout_ms, name, ctx) -> None: ...
def queue_enqueue_many(handle, components, timeout_ms: int = ..., name: Any | None = ...): ...

QueueEnqueueMany: Any

def queue_enqueue_many_eager_fallback(handle, components, timeout_ms, name, ctx) -> None: ...
def queue_enqueue_many_v2(handle, components, timeout_ms: int = ..., name: Any | None = ...): ...

QueueEnqueueManyV2: Any

def queue_enqueue_many_v2_eager_fallback(handle, components, timeout_ms, name, ctx): ...
def queue_enqueue_v2(handle, components, timeout_ms: int = ..., name: Any | None = ...): ...

QueueEnqueueV2: Any

def queue_enqueue_v2_eager_fallback(handle, components, timeout_ms, name, ctx): ...
def queue_is_closed(handle, name: Any | None = ...): ...

QueueIsClosed: Any

def queue_is_closed_eager_fallback(handle, name, ctx) -> None: ...
def queue_is_closed_v2(handle, name: Any | None = ...): ...

QueueIsClosedV2: Any

def queue_is_closed_v2_eager_fallback(handle, name, ctx): ...
def queue_size(handle, name: Any | None = ...): ...

QueueSize: Any

def queue_size_eager_fallback(handle, name, ctx) -> None: ...
def queue_size_v2(handle, name: Any | None = ...): ...

QueueSizeV2: Any

def queue_size_v2_eager_fallback(handle, name, ctx): ...
def random_shuffle_queue(component_types, shapes=..., capacity: int = ..., min_after_dequeue: int = ..., seed: int = ..., seed2: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

RandomShuffleQueue: Any

def random_shuffle_queue_eager_fallback(component_types, shapes, capacity, min_after_dequeue, seed, seed2, container, shared_name, name, ctx) -> None: ...
def random_shuffle_queue_v2(component_types, shapes=..., capacity: int = ..., min_after_dequeue: int = ..., seed: int = ..., seed2: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

RandomShuffleQueueV2: Any

def random_shuffle_queue_v2_eager_fallback(component_types, shapes, capacity, min_after_dequeue, seed, seed2, container, shared_name, name, ctx): ...
def record_input(file_pattern, file_random_seed: int = ..., file_shuffle_shift_ratio: int = ..., file_buffer_size: int = ..., file_parallelism: int = ..., batch_size: int = ..., compression_type: str = ..., name: Any | None = ...): ...

RecordInput: Any

def record_input_eager_fallback(file_pattern, file_random_seed, file_shuffle_shift_ratio, file_buffer_size, file_parallelism, batch_size, compression_type, name, ctx): ...
def resource_accumulator_apply_gradient(handle, local_step, gradient, name: Any | None = ...): ...

ResourceAccumulatorApplyGradient: Any

def resource_accumulator_apply_gradient_eager_fallback(handle, local_step, gradient, name, ctx): ...
def resource_accumulator_num_accumulated(handle, name: Any | None = ...): ...

ResourceAccumulatorNumAccumulated: Any

def resource_accumulator_num_accumulated_eager_fallback(handle, name, ctx): ...
def resource_accumulator_set_global_step(handle, new_global_step, name: Any | None = ...): ...

ResourceAccumulatorSetGlobalStep: Any

def resource_accumulator_set_global_step_eager_fallback(handle, new_global_step, name, ctx): ...
def resource_accumulator_take_gradient(handle, num_required, dtype, name: Any | None = ...): ...

ResourceAccumulatorTakeGradient: Any

def resource_accumulator_take_gradient_eager_fallback(handle, num_required, dtype, name, ctx): ...
def resource_conditional_accumulator(dtype, shape, container: str = ..., shared_name: str = ..., reduction_type: str = ..., name: Any | None = ...): ...

ResourceConditionalAccumulator: Any

def resource_conditional_accumulator_eager_fallback(dtype, shape, container, shared_name, reduction_type, name, ctx): ...
def sparse_accumulator_apply_gradient(handle, local_step, gradient_indices, gradient_values, gradient_shape, has_known_shape, name: Any | None = ...): ...

SparseAccumulatorApplyGradient: Any

def sparse_accumulator_apply_gradient_eager_fallback(handle, local_step, gradient_indices, gradient_values, gradient_shape, has_known_shape, name, ctx) -> None: ...

class _SparseAccumulatorTakeGradientOutput(NamedTuple):
    indices: Any
    values: Any
    shape: Any

def sparse_accumulator_take_gradient(handle, num_required, dtype, name: Any | None = ...): ...

SparseAccumulatorTakeGradient: Any

def sparse_accumulator_take_gradient_eager_fallback(handle, num_required, dtype, name, ctx) -> None: ...
def sparse_conditional_accumulator(dtype, shape, container: str = ..., shared_name: str = ..., reduction_type: str = ..., name: Any | None = ...): ...

SparseConditionalAccumulator: Any

def sparse_conditional_accumulator_eager_fallback(dtype, shape, container, shared_name, reduction_type, name, ctx) -> None: ...

Stack: Any

def stack_close(handle, name: Any | None = ...): ...

StackClose: Any

def stack_close_eager_fallback(handle, name, ctx) -> None: ...
def stack_close_v2(handle, name: Any | None = ...): ...

StackCloseV2: Any

def stack_close_v2_eager_fallback(handle, name, ctx): ...
def stack_pop(handle, elem_type, name: Any | None = ...): ...

StackPop: Any

def stack_pop_eager_fallback(handle, elem_type, name, ctx) -> None: ...
def stack_pop_v2(handle, elem_type, name: Any | None = ...): ...

StackPopV2: Any

def stack_pop_v2_eager_fallback(handle, elem_type, name, ctx): ...
def stack_push(handle, elem, swap_memory: bool = ..., name: Any | None = ...): ...

StackPush: Any

def stack_push_eager_fallback(handle, elem, swap_memory, name, ctx) -> None: ...
def stack_push_v2(handle, elem, swap_memory: bool = ..., name: Any | None = ...): ...

StackPushV2: Any

def stack_push_v2_eager_fallback(handle, elem, swap_memory, name, ctx): ...
def stack_v2(max_size, elem_type, stack_name: str = ..., name: Any | None = ...): ...

StackV2: Any

def stack_v2_eager_fallback(max_size, elem_type, stack_name, name, ctx): ...
def stage(values, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

Stage: Any

def stage_eager_fallback(values, capacity, memory_limit, container, shared_name, name, ctx): ...
def stage_clear(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

StageClear: Any

def stage_clear_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def stage_peek(index, dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

StagePeek: Any

def stage_peek_eager_fallback(index, dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def stage_size(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

StageSize: Any

def stage_size_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
def tensor_array(size, dtype, dynamic_size: bool = ..., clear_after_read: bool = ..., tensor_array_name: str = ..., element_shape: Any | None = ..., name: Any | None = ...): ...

TensorArray: Any

def tensor_array_eager_fallback(size, dtype, dynamic_size, clear_after_read, tensor_array_name, element_shape, name, ctx) -> None: ...
def tensor_array_close(handle, name: Any | None = ...): ...

TensorArrayClose: Any

def tensor_array_close_eager_fallback(handle, name, ctx) -> None: ...
def tensor_array_close_v2(handle, name: Any | None = ...): ...

TensorArrayCloseV2: Any

def tensor_array_close_v2_eager_fallback(handle, name, ctx): ...
def tensor_array_close_v3(handle, name: Any | None = ...): ...

TensorArrayCloseV3: Any

def tensor_array_close_v3_eager_fallback(handle, name, ctx): ...

class _TensorArrayConcatOutput(NamedTuple):
    value: Any
    lengths: Any

def tensor_array_concat(handle, flow_in, dtype, element_shape_except0: Any | None = ..., name: Any | None = ...): ...

TensorArrayConcat: Any

def tensor_array_concat_eager_fallback(handle, flow_in, dtype, element_shape_except0, name, ctx) -> None: ...

class _TensorArrayConcatV2Output(NamedTuple):
    value: Any
    lengths: Any

def tensor_array_concat_v2(handle, flow_in, dtype, element_shape_except0: Any | None = ..., name: Any | None = ...): ...

TensorArrayConcatV2: Any

def tensor_array_concat_v2_eager_fallback(handle, flow_in, dtype, element_shape_except0, name, ctx): ...

class _TensorArrayConcatV3Output(NamedTuple):
    value: Any
    lengths: Any

def tensor_array_concat_v3(handle, flow_in, dtype, element_shape_except0: Any | None = ..., name: Any | None = ...): ...

TensorArrayConcatV3: Any

def tensor_array_concat_v3_eager_fallback(handle, flow_in, dtype, element_shape_except0, name, ctx): ...
def tensor_array_gather(handle, indices, flow_in, dtype, element_shape: Any | None = ..., name: Any | None = ...): ...

TensorArrayGather: Any

def tensor_array_gather_eager_fallback(handle, indices, flow_in, dtype, element_shape, name, ctx) -> None: ...
def tensor_array_gather_v2(handle, indices, flow_in, dtype, element_shape: Any | None = ..., name: Any | None = ...): ...

TensorArrayGatherV2: Any

def tensor_array_gather_v2_eager_fallback(handle, indices, flow_in, dtype, element_shape, name, ctx): ...
def tensor_array_gather_v3(handle, indices, flow_in, dtype, element_shape: Any | None = ..., name: Any | None = ...): ...

TensorArrayGatherV3: Any

def tensor_array_gather_v3_eager_fallback(handle, indices, flow_in, dtype, element_shape, name, ctx): ...
def tensor_array_grad(handle, flow_in, source, name: Any | None = ...): ...

TensorArrayGrad: Any

def tensor_array_grad_eager_fallback(handle, flow_in, source, name, ctx) -> None: ...
def tensor_array_grad_v2(handle, flow_in, source, name: Any | None = ...): ...

TensorArrayGradV2: Any

def tensor_array_grad_v2_eager_fallback(handle, flow_in, source, name, ctx): ...

class _TensorArrayGradV3Output(NamedTuple):
    grad_handle: Any
    flow_out: Any

def tensor_array_grad_v3(handle, flow_in, source, name: Any | None = ...): ...

TensorArrayGradV3: Any

def tensor_array_grad_v3_eager_fallback(handle, flow_in, source, name, ctx): ...

class _TensorArrayGradWithShapeOutput(NamedTuple):
    grad_handle: Any
    flow_out: Any

def tensor_array_grad_with_shape(handle, flow_in, shape_to_prepend, source, name: Any | None = ...): ...

TensorArrayGradWithShape: Any

def tensor_array_grad_with_shape_eager_fallback(handle, flow_in, shape_to_prepend, source, name, ctx): ...
def tensor_array_pack(handle, flow_in, dtype, element_shape: Any | None = ..., name: Any | None = ...): ...

TensorArrayPack: Any

def tensor_array_pack_eager_fallback(handle, flow_in, dtype, element_shape, name, ctx) -> None: ...
def tensor_array_read(handle, index, flow_in, dtype, name: Any | None = ...): ...

TensorArrayRead: Any

def tensor_array_read_eager_fallback(handle, index, flow_in, dtype, name, ctx) -> None: ...
def tensor_array_read_v2(handle, index, flow_in, dtype, name: Any | None = ...): ...

TensorArrayReadV2: Any

def tensor_array_read_v2_eager_fallback(handle, index, flow_in, dtype, name, ctx): ...
def tensor_array_read_v3(handle, index, flow_in, dtype, name: Any | None = ...): ...

TensorArrayReadV3: Any

def tensor_array_read_v3_eager_fallback(handle, index, flow_in, dtype, name, ctx): ...
def tensor_array_scatter(handle, indices, value, flow_in, name: Any | None = ...): ...

TensorArrayScatter: Any

def tensor_array_scatter_eager_fallback(handle, indices, value, flow_in, name, ctx) -> None: ...
def tensor_array_scatter_v2(handle, indices, value, flow_in, name: Any | None = ...): ...

TensorArrayScatterV2: Any

def tensor_array_scatter_v2_eager_fallback(handle, indices, value, flow_in, name, ctx): ...
def tensor_array_scatter_v3(handle, indices, value, flow_in, name: Any | None = ...): ...

TensorArrayScatterV3: Any

def tensor_array_scatter_v3_eager_fallback(handle, indices, value, flow_in, name, ctx): ...
def tensor_array_size(handle, flow_in, name: Any | None = ...): ...

TensorArraySize: Any

def tensor_array_size_eager_fallback(handle, flow_in, name, ctx) -> None: ...
def tensor_array_size_v2(handle, flow_in, name: Any | None = ...): ...

TensorArraySizeV2: Any

def tensor_array_size_v2_eager_fallback(handle, flow_in, name, ctx): ...
def tensor_array_size_v3(handle, flow_in, name: Any | None = ...): ...

TensorArraySizeV3: Any

def tensor_array_size_v3_eager_fallback(handle, flow_in, name, ctx): ...
def tensor_array_split(handle, value, lengths, flow_in, name: Any | None = ...): ...

TensorArraySplit: Any

def tensor_array_split_eager_fallback(handle, value, lengths, flow_in, name, ctx) -> None: ...
def tensor_array_split_v2(handle, value, lengths, flow_in, name: Any | None = ...): ...

TensorArraySplitV2: Any

def tensor_array_split_v2_eager_fallback(handle, value, lengths, flow_in, name, ctx): ...
def tensor_array_split_v3(handle, value, lengths, flow_in, name: Any | None = ...): ...

TensorArraySplitV3: Any

def tensor_array_split_v3_eager_fallback(handle, value, lengths, flow_in, name, ctx): ...
def tensor_array_unpack(handle, value, flow_in, name: Any | None = ...): ...

TensorArrayUnpack: Any

def tensor_array_unpack_eager_fallback(handle, value, flow_in, name, ctx) -> None: ...
def tensor_array_v2(size, dtype, element_shape: Any | None = ..., dynamic_size: bool = ..., clear_after_read: bool = ..., tensor_array_name: str = ..., name: Any | None = ...): ...

TensorArrayV2: Any

def tensor_array_v2_eager_fallback(size, dtype, element_shape, dynamic_size, clear_after_read, tensor_array_name, name, ctx): ...

class _TensorArrayV3Output(NamedTuple):
    handle: Any
    flow: Any

def tensor_array_v3(size, dtype, element_shape: Any | None = ..., dynamic_size: bool = ..., clear_after_read: bool = ..., identical_element_shapes: bool = ..., tensor_array_name: str = ..., name: Any | None = ...): ...

TensorArrayV3: Any

def tensor_array_v3_eager_fallback(size, dtype, element_shape, dynamic_size, clear_after_read, identical_element_shapes, tensor_array_name, name, ctx): ...
def tensor_array_write(handle, index, value, flow_in, name: Any | None = ...): ...

TensorArrayWrite: Any

def tensor_array_write_eager_fallback(handle, index, value, flow_in, name, ctx) -> None: ...
def tensor_array_write_v2(handle, index, value, flow_in, name: Any | None = ...): ...

TensorArrayWriteV2: Any

def tensor_array_write_v2_eager_fallback(handle, index, value, flow_in, name, ctx): ...
def tensor_array_write_v3(handle, index, value, flow_in, name: Any | None = ...): ...

TensorArrayWriteV3: Any

def tensor_array_write_v3_eager_fallback(handle, index, value, flow_in, name, ctx): ...
def unstage(dtypes, capacity: int = ..., memory_limit: int = ..., container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

Unstage: Any

def unstage_eager_fallback(dtypes, capacity, memory_limit, container, shared_name, name, ctx): ...
