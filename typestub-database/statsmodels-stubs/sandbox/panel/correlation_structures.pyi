from statsmodels.regression.linear_model import yule_walker as yule_walker
from statsmodels.stats.moment_helpers import cov2corr as cov2corr
from typing import Any

def corr_equi(k_vars, rho): ...
def corr_ar(k_vars, ar): ...
def corr_arma(k_vars, ar, ma): ...
def corr2cov(corr, std): ...
def whiten_ar(x, ar_coefs, order): ...
def yule_walker_acov(acov, order: int = ..., method: str = ..., df: Any | None = ..., inv: bool = ...): ...

class ARCovariance:
    ar: Any
    ar_coefs: Any
    k_lags: Any
    arcoefs: Any
    def __init__(self, ar: Any | None = ..., ar_coefs: Any | None = ..., sigma: float = ...) -> None: ...
    @classmethod
    def fit(cls, cov, order, **kwds): ...
    def whiten(self, x): ...
    def corr(self, k_vars: Any | None = ...): ...
    def cov(self, k_vars: Any | None = ...): ...