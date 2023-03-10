import keras
import tensorflow.compat.v2 as tf
from absl.testing import parameterized
from keras.distribute import distributed_training_utils as distributed_training_utils
from keras.distribute.strategy_combinations import all_strategies as all_strategies, multi_worker_mirrored_strategies as multi_worker_mirrored_strategies, strategies_minus_tpu as strategies_minus_tpu
from keras.mixed_precision import policy as policy
from keras.preprocessing import sequence as sequence
from typing import Any

def eager_mode_test_configuration(): ...
def graph_mode_test_configuration(): ...
def all_strategy_and_input_config_combinations(): ...
def all_strategy_and_input_config_combinations_eager(): ...
def strategy_minus_tpu_and_input_config_combinations_eager(): ...
def strategies_for_embedding_models(): ...
def test_combinations_for_embedding_model(): ...
def test_combinations_with_tpu_strategies_graph(): ...
def multi_worker_mirrored_eager(): ...
def multi_worker_mirrored_eager_and_graph(): ...

class MaybeDistributionScope:
    def __init__(self, distribution) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, value, traceback) -> None: ...

def batch_wrapper(dataset, batch_size, repeat: Any | None = ...): ...
def get_batch_size(global_batch_size, distribution): ...
def get_data_size(data): ...
def get_shapes(data): ...
def get_correctness_test_inputs(use_numpy, use_validation_data, with_distribution, x_train, y_train, x_eval, y_eval, x_predict, training_epochs): ...
def fit_eval_and_predict(initial_weights, input_fn, model_fn, distribution: Any | None = ..., is_stateful_model: bool = ...): ...
def compare_results(results_with_ds, results_without_ds, distribution, testcase, partial_last_batch: Any | None = ...): ...
def should_skip_tpu_with_eager(distribution): ...

class LearningRateBatchScheduler(keras.callbacks.Callback):
    def __init__(self, update_freq: Any | None = ...) -> None: ...
    def on_batch_begin(self, batch, logs: Any | None = ...) -> None: ...

class TestDistributionStrategyCorrectnessBase(tf.test.TestCase, parameterized.TestCase):
    use_numpy: Any
    use_validation_data: Any
    with_batch_norm: Any
    def set_up_test_config(self, use_numpy: bool = ..., use_validation_data: bool = ..., with_batch_norm: Any | None = ...) -> None: ...
    def get_data(self): ...
    def get_data_with_partial_last_batch(self) -> None: ...
    def get_data_with_partial_last_batch_eval(self) -> None: ...
    def get_input_for_correctness_test(self, **kwargs): ...
    def get_model(self, distribution: Any | None = ..., input_shapes: Any | None = ...) -> None: ...
    def run_correctness_test(self, distribution, use_numpy, use_validation_data, with_batch_norm: Any | None = ..., is_stateful_model: bool = ..., partial_last_batch: Any | None = ..., training_epochs: int = ...) -> None: ...
    def get_input_for_dynamic_lr_test(self, **kwargs): ...
    def run_dynamic_lr_test(self, distribution) -> None: ...

class TestDistributionStrategyEmbeddingModelCorrectnessBase(TestDistributionStrategyCorrectnessBase):
    def get_data(self, count=..., min_words: int = ..., max_words: int = ..., max_word_id: int = ..., num_classes: int = ...): ...
