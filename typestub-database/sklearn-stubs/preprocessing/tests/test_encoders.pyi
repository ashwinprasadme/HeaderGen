from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.preprocessing import OneHotEncoder as OneHotEncoder, OrdinalEncoder as OrdinalEncoder
from sklearn.utils import is_scalar_nan as is_scalar_nan
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_array_equal as assert_array_equal

def test_one_hot_encoder_sparse_dense() -> None: ...
def test_one_hot_encoder_handle_unknown() -> None: ...
def test_one_hot_encoder_not_fitted() -> None: ...
def test_one_hot_encoder_handle_unknown_strings() -> None: ...
def test_one_hot_encoder_dtype(input_dtype, output_dtype) -> None: ...
def test_one_hot_encoder_dtype_pandas(output_dtype) -> None: ...
def test_one_hot_encoder_feature_names(get_names) -> None: ...
def test_one_hot_encoder_feature_names_unicode(get_names) -> None: ...
def test_one_hot_encoder_set_params() -> None: ...
def check_categorical_onehot(X): ...
def test_one_hot_encoder(X) -> None: ...
def test_one_hot_encoder_inverse(sparse_, drop) -> None: ...
def test_one_hot_encoder_inverse_transform_raise_error_with_unknown(X, X_trans, sparse_) -> None: ...
def test_one_hot_encoder_inverse_if_binary() -> None: ...
def test_one_hot_encoder_drop_reset(get_names, drop, reset_drop) -> None: ...
def test_X_is_not_1D(X, method) -> None: ...
def test_X_is_not_1D_pandas(method) -> None: ...
def test_one_hot_encoder_categories(X, cat_exp, cat_dtype) -> None: ...
def test_one_hot_encoder_specified_categories(X, X2, cats, cat_dtype) -> None: ...
def test_one_hot_encoder_unsorted_categories() -> None: ...
def test_one_hot_encoder_specified_categories_mixed_columns() -> None: ...
def test_one_hot_encoder_pandas() -> None: ...
def test_one_hot_encoder_feature_names_drop(get_names, drop, expected_names) -> None: ...
def test_one_hot_encoder_drop_equals_if_binary() -> None: ...
def test_ordinal_encoder(X) -> None: ...
def test_ordinal_encoder_specified_categories(X, X2, cats, cat_dtype) -> None: ...
def test_ordinal_encoder_inverse() -> None: ...
def test_ordinal_encoder_handle_unknowns_string() -> None: ...
def test_ordinal_encoder_handle_unknowns_numeric(dtype) -> None: ...
def test_ordinal_encoder_handle_unknowns_raise(params, err_type, err_msg) -> None: ...
def test_ordinal_encoder_handle_unknowns_nan() -> None: ...
def test_ordinal_encoder_handle_unknowns_nan_non_float_dtype() -> None: ...
def test_ordinal_encoder_raise_categories_shape() -> None: ...
def test_encoder_dtypes() -> None: ...
def test_encoder_dtypes_pandas() -> None: ...
def test_one_hot_encoder_warning() -> None: ...
def test_one_hot_encoder_drop_manual(missing_value) -> None: ...
def test_one_hot_encoder_invalid_params(X_fit, params, err_msg) -> None: ...
def test_invalid_drop_length(drop) -> None: ...
def test_categories(density, drop) -> None: ...
def test_encoders_has_categorical_tags(Encoder) -> None: ...
def test_one_hot_encoder_get_feature_names_deprecated() -> None: ...
def test_encoders_string_categories(input_dtype, category_dtype, array_type) -> None: ...
def test_ohe_missing_values_get_feature_names(get_names, missing_value) -> None: ...
def test_ohe_missing_value_support_pandas() -> None: ...
def test_ohe_missing_value_support_pandas_categorical(pd_nan_type) -> None: ...
def test_ohe_drop_first_handle_unknown_ignore_warns() -> None: ...
def test_ohe_drop_if_binary_handle_unknown_ignore_warns() -> None: ...
def test_ohe_drop_first_explicit_categories() -> None: ...
def test_ordinal_encoder_passthrough_missing_values_float_errors_dtype() -> None: ...
def test_ordinal_encoder_passthrough_missing_values_float() -> None: ...
def test_ordinal_encoder_missing_value_support_pandas_categorical(pd_nan_type) -> None: ...
def test_ordinal_encoder_specified_categories_missing_passthrough(X, X2, cats, cat_dtype) -> None: ...
def test_ordinal_encoder_handle_missing_and_unknown(X, expected_X_trans, X_test) -> None: ...
def test_ordinal_encoder_sparse() -> None: ...
def test_ordinal_encoder_fit_with_unseen_category() -> None: ...
def test_ordinal_encoder_handle_unknown_string_dtypes(X_train, X_test) -> None: ...
def test_ordinal_encoder_python_integer() -> None: ...
