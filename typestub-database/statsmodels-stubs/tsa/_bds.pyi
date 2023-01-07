from statsmodels.tools.validation import array_like as array_like
from typing import Any

def distance_indicators(x, epsilon: Any | None = ..., distance: float = ...): ...
def correlation_sum(indicators, embedding_dim): ...
def correlation_sums(indicators, max_dim): ...
def bds(x, max_dim: int = ..., epsilon: Any | None = ..., distance: float = ...): ...