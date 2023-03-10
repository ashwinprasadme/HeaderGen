from statsmodels.compat.python import lrange as lrange
from statsmodels.regression.feasible_gls import atleast_2dcols as atleast_2dcols
from statsmodels.regression.linear_model import GLS as GLS, OLS as OLS, RegressionResults as RegressionResults
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from typing import Any

class TheilGLS(GLS):
    r_matrix: Any
    q_matrix: Any
    sigma_prior: Any
    sigma_prior_inv: Any
    def __init__(self, endog, exog, r_matrix: Any | None = ..., q_matrix: Any | None = ..., sigma_prior: Any | None = ..., sigma: Any | None = ...) -> None: ...
    res_gls: Any
    normalized_cov_params: Any
    xpxi: Any
    sigma2_e: Any
    def fit(self, pen_weight: float = ..., cov_type: str = ..., use_t: bool = ...): ...
    def select_pen_weight(self, method: str = ..., start_params: float = ..., optim_args: Any | None = ...): ...

class TheilRegressionResults(RegressionResults):
    df_model: Any
    df_resid: Any
    def __init__(self, *args, **kwds) -> None: ...
    def hatmatrix_diag(self): ...
    def hatmatrix_trace(self): ...
    def gcv(self): ...
    def cv(self): ...
    def aicc(self): ...
    def test_compatibility(self): ...
    def share_data(self): ...

def coef_restriction_meandiff(n_coeffs, n_vars: Any | None = ..., position: int = ...): ...
def coef_restriction_diffbase(n_coeffs, n_vars: Any | None = ..., position: int = ..., base_idx: int = ...): ...
def next_odd(d): ...
def coef_restriction_diffseq(n_coeffs, degree: int = ..., n_vars: Any | None = ..., position: int = ..., base_idx: int = ...): ...
