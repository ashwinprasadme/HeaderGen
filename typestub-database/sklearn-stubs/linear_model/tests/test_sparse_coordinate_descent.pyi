from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model import ElasticNet as ElasticNet, ElasticNetCV as ElasticNetCV, Lasso as Lasso, LassoCV as LassoCV
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, ignore_warnings as ignore_warnings
from typing import Any

filterwarnings_normalize: Any

def test_sparse_coef() -> None: ...
def test_normalize_option() -> None: ...
def test_lasso_zero() -> None: ...
def test_enet_toy_list_input() -> None: ...
def test_enet_toy_explicit_sparse_input() -> None: ...
def make_sparse_data(n_samples: int = ..., n_features: int = ..., n_informative: int = ..., seed: int = ..., positive: bool = ..., n_targets: int = ...): ...
def test_sparse_enet_not_as_toy_dataset() -> None: ...
def test_sparse_lasso_not_as_toy_dataset() -> None: ...
def test_enet_multitarget() -> None: ...
def test_path_parameters() -> None: ...
def test_same_output_sparse_dense_lasso_and_enet_cv() -> None: ...
def test_same_multiple_output_sparse_dense() -> None: ...
def test_sparse_enet_coordinate_descent() -> None: ...
