import keras
from keras import backend as backend, testing_utils as testing_utils
from keras.distribute import keras_correctness_test_base as keras_correctness_test_base, strategy_combinations as strategy_combinations
from typing import Any

def all_strategy_combinations_with_eager_and_graph_modes(): ...
def all_strategy_combinations_with_graph_mode(): ...
def is_default_strategy(strategy): ...

class TestDistributionStrategyDnnCorrectness(keras_correctness_test_base.TestDistributionStrategyCorrectnessBase):
    def get_model(self, initial_weights: Any | None = ..., distribution: Any | None = ..., input_shapes: Any | None = ...): ...
    def get_data(self): ...
    def get_data_with_partial_last_batch(self): ...
    def get_data_with_partial_last_batch_eval(self): ...
    def test_dnn_correctness(self, distribution, use_numpy, use_validation_data) -> None: ...
    def test_dnn_correctness_with_partial_last_batch_eval(self, distribution, use_numpy, use_validation_data) -> None: ...
    def test_dnn_correctness_with_partial_last_batch(self, distribution, use_numpy, use_validation_data) -> None: ...
    def test_dnn_with_dynamic_learning_rate(self, distribution) -> None: ...

class TestDistributionStrategyDnnMetricCorrectness(keras_correctness_test_base.TestDistributionStrategyCorrectnessBase):
    def get_model(self, distribution: Any | None = ..., input_shapes: Any | None = ...): ...
    def run_metric_correctness_test(self, distribution) -> None: ...
    def test_simple_dnn_metric_correctness(self, distribution) -> None: ...

class TestDistributionStrategyDnnMetricEvalCorrectness(keras_correctness_test_base.TestDistributionStrategyCorrectnessBase):
    def get_model(self, distribution: Any | None = ..., input_shapes: Any | None = ...): ...
    def run_eval_metrics_correctness_test(self, distribution) -> None: ...
    def test_identity_model_metric_eval_correctness(self, distribution) -> None: ...

class SubclassedModel(keras.Model):
    dense1: Any
    dense2: Any
    dense3: Any
    dense4: Any
    def __init__(self, initial_weights, input_shapes) -> None: ...
    def call(self, inputs): ...

class TestDistributionStrategyDnnCorrectnessWithSubclassedModel(TestDistributionStrategyDnnCorrectness):
    def get_model(self, initial_weights: Any | None = ..., distribution: Any | None = ..., input_shapes: Any | None = ...): ...
    def test_dnn_correctness(self, distribution, use_numpy, use_validation_data) -> None: ...
    def test_dnn_with_dynamic_learning_rate(self, distribution) -> None: ...
    def test_dnn_correctness_with_partial_last_batch_eval(self, distribution, use_numpy, use_validation_data) -> None: ...