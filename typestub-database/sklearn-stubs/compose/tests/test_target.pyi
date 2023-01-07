from sklearn import datasets as datasets
from sklearn.base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin, clone as clone
from sklearn.compose import TransformedTargetRegressor as TransformedTargetRegressor
from sklearn.dummy import DummyRegressor as DummyRegressor
from sklearn.linear_model import LinearRegression as LinearRegression, OrthogonalMatchingPursuit as OrthogonalMatchingPursuit
from sklearn.pipeline import Pipeline as Pipeline
from sklearn.preprocessing import FunctionTransformer as FunctionTransformer, StandardScaler as StandardScaler
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_no_warnings as assert_no_warnings
from typing import Any

friedman: Any

def test_transform_target_regressor_error() -> None: ...
def test_transform_target_regressor_invertible() -> None: ...
def test_transform_target_regressor_functions() -> None: ...
def test_transform_target_regressor_functions_multioutput() -> None: ...
def test_transform_target_regressor_1d_transformer(X, y): ...
def test_transform_target_regressor_2d_transformer(X, y) -> None: ...
def test_transform_target_regressor_2d_transformer_multioutput() -> None: ...
def test_transform_target_regressor_3d_target(): ...
def test_transform_target_regressor_multi_to_single(): ...

class DummyCheckerArrayTransformer(TransformerMixin, BaseEstimator):
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...

class DummyCheckerListRegressor(DummyRegressor):
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...

def test_transform_target_regressor_ensure_y_array() -> None: ...

class DummyTransformer(TransformerMixin, BaseEstimator):
    fit_counter: Any
    def __init__(self, fit_counter: int = ...) -> None: ...
    def fit(self, X, y: Any | None = ...): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...

def test_transform_target_regressor_count_fit(check_inverse) -> None: ...

class DummyRegressorWithExtraFitParams(DummyRegressor):
    def fit(self, X, y, sample_weight: Any | None = ..., check_input: bool = ...): ...

def test_transform_target_regressor_pass_fit_parameters() -> None: ...
def test_transform_target_regressor_route_pipeline() -> None: ...

class DummyRegressorWithExtraPredictParams(DummyRegressor):
    predict_called: bool
    def predict(self, X, check_input: bool = ...): ...

def test_transform_target_regressor_pass_extra_predict_parameters() -> None: ...