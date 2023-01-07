from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.cluster import KMeans as KMeans
from sklearn.datasets import load_diabetes as load_diabetes, make_blobs as make_blobs, make_classification as make_classification, make_multilabel_classification as make_multilabel_classification, make_regression as make_regression
from sklearn.linear_model import LogisticRegression as LogisticRegression, Perceptron as Perceptron, Ridge as Ridge
from sklearn.metrics import SCORERS as SCORERS, accuracy_score as accuracy_score, average_precision_score as average_precision_score, balanced_accuracy_score as balanced_accuracy_score, brier_score_loss as brier_score_loss, check_scoring as check_scoring, f1_score as f1_score, fbeta_score as fbeta_score, get_scorer as get_scorer, jaccard_score as jaccard_score, log_loss as log_loss, make_scorer as make_scorer, precision_score as precision_score, r2_score as r2_score, recall_score as recall_score, roc_auc_score as roc_auc_score, top_k_accuracy_score as top_k_accuracy_score
from sklearn.model_selection import GridSearchCV as GridSearchCV, cross_val_score as cross_val_score, train_test_split as train_test_split
from sklearn.multiclass import OneVsRestClassifier as OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier as KNeighborsClassifier
from sklearn.pipeline import make_pipeline as make_pipeline
from sklearn.svm import LinearSVC as LinearSVC
from sklearn.tree import DecisionTreeClassifier as DecisionTreeClassifier, DecisionTreeRegressor as DecisionTreeRegressor
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_equal as assert_array_equal, ignore_warnings as ignore_warnings
from typing import Any

REGRESSION_SCORERS: Any
CLF_SCORERS: Any
CLUSTER_SCORERS: Any
MULTILABEL_ONLY_SCORERS: Any
REQUIRE_POSITIVE_Y_SCORERS: Any
X_mm: Any
y_mm: Any
y_ml_mm: Any
ESTIMATORS: Any
TEMP_FOLDER: Any

def setup_module() -> None: ...
def teardown_module() -> None: ...

class EstimatorWithoutFit: ...

class EstimatorWithFit(BaseEstimator):
    def fit(self, X, y): ...

class EstimatorWithFitAndScore:
    def fit(self, X, y): ...
    def score(self, X, y): ...

class EstimatorWithFitAndPredict:
    y: Any
    def fit(self, X, y): ...
    def predict(self, X): ...

class DummyScorer:
    def __call__(self, est, X, y): ...

def test_all_scorers_repr() -> None: ...
def check_scoring_validator_for_single_metric_usecases(scoring_validator) -> None: ...
def test_check_scoring_and_check_multimetric_scoring(scoring) -> None: ...
def test_check_scoring_and_check_multimetric_scoring_errors(scoring, msg) -> None: ...
def test_check_scoring_gridsearchcv() -> None: ...
def test_make_scorer(): ...
def test_classification_binary_scores(scorer_name, metric) -> None: ...
def test_classification_multiclass_scores(scorer_name, metric) -> None: ...
def test_custom_scorer_pickling() -> None: ...
def test_regression_scorers() -> None: ...
def test_thresholded_scorers() -> None: ...
def test_thresholded_scorers_multilabel_indicator_data(): ...
def test_supervised_cluster_scorers() -> None: ...
def test_raises_on_score_list() -> None: ...
def test_classification_scorer_sample_weight() -> None: ...
def test_regression_scorer_sample_weight() -> None: ...
def test_scorer_memmap_input(name) -> None: ...
def test_scoring_is_not_metric() -> None: ...
def test_multimetric_scorer_calls_method_once(scorers, expected_predict_count, expected_predict_proba_count, expected_decision_func_count) -> None: ...
def test_multimetric_scorer_calls_method_once_classifier_no_decision(): ...
def test_multimetric_scorer_calls_method_once_regressor_threshold(): ...
def test_multimetric_scorer_sanity_check() -> None: ...
def test_multiclass_roc_proba_scorer(scorer_name, metric) -> None: ...
def test_multiclass_roc_proba_scorer_label() -> None: ...
def test_multiclass_roc_no_proba_scorer_errors(scorer_name) -> None: ...
def string_labeled_classification_problem(): ...
def test_average_precision_pos_label(string_labeled_classification_problem) -> None: ...
def test_brier_score_loss_pos_label(string_labeled_classification_problem) -> None: ...
def test_non_symmetric_metric_pos_label(score_func, string_labeled_classification_problem) -> None: ...
def test_scorer_select_proba_error(scorer) -> None: ...
def test_scorer_no_op_multiclass_select_proba() -> None: ...