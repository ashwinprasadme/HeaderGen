from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, errors as errors, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, functional_ops as functional_ops, gen_dataset_ops as gen_dataset_ops, resource_variable_ops as resource_variable_ops
from typing import Any

class _PerDeviceGenerator(dataset_ops.DatasetV2):
    def __init__(self, shard_num, multi_device_iterator_resource, incarnation_id, source_device, element_spec): ...
    @property
    def element_spec(self): ...

class _ReincarnatedPerDeviceGenerator(dataset_ops.DatasetV2):
    def __init__(self, per_device_dataset, incarnation_id) -> None: ...
    @property
    def element_spec(self): ...

class MultiDeviceIterator:
    def __init__(self, dataset, devices, max_buffer_size: int = ..., prefetch_buffer_size: int = ..., source_device: str = ...) -> None: ...
    def get_next(self, device: Any | None = ...): ...
    def get_next_as_optional(self): ...
    @property
    def initializer(self): ...
    @property
    def element_spec(self): ...

class MultiDeviceIteratorResourceDeleter:
    def __init__(self, multi_device_iterator, iterators, device, deleter) -> None: ...
    def __del__(self) -> None: ...

class MultiDeviceIteratorSpec(type_spec.TypeSpec):
    def __init__(self, devices, source_device, element_spec) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class OwnedMultiDeviceIterator(composite_tensor.CompositeTensor):
    def __init__(self, dataset: Any | None = ..., devices: Any | None = ..., max_buffer_size: int = ..., prefetch_buffer_size: int = ..., source_device: str = ..., components: Any | None = ..., element_spec: Any | None = ...) -> None: ...
    def get_next(self, device: Any | None = ...): ...
    def __iter__(self): ...
    def next(self): ...
    def __next__(self): ...
    def get_next_as_optional(self): ...
    @property
    def element_spec(self): ...