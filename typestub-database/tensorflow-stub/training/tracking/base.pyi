import abc
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.training.saving import saveable_object as saveable_object
from tensorflow.python.util import tf_contextlib as tf_contextlib, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

OBJECT_GRAPH_PROTO_KEY: str
VARIABLE_VALUE_KEY: str
OBJECT_CONFIG_JSON_KEY: str

class TrackableReference: ...

class ShardInfo(NamedTuple):
    shape: Any
    offset: Any

class CheckpointInitialValueCallable:
    def __init__(self, checkpoint_position) -> None: ...
    @property
    def checkpoint_position(self): ...
    def __call__(self, shape: Any | None = ..., dtype: Any | None = ..., shard_info: Any | None = ...): ...
    @property
    def restore_uid(self): ...

class CheckpointInitialValue(ops.Tensor):
    wrapped_value: Any
    def __init__(self, checkpoint_position, shape: Any | None = ..., shard_info: Any | None = ...) -> None: ...
    def __getattr__(self, attr): ...
    @property
    def checkpoint_position(self): ...

class NoRestoreSaveable(saveable_object.SaveableObject):
    def __init__(self, tensor, name, dtype: Any | None = ..., device: Any | None = ...) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

class PythonStateSaveable(saveable_object.SaveableObject, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def feed_dict_additions(self): ...
    @abc.abstractmethod
    def freeze(self): ...

class PythonStringStateSaveable(PythonStateSaveable):
    def __init__(self, name, state_callback, restore_callback: Any | None = ...): ...
    @property
    def optional_restore(self): ...
    def feed_dict_additions(self): ...
    def freeze(self): ...
    def python_restore(self, restored_strings) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

class CheckpointPosition:
    def __init__(self, checkpoint, proto_id) -> None: ...
    def restore(self, trackable) -> None: ...
    def bind_object(self, trackable): ...
    def is_simple_variable(self): ...
    def value_tensors(self, shape_and_slices: Any | None = ...): ...
    def gather_ops_or_named_saveables(self): ...
    def restore_ops(self): ...
    @property
    def checkpoint(self): ...
    @property
    def trackable(self): ...
    @property
    def object_proto(self): ...
    @property
    def restore_uid(self): ...
    def value_shape(self): ...

class _DeferredSlotVariableRestoration(NamedTuple):
    original_variable: Any
    slot_variable_id: Any
    slot_name: Any

class _SlotVariableRestoration(NamedTuple):
    optimizer_id: Any
    slot_variable_id: Any
    slot_name: Any

def no_automatic_dependency_tracking(method): ...
def no_manual_dependency_tracking_scope(obj) -> None: ...
def no_automatic_dependency_tracking_scope(obj) -> None: ...

class Trackable: ...
