from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops, variables as variables
from tensorflow.python.saved_model import save_context as save_context
from tensorflow.python.training.saving import saveable_object as saveable_object
from tensorflow.python.util import nest as nest, object_identity as object_identity
from typing import Any

def set_cpu0(device_string): ...

class ReferenceVariableSaveable(saveable_object.SaveableObject):
    def __init__(self, var, slice_spec, name) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

class ResourceVariableSaveable(saveable_object.SaveableObject):
    handle_op: Any
    def __init__(self, var, slice_spec, name): ...
    def restore(self, restored_tensors, restored_shapes): ...

def create_saveables_from_factory(saveable_factory, checkpoint_key, call_with_mapped_captures: Any | None = ..., use_graph_element_for_variables: bool = ...): ...
def saveable_objects_for_op(op, name, use_graph_element_for_variables: bool = ...) -> None: ...
def op_list_to_dict(op_list, convert_variable_to_tensor: bool = ...): ...
def validate_and_slice_inputs(names_to_saveables): ...
def build_traceable_saveable(saveable_factory, checkpoint_key, obj): ...
def validate_saveables_for_saved_model(saveables, obj): ...

class RestoredSaveableObject(saveable_object.SaveableObject):
    save_function: Any
    restore_function: Any
    def __init__(self, save_function, restore_function, name) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

def restored_saved_object_factory(save_function, restore_function): ...
def create_saveable_object(factory, name, call_with_mapped_captures): ...
def is_factory_for_restored_saveable_object(factory): ...
