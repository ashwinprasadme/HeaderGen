from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def as_bytes(bytes_or_text, encoding: str = ...): ...
def as_text(bytes_or_text, encoding: str = ...): ...
def as_str(bytes_or_text, encoding: str = ...): ...
def as_str_any(value): ...
def path_to_str(path): ...
def path_to_bytes(path): ...

integral_types: Any
real_types: Any
complex_types: Any
bytes_or_text_types: Any
