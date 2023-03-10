from tensorflow.python import keras as keras
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.keras.layers.preprocessing import string_lookup as string_lookup
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.platform import test as test
from typing import Any

class DistributeKplTestUtils(test.TestCase):
    FEATURE_VOCAB: Any
    LABEL_VOCAB: Any
    def define_kpls_for_training(self, use_adapt): ...
    def dataset_fn(self, feature_mapper, label_mapper): ...
    def define_model(self): ...
    def define_reverse_lookup_layer(self): ...
    def create_serving_signature(self, model, feature_mapper, label_inverse_lookup_layer): ...
    def test_save_load_serving_model(self, model, feature_mapper, label_inverse_lookup_layer) -> None: ...
