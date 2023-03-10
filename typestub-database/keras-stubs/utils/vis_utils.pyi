from keras import activations as activations
from keras.utils import io_utils as io_utils
from typing import Any

def check_pydot(): ...
def is_wrapped_model(layer): ...
def add_edge(dot, src, dst) -> None: ...
def get_layer_index_bound_by_layer_name(model, layer_names): ...
def model_to_dot(model, show_shapes: bool = ..., show_dtype: bool = ..., show_layer_names: bool = ..., rankdir: str = ..., expand_nested: bool = ..., dpi: int = ..., subgraph: bool = ..., layer_range: Any | None = ..., show_layer_activations: bool = ...): ...
def plot_model(model, to_file: str = ..., show_shapes: bool = ..., show_dtype: bool = ..., show_layer_names: bool = ..., rankdir: str = ..., expand_nested: bool = ..., dpi: int = ..., layer_range: Any | None = ..., show_layer_activations: bool = ...): ...
