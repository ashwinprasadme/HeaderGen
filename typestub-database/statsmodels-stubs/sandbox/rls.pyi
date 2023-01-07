from statsmodels.regression.linear_model import GLS as GLS, RegressionResults as RegressionResults
from typing import Any

class RLS(GLS):
    ncoeffs: Any
    nconstraint: Any
    constraint: Any
    param: Any
    sigma: Any
    cholsigmainv: Any
    def __init__(self, endog, exog, constr, param: float = ..., sigma: Any | None = ...) -> None: ...
    @property
    def rwexog(self): ...
    @property
    def inv_rwexog(self): ...
    @property
    def rwendog(self): ...
    @property
    def rnorm_cov_params(self): ...
    @property
    def wrnorm_cov_params(self): ...
    @property
    def coeffs(self): ...
    def fit(self): ...