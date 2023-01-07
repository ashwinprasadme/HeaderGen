from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, confusion_matrix as confusion_matrix, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.util import tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def squeeze_or_expand_dimensions(y_pred, y_true: Any | None = ..., sample_weight: Any | None = ...): ...
def scale_losses_by_sample_weight(losses, sample_weight): ...
def check_per_example_loss_rank(per_example_loss) -> None: ...
def add_loss(loss, loss_collection=...) -> None: ...
def get_losses(scope: Any | None = ..., loss_collection=...): ...
def get_regularization_losses(scope: Any | None = ...): ...
def get_regularization_loss(scope: Any | None = ..., name: str = ...): ...
def get_total_loss(add_regularization_losses: bool = ..., name: str = ..., scope: Any | None = ...): ...