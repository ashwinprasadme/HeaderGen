from statsmodels.tools.decorators import cache_readonly as cache_readonly
from typing import Any

class TableDist:
    alpha: Any
    size: Any
    crit_table: Any
    n_alpha: Any
    signcrit: Any
    critv_bounds: Any
    asymptotic: Any
    min_nobs: Any
    max_nobs: Any
    def __init__(self, alpha, size, crit_table, asymptotic: Any | None = ..., min_nobs: Any | None = ..., max_nobs: Any | None = ...) -> None: ...
    def polyn(self): ...
    def poly2d(self): ...
    def polyrbf(self): ...
    def prob(self, x, n): ...
    def crit(self, prob, n): ...
    def crit3(self, prob, n): ...
