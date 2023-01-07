from sklearn.datasets import load_digits as load_digits, make_classification as make_classification
from sklearn.dummy import DummyClassifier as DummyClassifier
from sklearn.model_selection import GridSearchCV as GridSearchCV, GroupKFold as GroupKFold, GroupShuffleSplit as GroupShuffleSplit, KFold as KFold, LeaveOneGroupOut as LeaveOneGroupOut, LeaveOneOut as LeaveOneOut, LeavePGroupsOut as LeavePGroupsOut, LeavePOut as LeavePOut, PredefinedSplit as PredefinedSplit, RepeatedKFold as RepeatedKFold, RepeatedStratifiedKFold as RepeatedStratifiedKFold, ShuffleSplit as ShuffleSplit, StratifiedGroupKFold as StratifiedGroupKFold, StratifiedKFold as StratifiedKFold, StratifiedShuffleSplit as StratifiedShuffleSplit, TimeSeriesSplit as TimeSeriesSplit, check_cv as check_cv, cross_val_score as cross_val_score, train_test_split as train_test_split
from sklearn.svm import SVC as SVC
from sklearn.utils._mocking import MockDataFrame as MockDataFrame
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal, ignore_warnings as ignore_warnings
from typing import Any

X: Any
y: Any
P_sparse: Any
test_groups: Any
digits: Any

def test_cross_validator_with_default_params() -> None: ...
def test_2d_y() -> None: ...
def check_valid_split(train, test, n_samples: Any | None = ...) -> None: ...
def check_cv_coverage(cv, X, y, groups, expected_n_splits) -> None: ...
def test_kfold_valueerrors() -> None: ...
def test_kfold_indices() -> None: ...
def test_kfold_no_shuffle() -> None: ...
def test_stratified_kfold_no_shuffle() -> None: ...
def test_stratified_kfold_ratios(k, shuffle, kfold) -> None: ...
def test_stratified_kfold_label_invariance(k, shuffle, kfold): ...
def test_kfold_balance() -> None: ...
def test_stratifiedkfold_balance(kfold) -> None: ...
def test_shuffle_kfold() -> None: ...
def test_shuffle_kfold_stratifiedkfold_reproducibility(kfold) -> None: ...
def test_shuffle_stratifiedkfold() -> None: ...
def test_kfold_can_detect_dependent_samples_on_digits() -> None: ...
def test_stratified_group_kfold_trivial() -> None: ...
def test_stratified_group_kfold_approximate() -> None: ...
def test_stratified_group_kfold_homogeneous_groups(y, groups, expected) -> None: ...
def test_stratified_group_kfold_against_group_kfold(cls_distr, n_groups) -> None: ...
def test_shuffle_split() -> None: ...
def test_shuffle_split_default_test_size(split_class, train_size, exp_train, exp_test) -> None: ...
def test_group_shuffle_split_default_test_size(train_size, exp_train, exp_test) -> None: ...
def test_stratified_shuffle_split_init() -> None: ...
def test_stratified_shuffle_split_respects_test_size() -> None: ...
def test_stratified_shuffle_split_iter() -> None: ...
def test_stratified_shuffle_split_even() -> None: ...
def test_stratified_shuffle_split_overlap_train_test_bug() -> None: ...
def test_stratified_shuffle_split_multilabel() -> None: ...
def test_stratified_shuffle_split_multilabel_many_labels() -> None: ...
def test_predefinedsplit_with_kfold_split() -> None: ...
def test_group_shuffle_split() -> None: ...
def test_leave_one_p_group_out() -> None: ...
def test_leave_group_out_changing_groups() -> None: ...
def test_leave_one_p_group_out_error_on_fewer_number_of_groups() -> None: ...
def test_repeated_cv_value_errors() -> None: ...
def test_repeated_cv_repr(RepeatedCV) -> None: ...
def test_repeated_kfold_determinstic_split() -> None: ...
def test_get_n_splits_for_repeated_kfold() -> None: ...
def test_get_n_splits_for_repeated_stratified_kfold() -> None: ...
def test_repeated_stratified_kfold_determinstic_split() -> None: ...
def test_train_test_split_errors() -> None: ...
def test_train_test_split_invalid_sizes1(train_size, test_size) -> None: ...
def test_train_test_split_invalid_sizes2(train_size, test_size) -> None: ...
def test_train_test_split_default_test_size(train_size, exp_train, exp_test) -> None: ...
def test_train_test_split() -> None: ...
def test_train_test_split_32bit_overflow() -> None: ...
def test_train_test_split_pandas() -> None: ...
def test_train_test_split_sparse() -> None: ...
def test_train_test_split_mock_pandas() -> None: ...
def test_train_test_split_list_input() -> None: ...
def test_shufflesplit_errors(test_size, train_size) -> None: ...
def test_shufflesplit_reproducible() -> None: ...
def test_stratifiedshufflesplit_list_input() -> None: ...
def test_train_test_split_allow_nans() -> None: ...
def test_check_cv() -> None: ...
def test_cv_iterable_wrapper() -> None: ...
def test_group_kfold(kfold) -> None: ...
def test_time_series_cv() -> None: ...
def test_time_series_max_train_size() -> None: ...
def test_time_series_test_size() -> None: ...
def test_time_series_gap() -> None: ...
def test_nested_cv() -> None: ...
def test_build_repr(): ...
def test_shuffle_split_empty_trainset(CVSplitter) -> None: ...
def test_train_test_split_empty_trainset() -> None: ...
def test_leave_one_out_empty_trainset() -> None: ...
def test_leave_p_out_empty_trainset() -> None: ...
def test_random_state_shuffle_false(Klass) -> None: ...
def test_yields_constant_splits(cv, expected) -> None: ...