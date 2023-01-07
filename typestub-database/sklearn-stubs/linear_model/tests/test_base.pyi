from sklearn.datasets import load_iris as load_iris, make_regression as make_regression, make_sparse_uncorrelated as make_sparse_uncorrelated
from sklearn.linear_model import LinearRegression as LinearRegression
from sklearn.linear_model._base import make_dataset as make_dataset
from sklearn.preprocessing import StandardScaler as StandardScaler
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal
from sklearn.utils.fixes import parse_version as parse_version
from typing import Any

rng: Any
rtol: float

def test_linear_regression() -> None: ...
def test_linear_regression_sample_weights() -> None: ...
def test_raises_value_error_if_positive_and_sparse() -> None: ...
def test_raises_value_error_if_sample_weights_greater_than_1d() -> None: ...
def test_fit_intercept() -> None: ...
def test_error_on_wrong_normalize() -> None: ...
def test_deprecate_normalize(normalize, default) -> None: ...
def test_linear_regression_sparse(random_state: int = ...) -> None: ...
def test_linear_regression_sparse_equal_dense(normalize, fit_intercept) -> None: ...
def test_linear_regression_multiple_outcome(random_state: int = ...) -> None: ...
def test_linear_regression_sparse_multiple_outcome(random_state: int = ...) -> None: ...
def test_linear_regression_positive() -> None: ...
def test_linear_regression_positive_multiple_outcome(random_state: int = ...) -> None: ...
def test_linear_regression_positive_vs_nonpositive() -> None: ...
def test_linear_regression_positive_vs_nonpositive_when_positive() -> None: ...
def test_linear_regression_pd_sparse_dataframe_warning() -> None: ...
def test_preprocess_data() -> None: ...
def test_preprocess_data_multioutput() -> None: ...
def test_preprocess_data_weighted(is_sparse) -> None: ...
def test_sparse_preprocess_data_with_return_mean() -> None: ...
def test_csr_preprocess_data() -> None: ...
def test_preprocess_copy_data_no_checks(is_sparse, to_copy) -> None: ...
def test_dtype_preprocess_data() -> None: ...
def test_rescale_data_dense(n_targets) -> None: ...
def test_fused_types_make_dataset() -> None: ...