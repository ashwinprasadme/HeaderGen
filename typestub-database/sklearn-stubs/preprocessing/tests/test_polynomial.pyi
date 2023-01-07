from sklearn.linear_model import LinearRegression as LinearRegression
from sklearn.pipeline import Pipeline as Pipeline
from sklearn.preprocessing import KBinsDiscretizer as KBinsDiscretizer, PolynomialFeatures as PolynomialFeatures, SplineTransformer as SplineTransformer
from sklearn.utils._testing import assert_array_almost_equal as assert_array_almost_equal
from sklearn.utils.fixes import linspace as linspace, parse_version as parse_version, sp_version as sp_version

def test_polynomial_and_spline_array_order(est): ...
def test_spline_transformer_input_validation(params, err_msg) -> None: ...
def test_spline_transformer_manual_knot_input() -> None: ...
def test_spline_transformer_integer_knots(extrapolation) -> None: ...
def test_spline_transformer_feature_names(get_names) -> None: ...
def test_spline_transformer_unity_decomposition(degree, n_knots, knots, extrapolation) -> None: ...
def test_spline_transformer_linear_regression(bias, intercept) -> None: ...
def test_spline_transformer_get_base_knot_positions(knots, n_knots, sample_weight, expected_knots) -> None: ...
def test_spline_transformer_periodicity_of_extrapolation(knots, n_knots, degree) -> None: ...
def test_spline_transformer_periodic_linear_regression(bias, intercept): ...
def test_spline_transformer_periodic_spline_backport() -> None: ...
def test_spline_transformer_periodic_splines_periodicity() -> None: ...
def test_spline_transformer_periodic_splines_smoothness(degree) -> None: ...
def test_spline_transformer_extrapolation(bias, intercept, degree) -> None: ...
def test_spline_transformer_kbindiscretizer() -> None: ...
def test_spline_transformer_n_features_out(n_knots, include_bias, degree) -> None: ...
def test_polynomial_features_input_validation(params, err_msg) -> None: ...
def single_feature_degree3(): ...
def test_polynomial_features_one_feature(single_feature_degree3, degree, include_bias, interaction_only, indices, sparse_X) -> None: ...
def two_features_degree3(): ...
def test_polynomial_features_two_features(two_features_degree3, degree, include_bias, interaction_only, indices, sparse_X) -> None: ...
def test_polynomial_feature_names(get_names) -> None: ...
def test_polynomial_features_csc_X(deg, include_bias, interaction_only, dtype) -> None: ...
def test_polynomial_features_csr_X(deg, include_bias, interaction_only, dtype) -> None: ...
def test_num_combinations(n_features, min_degree, max_degree, interaction_only, include_bias) -> None: ...
def test_polynomial_features_csr_X_floats(deg, include_bias, interaction_only, dtype) -> None: ...
def test_polynomial_features_csr_X_zero_row(zero_row_index, deg, interaction_only) -> None: ...
def test_polynomial_features_csr_X_degree_4(include_bias, interaction_only) -> None: ...
def test_polynomial_features_csr_X_dim_edges(deg, dim, interaction_only) -> None: ...
def test_polynomial_features_deprecated_n_input_features() -> None: ...
def test_get_feature_names_deprecated(Transformer) -> None: ...