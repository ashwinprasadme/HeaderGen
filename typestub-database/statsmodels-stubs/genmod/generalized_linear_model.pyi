import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from statsmodels.genmod._prediction import PredictionResults as PredictionResults
from typing import Any

class _ModuleVariable:
    @property
    def use_bic_llf(self): ...
    def set_use_bic_llf(self, val) -> None: ...

class GLM(base.LikelihoodModel):
    __doc__: Any
    freq_weights: Any
    var_weights: Any
    nobs: Any
    n_trials: Any
    scaletype: Any
    def __init__(self, endog, exog, family: Any | None = ..., offset: Any | None = ..., exposure: Any | None = ..., freq_weights: Any | None = ..., var_weights: Any | None = ..., missing: str = ..., **kwargs) -> None: ...
    df_model: Any
    wnobs: Any
    df_resid: Any
    def initialize(self) -> None: ...
    def loglike_mu(self, mu, scale: float = ...): ...
    def loglike(self, params, scale: Any | None = ...): ...
    def score_obs(self, params, scale: Any | None = ...): ...
    def score(self, params, scale: Any | None = ...): ...
    def score_factor(self, params, scale: Any | None = ...): ...
    def hessian_factor(self, params, scale: Any | None = ..., observed: bool = ...): ...
    def hessian(self, params, scale: Any | None = ..., observed: Any | None = ...): ...
    def information(self, params, scale: Any | None = ...): ...
    def score_test(self, params_constrained, k_constraints: Any | None = ..., exog_extra: Any | None = ..., observed: bool = ...): ...
    def estimate_scale(self, mu): ...
    def estimate_tweedie_power(self, mu, method: str = ..., low: float = ..., high: float = ...): ...
    def predict(self, params, exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., linear: bool = ...): ...
    def get_distribution(self, params, scale: Any | None = ..., exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., var_weights: float = ..., n_trials: float = ...): ...
    def fit(self, start_params: Any | None = ..., maxiter: int = ..., method: str = ..., tol: float = ..., scale: Any | None = ..., cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ..., full_output: bool = ..., disp: bool = ..., max_start_irls: int = ..., **kwargs): ...
    mu: Any
    scale: Any
    def fit_regularized(self, method: str = ..., alpha: float = ..., start_params: Any | None = ..., refit: bool = ..., opt_method: str = ..., **kwargs): ...
    def fit_constrained(self, constraints, start_params: Any | None = ..., **fit_kwds): ...

class GLMResults(base.LikelihoodModelResults):
    family: Any
    nobs: Any
    df_resid: Any
    df_model: Any
    use_t: bool
    cov_type: str
    cov_kwds: Any
    def __init__(self, model, params, normalized_cov_params, scale, cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ...) -> None: ...
    def resid_response(self): ...
    def resid_pearson(self): ...
    def resid_working(self): ...
    def resid_anscombe(self): ...
    def resid_anscombe_scaled(self): ...
    def resid_anscombe_unscaled(self): ...
    def resid_deviance(self): ...
    def pearson_chi2(self): ...
    def fittedvalues(self): ...
    def mu(self): ...
    def null(self): ...
    def deviance(self): ...
    def null_deviance(self): ...
    def llnull(self): ...
    def llf_scaled(self, scale: Any | None = ...): ...
    def llf(self): ...
    def pseudo_rsquared(self, kind: str = ...): ...
    def aic(self): ...
    @property
    def bic(self): ...
    def bic_deviance(self): ...
    def bic_llf(self): ...
    def info_criteria(self, crit, scale: Any | None = ..., dk_params: int = ...): ...
    def get_prediction(self, exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., transform: bool = ..., linear: bool = ..., row_labels: Any | None = ...): ...
    def get_hat_matrix_diag(self, observed: bool = ...): ...
    def get_influence(self, observed: bool = ...): ...
    def remove_data(self) -> None: ...
    def plot_added_variable(self, focus_exog, resid_type: Any | None = ..., use_glm_weights: bool = ..., fit_kwargs: Any | None = ..., ax: Any | None = ...): ...
    def plot_partial_residuals(self, focus_exog, ax: Any | None = ...): ...
    def plot_ceres_residuals(self, focus_exog, frac: float = ..., cond_means: Any | None = ..., ax: Any | None = ...): ...
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ...): ...
    method: str
    def summary2(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ..., float_format: str = ...): ...

class GLMResultsWrapper(lm.RegressionResultsWrapper): ...