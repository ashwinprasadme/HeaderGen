from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def collective_all_to_all_v3(input, communicator, group_assignment, timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveAllToAllV3: Any

def collective_all_to_all_v3_eager_fallback(input, communicator, group_assignment, timeout_seconds, name, ctx): ...
def collective_bcast_recv(T, group_size, group_key, instance_key, shape, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveBcastRecv: Any

def collective_bcast_recv_eager_fallback(T, group_size, group_key, instance_key, shape, communication_hint, timeout_seconds, name, ctx): ...
def collective_bcast_recv_v2(group_size, group_key, instance_key, shape, T, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveBcastRecvV2: Any

def collective_bcast_recv_v2_eager_fallback(group_size, group_key, instance_key, shape, T, communication_hint, timeout_seconds, name, ctx): ...
def collective_bcast_send(input, group_size, group_key, instance_key, shape, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveBcastSend: Any

def collective_bcast_send_eager_fallback(input, group_size, group_key, instance_key, shape, communication_hint, timeout_seconds, name, ctx): ...
def collective_bcast_send_v2(input, group_size, group_key, instance_key, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveBcastSendV2: Any

def collective_bcast_send_v2_eager_fallback(input, group_size, group_key, instance_key, communication_hint, timeout_seconds, name, ctx): ...
def collective_gather(input, group_size, group_key, instance_key, shape, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveGather: Any

def collective_gather_eager_fallback(input, group_size, group_key, instance_key, shape, communication_hint, timeout_seconds, name, ctx): ...
def collective_gather_v2(input, group_size, group_key, instance_key, ordering_token, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveGatherV2: Any

def collective_gather_v2_eager_fallback(input, group_size, group_key, instance_key, ordering_token, communication_hint, timeout_seconds, name, ctx): ...
def collective_initialize_communicator(group_key, rank, group_size, communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveInitializeCommunicator: Any

def collective_initialize_communicator_eager_fallback(group_key, rank, group_size, communication_hint, timeout_seconds, name, ctx): ...
def collective_reduce(input, group_size, group_key, instance_key, merge_op, final_op, subdiv_offsets, wait_for=..., communication_hint: str = ..., timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveReduce: Any

def collective_reduce_eager_fallback(input, group_size, group_key, instance_key, merge_op, final_op, subdiv_offsets, wait_for, communication_hint, timeout_seconds, name, ctx): ...
def collective_reduce_v2(input, group_size, group_key, instance_key, ordering_token, merge_op, final_op, communication_hint: str = ..., timeout_seconds: int = ..., max_subdivs_per_device: int = ..., name: Any | None = ...): ...

CollectiveReduceV2: Any

def collective_reduce_v2_eager_fallback(input, group_size, group_key, instance_key, ordering_token, merge_op, final_op, communication_hint, timeout_seconds, max_subdivs_per_device, name, ctx): ...
def collective_reduce_v3(input, communicator, group_assignment, reduction, timeout_seconds: int = ..., name: Any | None = ...): ...

CollectiveReduceV3: Any

def collective_reduce_v3_eager_fallback(input, communicator, group_assignment, reduction, timeout_seconds, name, ctx): ...