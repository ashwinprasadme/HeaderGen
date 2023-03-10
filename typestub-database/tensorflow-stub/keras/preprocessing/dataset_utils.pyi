from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from typing import Any

def index_directory(directory, labels, formats, class_names: Any | None = ..., shuffle: bool = ..., seed: Any | None = ..., follow_links: bool = ...): ...
def iter_valid_files(directory, follow_links, formats): ...
def index_subdirectory(directory, class_indices, follow_links, formats): ...
def get_training_or_validation_split(samples, labels, validation_split, subset): ...
def labels_to_dataset(labels, label_mode, num_classes): ...
def check_validation_split_arg(validation_split, subset, shuffle, seed) -> None: ...
