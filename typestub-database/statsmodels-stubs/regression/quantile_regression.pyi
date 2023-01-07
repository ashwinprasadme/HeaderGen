from statsmodels.regression.linear_model import RegressionModel as RegressionModel, RegressionResults as RegressionResults, RegressionResultsWrapper as RegressionResultsWrapper
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.sm_exceptions import ConvergenceWarning as ConvergenceWarning, IterationLimitWarning as IterationLimitWarning
from typing import Any

class QuantReg(RegressionModel):
    def __init__(self, endog, exog, **kwargs) -> None: ...
    def whiten(self, data): ...
    rank: Any
    df_model: Any
    df_resid: Any
    def fit(self, q: float = ..., vcov: str = ..., kernel: str = ..., bandwidth: str = ..., max_iter: int = ..., p_tol: float = ..., **kwargs): ...

kernels: Any

def hall_sheather(n, q, alpha: float = ...): ...
def bofinger(n, q): ...
def chamberlain(n, q, alpha: float = ...): ...

class QuantRegResults(RegressionResults):
    def prsquared(self): ...
    def scale(self): ...
    def bic(self): ...
    def aic(self): ...
    def llf(self): ...
    def rsquared(self): ...
    def rsquared_adj(self): ...
    def mse(self): ...
    def mse_model(self): ...
    def mse_total(self): ...
    def centered_tss(self): ...
    def uncentered_tss(self): ...
    def HC0_se(self) -> None: ...
    def HC1_se(self) -> None: ...
    def HC2_se(self) -> None: ...
    def HC3_se(self) -> None: ...
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ...): ...