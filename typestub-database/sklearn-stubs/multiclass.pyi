from .base import BaseEstimator, ClassifierMixin, MetaEstimatorMixin, MultiOutputMixin
from typing import Any

class _ConstantPredictor(BaseEstimator):
    y_: Any
    def fit(self, X, y): ...
    def predict(self, X): ...
    def decision_function(self, X): ...
    def predict_proba(self, X): ...

class OneVsRestClassifier(MultiOutputMixin, ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Any
    n_jobs: Any
    def __init__(self, estimator, *, n_jobs: Any | None = ...) -> None: ...
    label_binarizer_: Any
    classes_: Any
    estimators_: Any
    n_features_in_: Any
    feature_names_in_: Any
    def fit(self, X, y): ...
    def partial_fit(self, X, y, classes: Any | None = ...): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def decision_function(self, X): ...
    @property
    def multilabel_(self): ...
    @property
    def n_classes_(self): ...
    @property
    def coef_(self): ...
    @property
    def intercept_(self): ...

class OneVsOneClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    estimator: Any
    n_jobs: Any
    def __init__(self, estimator, *, n_jobs: Any | None = ...) -> None: ...
    classes_: Any
    estimators_: Any
    pairwise_indices_: Any
    def fit(self, X, y): ...
    n_features_in_: Any
    def partial_fit(self, X, y, classes: Any | None = ...): ...
    def predict(self, X): ...
    def decision_function(self, X): ...
    @property
    def n_classes_(self): ...

class OutputCodeClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    estimator: Any
    code_size: Any
    random_state: Any
    n_jobs: Any
    def __init__(self, estimator, *, code_size: float = ..., random_state: Any | None = ..., n_jobs: Any | None = ...) -> None: ...
    classes_: Any
    code_book_: Any
    estimators_: Any
    n_features_in_: Any
    feature_names_in_: Any
    def fit(self, X, y): ...
    def predict(self, X): ...
