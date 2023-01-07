from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..utils import check_array as check_array, tosequence as tosequence
from ..utils.deprecation import deprecated as deprecated
from typing import Any

class DictVectorizer(TransformerMixin, BaseEstimator):
    dtype: Any
    separator: Any
    sparse: Any
    sort: Any
    def __init__(self, *, dtype=..., separator: str = ..., sparse: bool = ..., sort: bool = ...) -> None: ...
    feature_names_: Any
    vocabulary_: Any
    def fit(self, X, y: Any | None = ...): ...
    def fit_transform(self, X, y: Any | None = ...): ...
    def inverse_transform(self, X, dict_type=...): ...
    def transform(self, X): ...
    def get_feature_names(self): ...
    def get_feature_names_out(self, input_features: Any | None = ...): ...
    def restrict(self, support, indices: bool = ...): ...