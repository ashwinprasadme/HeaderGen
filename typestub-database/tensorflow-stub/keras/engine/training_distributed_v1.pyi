from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context, input_lib as input_lib
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, errors as errors, ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import training_arrays_v1 as training_arrays_v1, training_utils_v1 as training_utils_v1
from tensorflow.python.keras.utils.generic_utils import Progbar as Progbar
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from typing import Any

def experimental_tpu_fit_loop(model, dataset, epochs: int = ..., verbose: int = ..., callbacks: Any | None = ..., initial_epoch: int = ..., steps_per_epoch: Any | None = ..., val_dataset: Any | None = ..., validation_steps: Any | None = ..., validation_freq: int = ...): ...
def experimental_tpu_test_loop(model, dataset, verbose: int = ..., steps: Any | None = ..., callbacks: Any | None = ...): ...
def experimental_tpu_predict_loop(model, dataset, verbose: int = ..., steps: Any | None = ..., callbacks: Any | None = ...): ...

class DistributionSingleWorkerTrainingLoop(training_utils_v1.TrainingLoop):
    def fit(self, model, x: Any | None = ..., y: Any | None = ..., batch_size: Any | None = ..., epochs: int = ..., verbose: int = ..., callbacks: Any | None = ..., validation_split: float = ..., validation_data: Any | None = ..., shuffle: bool = ..., class_weight: Any | None = ..., sample_weight: Any | None = ..., initial_epoch: int = ..., steps_per_epoch: Any | None = ..., validation_steps: Any | None = ..., validation_freq: int = ..., **kwargs): ...
    def evaluate(self, model, x: Any | None = ..., y: Any | None = ..., batch_size: Any | None = ..., verbose: int = ..., sample_weight: Any | None = ..., steps: Any | None = ..., callbacks: Any | None = ..., **kwargs): ...
    def predict(self, model, x, batch_size: Any | None = ..., verbose: int = ..., steps: Any | None = ..., callbacks: Any | None = ..., **kwargs): ...

class DistributionMultiWorkerTrainingLoop(training_utils_v1.TrainingLoop):
    def __init__(self, single_worker_loop) -> None: ...
    def fit(self, *args, **kwargs): ...
    def evaluate(self, *args, **kwargs): ...
    def predict(self, *args, **kwargs): ...
