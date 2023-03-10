from sklearn import datasets as datasets
from sklearn.linear_model import ARDRegression as ARDRegression, BayesianRidge as BayesianRidge, Ridge as Ridge
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_less as assert_array_less
from sklearn.utils.extmath import fast_logdet as fast_logdet
from typing import Any

diabetes: Any

def test_n_iter() -> None: ...
def test_bayesian_ridge_scores() -> None: ...
def test_bayesian_ridge_score_values() -> None: ...
def test_bayesian_ridge_parameter() -> None: ...
def test_bayesian_sample_weights() -> None: ...
def test_toy_bayesian_ridge_object() -> None: ...
def test_bayesian_initial_params() -> None: ...
def test_prediction_bayesian_ridge_ard_with_constant_input() -> None: ...
def test_std_bayesian_ridge_ard_with_constant_input() -> None: ...
def test_update_of_sigma_in_ard() -> None: ...
def test_toy_ard_object() -> None: ...
def test_ard_accuracy_on_easy_problem(seed, n_samples, n_features) -> None: ...
def test_return_std(): ...
def test_update_sigma(seed) -> None: ...
def test_ard_regression_predict_normalize_true() -> None: ...
