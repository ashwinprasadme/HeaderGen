from statsmodels.base.model import LikelihoodModel as LikelihoodModel, LikelihoodModelResults as LikelihoodModelResults, Model as Model
from statsmodels.compat.python import lrange as lrange
from statsmodels.regression.linear_model import OLS as OLS, RegressionResults as RegressionResults, RegressionResultsWrapper as RegressionResultsWrapper
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.numdiff import approx_fprime as approx_fprime
from typing import Any

DEBUG: int

def maxabs(x): ...

class IV2SLS(LikelihoodModel):
    df_resid: Any
    df_model: Any
    def __init__(self, endog, exog, instrument: Any | None = ...) -> None: ...
    wendog: Any
    wexog: Any
    def initialize(self) -> None: ...
    def whiten(self, X) -> None: ...
    xhatparams: Any
    xhatprod: Any
    normalized_cov_params: Any
    def fit(self): ...
    def predict(self, params, exog: Any | None = ...): ...

class IVRegressionResults(RegressionResults):
    def fvalue(self): ...
    def spec_hausman(self, dof: Any | None = ...): ...
    diagn: Any
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ...): ...

class GMM(Model):
    results_class: str
    nobs: Any
    nmoms: Any
    k_params: Any
    epsilon_iter: float
    def __init__(self, endog, exog, instrument, k_moms: Any | None = ..., k_params: Any | None = ..., missing: str = ..., **kwds) -> None: ...
    def set_param_names(self, param_names, k_params: Any | None = ...) -> None: ...
    results: Any
    def fit(self, start_params: Any | None = ..., maxiter: int = ..., inv_weights: Any | None = ..., weights_method: str = ..., wargs=..., has_optimal_weights: bool = ..., optim_method: str = ..., optim_args: Any | None = ...): ...
    def fitgmm(self, start, weights: Any | None = ..., optim_method: str = ..., optim_args: Any | None = ...): ...
    def fitgmm_cu(self, start, optim_method: str = ..., optim_args: Any | None = ...): ...
    def start_weights(self, inv: bool = ...): ...
    def gmmobjective(self, params, weights): ...
    def gmmobjective_cu(self, params, weights_method: str = ..., wargs=...): ...
    history: Any
    def fititer(self, start, maxiter: int = ..., start_invweights: Any | None = ..., weights_method: str = ..., wargs=..., optim_method: str = ..., optim_args: Any | None = ...): ...
    def calc_weightmatrix(self, moms, weights_method: str = ..., wargs=..., params: Any | None = ...): ...
    def momcond_mean(self, params): ...
    def gradient_momcond(self, params, epsilon: float = ..., centered: bool = ...): ...
    def score(self, params, weights, epsilon: Any | None = ..., centered: bool = ...): ...
    def score_cu(self, params, epsilon: Any | None = ..., centered: bool = ...): ...

class GMMResults(LikelihoodModelResults):
    use_t: bool
    nobs: Any
    df_resid: Any
    cov_params_default: Any
    def __init__(self, *args, **kwds) -> None: ...
    def q(self): ...
    def jval(self): ...
    def calc_cov_params(self, moms, gradmoms, weights: Any | None = ..., use_weights: bool = ..., has_optimal_weights: bool = ..., weights_method: str = ..., wargs=...): ...
    @property
    def bse_(self): ...
    def get_bse(self, **kwds): ...
    def jtest(self): ...
    def compare_j(self, other): ...
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ...): ...

class IVGMM(GMM):
    results_class: str
    def fitstart(self): ...
    def start_weights(self, inv: bool = ...): ...
    def get_error(self, params): ...
    def predict(self, params, exog: Any | None = ...): ...
    def momcond(self, params): ...

class LinearIVGMM(IVGMM):
    def fitgmm(self, start, weights: Any | None = ..., optim_method: Any | None = ..., **kwds): ...
    def predict(self, params, exog: Any | None = ...): ...
    def gradient_momcond(self, params, **kwds): ...
    def score(self, params, weights, **kwds): ...

class NonlinearIVGMM(IVGMM):
    def fitstart(self): ...
    func: Any
    def __init__(self, endog, exog, instrument, func, **kwds) -> None: ...
    def predict(self, params, exog: Any | None = ...): ...
    def jac_func(self, params, weights, args: Any | None = ..., centered: bool = ..., epsilon: Any | None = ...): ...
    def jac_error(self, params, weights, args: Any | None = ..., centered: bool = ..., epsilon: Any | None = ...): ...
    def score(self, params, weights, **kwds): ...

class IVGMMResults(GMMResults):
    def fittedvalues(self): ...
    def resid(self): ...
    def ssr(self): ...

def spec_hausman(params_e, params_i, cov_params_e, cov_params_i, dof: Any | None = ...): ...

class DistQuantilesGMM(GMM):
    epsilon_iter: float
    distfn: Any
    endog: Any
    pquant: Any
    xquant: Any
    nmoms: Any
    exog: Any
    instrument: Any
    results: Any
    def __init__(self, endog, exog, instrument, **kwds) -> None: ...
    def fitstart(self): ...
    def momcond(self, params): ...
    def fitonce(self, start: Any | None = ..., weights: Any | None = ..., has_optimal_weights: bool = ...): ...

results_class_dict: Any
