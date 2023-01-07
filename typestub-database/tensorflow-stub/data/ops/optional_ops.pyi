import abc
from tensorflow.python.data.util import structure as structure
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class Optional(composite_tensor.CompositeTensor, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def has_value(self, name: Any | None = ...): ...
    @abc.abstractmethod
    def get_value(self, name: Any | None = ...): ...
    @property
    @abc.abstractmethod
    def element_spec(self): ...
    @staticmethod
    def empty(element_spec): ...
    @staticmethod
    def from_value(value): ...

class _OptionalImpl(Optional):
    def __init__(self, variant_tensor, element_spec) -> None: ...
    def has_value(self, name: Any | None = ...): ...
    def get_value(self, name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class OptionalSpec(type_spec.TypeSpec):
    def __init__(self, element_spec) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...