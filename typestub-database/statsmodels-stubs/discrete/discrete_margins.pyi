from statsmodels.compat.python import lzip as lzip
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from typing import Any

def margeff_cov_params(model, params, exog, cov_params, at, derivative, dummy_ind, count_ind, method, J): ...
def margeff_cov_with_se(model, params, exog, cov_params, at, derivative, dummy_ind, count_ind, method, J): ...
def margeff() -> None: ...

class Margins:
    results: Any
    dist: Any
    def __init__(self, results, get_margeff, derivative, dist: Any | None = ..., margeff_args=...) -> None: ...
    margeff: Any
    def get_margeff(self, *args, **kwargs) -> None: ...
    def tvalues(self) -> None: ...
    def cov_margins(self) -> None: ...
    def margins_se(self) -> None: ...
    def summary_frame(self) -> None: ...
    def pvalues(self) -> None: ...
    def conf_int(self, alpha: float = ...) -> None: ...
    def summary(self, alpha: float = ...) -> None: ...

class DiscreteMargins:
    results: Any
    def __init__(self, results, args, kwargs=...) -> None: ...
    def tvalues(self): ...
    def summary_frame(self, alpha: float = ...): ...
    def pvalues(self): ...
    def conf_int(self, alpha: float = ...): ...
    def summary(self, alpha: float = ...): ...
    margeff_options: Any
    dummy_idx: Any
    count_idx: Any
    margeff: Any
    margeff_se: Any
    margeff_cov: Any
    def get_margeff(self, at: str = ..., method: str = ..., atexog: Any | None = ..., dummy: bool = ..., count: bool = ...) -> None: ...
