from sklearn.dummy import DummyRegressor as DummyRegressor
from sklearn.exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from sklearn.metrics import d2_tweedie_score as d2_tweedie_score, explained_variance_score as explained_variance_score, make_scorer as make_scorer, max_error as max_error, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_pinball_loss as mean_pinball_loss, mean_squared_error as mean_squared_error, mean_squared_log_error as mean_squared_log_error, mean_tweedie_deviance as mean_tweedie_deviance, median_absolute_error as median_absolute_error, r2_score as r2_score
from sklearn.model_selection import GridSearchCV as GridSearchCV
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal

def test_regression_metrics(n_samples: int = ...) -> None: ...
def test_mean_squared_error_multioutput_raw_value_squared() -> None: ...
def test_multioutput_regression() -> None: ...
def test_regression_metrics_at_limits() -> None: ...
def test__check_reg_targets() -> None: ...
def test__check_reg_targets_exception() -> None: ...
def test_regression_multioutput_array() -> None: ...
def test_regression_custom_weights() -> None: ...
def test_regression_single_sample(metric) -> None: ...
def test_deprecation_positional_arguments_mape() -> None: ...
def test_tweedie_deviance_continuity() -> None: ...
def test_mean_absolute_percentage_error() -> None: ...
def test_mean_pinball_loss_on_constant_predictions(distribution, target_quantile): ...
def test_dummy_quantile_parameter_tuning() -> None: ...