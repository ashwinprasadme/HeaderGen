from tensorflow.python.keras.utils.io_utils import path_to_string as path_to_string
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export

def check_pydot(): ...
def is_wrapped_model(layer): ...
def add_edge(dot, src, dst) -> None: ...
def model_to_dot(model, show_shapes: bool = ..., show_dtype: bool = ..., show_layer_names: bool = ..., rankdir: str = ..., expand_nested: bool = ..., dpi: int = ..., subgraph: bool = ...): ...
def plot_model(model, to_file: str = ..., show_shapes: bool = ..., show_dtype: bool = ..., show_layer_names: bool = ..., rankdir: str = ..., expand_nested: bool = ..., dpi: int = ...): ...
