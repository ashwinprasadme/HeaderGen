from ..base import TransformerMixin as TransformerMixin
from ..utils.validation import check_is_fitted as check_is_fitted

class AgglomerationTransform(TransformerMixin):
    def transform(self, X): ...
    def inverse_transform(self, Xred): ...
