from tensorflow.python.autograph.pyct import errors as errors, inspect_utils as inspect_utils
from tensorflow.python.util import tf_inspect as tf_inspect
from typing import Any

PY2_PREAMBLE: Any
PY3_PREAMBLE: str
MAX_SIZE: int
STANDARD_PREAMBLE = PY3_PREAMBLE
STANDARD_PREAMBLE_LEN: Any

def dedent_block(code_string): ...
def parse_entity(entity, future_features): ...
def parse(src, preamble_len: int = ..., single_node: bool = ...): ...
def parse_expression(src): ...
def unparse(node, indentation: Any | None = ..., include_encoding_marker: bool = ...): ...
