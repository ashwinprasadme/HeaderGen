from sklearn.datasets import load_iris as load_iris, make_blobs as make_blobs
from sklearn.ensemble import StackingClassifier as StackingClassifier
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.metrics import accuracy_score as accuracy_score
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNeighborsClassifier
from sklearn.semi_supervised import SelfTrainingClassifier as SelfTrainingClassifier
from sklearn.svm import SVC as SVC
from typing import Any

iris: Any
X_train: Any
X_test: Any
y_train: Any
y_test: Any
n_labeled_samples: int
y_train_missing_labels: Any
mapping: Any
y_train_missing_strings: Any

def test_missing_predict_proba() -> None: ...
def test_none_classifier() -> None: ...
def test_invalid_params(max_iter, threshold) -> None: ...
def test_invalid_params_selection_crit() -> None: ...
def test_warns_k_best() -> None: ...
def test_classification(base_estimator, selection_crit) -> None: ...
def test_k_best() -> None: ...
def test_sanity_classification() -> None: ...
def test_none_iter() -> None: ...
def test_zero_iterations(base_estimator, y) -> None: ...
def test_prefitted_throws_error() -> None: ...
def test_labeled_iter(max_iter) -> None: ...
def test_no_unlabeled() -> None: ...
def test_early_stopping() -> None: ...
def test_strings_dtype() -> None: ...
def test_verbose(capsys, verbose) -> None: ...
def test_verbose_k_best(capsys) -> None: ...
def test_k_best_selects_best() -> None: ...
def test_base_estimator_meta_estimator() -> None: ...