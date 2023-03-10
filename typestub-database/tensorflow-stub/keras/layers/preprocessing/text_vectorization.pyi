from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_preprocessing_layer as base_preprocessing_layer
from tensorflow.python.keras.layers.preprocessing import index_lookup as index_lookup, string_lookup as string_lookup
from tensorflow.python.keras.utils import layer_utils as layer_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, gen_string_ops as gen_string_ops, string_ops as string_ops
from tensorflow.python.ops.ragged import ragged_functional_ops as ragged_functional_ops, ragged_string_ops as ragged_string_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

LOWER_AND_STRIP_PUNCTUATION: str
SPLIT_ON_WHITESPACE: str
TF_IDF: Any
INT: Any
MULTI_HOT: Any
COUNT: Any
DEFAULT_STRIP_REGEX: str

class TextVectorization(base_preprocessing_layer.CombinerPreprocessingLayer):
    def __init__(self, max_tokens: Any | None = ..., standardize=..., split=..., ngrams: Any | None = ..., output_mode=..., output_sequence_length: Any | None = ..., pad_to_max_tokens: bool = ..., vocabulary: Any | None = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def adapt(self, data, reset_state: bool = ...): ...
    def get_vocabulary(self, include_special_tokens: bool = ...): ...
    def vocabulary_size(self): ...
    def get_config(self): ...
    def count_params(self): ...
    def set_vocabulary(self, vocabulary, idf_weights: Any | None = ...) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
