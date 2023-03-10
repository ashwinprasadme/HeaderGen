from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def is_namedtuple(instance, strict: bool = ...): ...
def is_attrs(obj): ...
def is_mapping(obj): ...

is_sequence: Any
is_sequence_or_composite: Any

def is_nested(seq): ...
def flatten(structure, expand_composites: bool = ...): ...

same_namedtuples: Any

class _DotString: ...

def assert_same_structure(nest1, nest2, check_types: bool = ..., expand_composites: bool = ...): ...
def flatten_dict_items(dictionary): ...
def pack_sequence_as(structure, flat_sequence, expand_composites: bool = ...): ...
def map_structure(func, *structure, **kwargs): ...
def map_structure_with_paths(func, *structure, **kwargs): ...
def map_structure_with_tuple_paths(func, *structure, **kwargs): ...
def assert_shallow_structure(shallow_tree, input_tree, check_types: bool = ..., expand_composites: bool = ...) -> None: ...
def flatten_up_to(shallow_tree, input_tree, check_types: bool = ..., expand_composites: bool = ...): ...
def flatten_with_tuple_paths_up_to(shallow_tree, input_tree, check_types: bool = ..., expand_composites: bool = ...): ...
def map_structure_up_to(shallow_tree, func, *inputs, **kwargs): ...
def map_structure_with_tuple_paths_up_to(shallow_tree, func, *inputs, **kwargs): ...
def get_traverse_shallow_structure(traverse_fn, structure, expand_composites: bool = ...): ...
def yield_flat_paths(nest, expand_composites: bool = ...) -> None: ...
def flatten_with_joined_string_paths(structure, separator: str = ..., expand_composites: bool = ...): ...
def flatten_with_tuple_paths(structure, expand_composites: bool = ...): ...
def list_to_tuple(structure): ...
