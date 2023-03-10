import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from typing import Any

class DiscreteModel(base.LikelihoodModel):
    raise_on_perfect_prediction: bool
    def __init__(self, endog, exog, check_rank: bool = ..., **kwargs) -> None: ...
    df_model: Any
    df_resid: Any
    def initialize(self) -> None: ...
    def cdf(self, X) -> None: ...
    def pdf(self, X) -> None: ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: bool = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., qc_verbose: bool = ..., **kwargs): ...
    def cov_params_func_l1(self, likelihood_model, xopt, retvals): ...
    def predict(self, params, exog: Any | None = ..., linear: bool = ...) -> None: ...

class BinaryModel(DiscreteModel):
    def __init__(self, endog, exog, check_rank: bool = ..., **kwargs) -> None: ...
    def predict(self, params, exog: Any | None = ..., linear: bool = ...): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...

class MultinomialModel(BinaryModel):
    endog: Any
    J: Any
    K: Any
    df_resid: Any
    def initialize(self) -> None: ...
    def predict(self, params, exog: Any | None = ..., linear: bool = ...): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...

class CountModel(DiscreteModel):
    exposure: Any
    offset: Any
    endog: Any
    exog: Any
    def __init__(self, endog, exog, offset: Any | None = ..., exposure: Any | None = ..., missing: str = ..., check_rank: bool = ..., **kwargs) -> None: ...
    def predict(self, params, exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., linear: bool = ...): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...

class Poisson(CountModel):
    __doc__: Any
    @property
    def family(self): ...
    def cdf(self, X): ...
    def pdf(self, X): ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...
    def fit_constrained(self, constraints, start_params: Any | None = ..., **fit_kwds): ...
    def score(self, params): ...
    def score_obs(self, params): ...
    def score_factor(self, params): ...
    def hessian(self, params): ...
    def hessian_factor(self, params): ...

class GeneralizedPoisson(CountModel):
    __doc__: Any
    parameterization: Any
    k_extra: int
    def __init__(self, endog, exog, p: int = ..., offset: Any | None = ..., exposure: Any | None = ..., missing: str = ..., check_rank: bool = ..., **kwargs) -> None: ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., use_transparams: bool = ..., cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ..., optim_kwds_prelim: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...
    def score_obs(self, params): ...
    def score(self, params): ...
    def hessian(self, params): ...
    def predict(self, params, exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., which: str = ...): ...

class Logit(BinaryModel):
    __doc__: Any
    def cdf(self, X): ...
    def pdf(self, X): ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def score(self, params): ...
    def score_obs(self, params): ...
    def hessian(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., **kwargs): ...

class Probit(BinaryModel):
    __doc__: Any
    def cdf(self, X): ...
    def pdf(self, X): ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def score(self, params): ...
    def score_obs(self, params): ...
    def hessian(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., **kwargs): ...

class MNLogit(MultinomialModel):
    __doc__: Any
    def __init__(self, endog, exog, check_rank: bool = ..., **kwargs) -> None: ...
    def pdf(self, eXB) -> None: ...
    def cdf(self, X): ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def score(self, params): ...
    def loglike_and_score(self, params): ...
    def score_obs(self, params): ...
    def hessian(self, params): ...

class NegativeBinomial(CountModel):
    __doc__: Any
    loglike_method: Any
    k_extra: int
    def __init__(self, endog, exog, loglike_method: str = ..., offset: Any | None = ..., exposure: Any | None = ..., missing: str = ..., check_rank: bool = ..., **kwargs) -> None: ...
    def loglike(self, params): ...
    def score_obs(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ..., optim_kwds_prelim: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...

class NegativeBinomialP(CountModel):
    __doc__: Any
    parameterization: Any
    k_extra: int
    def __init__(self, endog, exog, p: int = ..., offset: Any | None = ..., exposure: Any | None = ..., missing: str = ..., check_rank: bool = ..., **kwargs) -> None: ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def score_obs(self, params): ...
    def score(self, params): ...
    def hessian(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., use_transparams: bool = ..., cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ..., optim_kwds_prelim: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...
    def predict(self, params, exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., which: str = ...): ...
    def convert_params(self, params, mu): ...

class DiscreteResults(base.LikelihoodModelResults):
    __doc__: Any
    model: Any
    df_model: Any
    df_resid: Any
    nobs: Any
    use_t: Any
    cov_type: str
    cov_kwds: Any
    def __init__(self, model, mlefit, cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ...) -> None: ...
    def prsquared(self): ...
    def llr(self): ...
    def llr_pvalue(self): ...
    def set_null_options(self, llnull: Any | None = ..., attach_results: bool = ..., **kwargs) -> None: ...
    res_null: Any
    def llnull(self): ...
    def fittedvalues(self): ...
    def resid_response(self): ...
    def aic(self): ...
    def bic(self): ...
    def get_margeff(self, at: str = ..., method: str = ..., atexog: Any | None = ..., dummy: bool = ..., count: bool = ...): ...
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ..., yname_list: Any | None = ...): ...
    def summary2(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ..., float_format: str = ...): ...

class CountResults(DiscreteResults):
    __doc__: Any
    def resid(self): ...

class NegativeBinomialResults(CountResults):
    __doc__: Any
    def lnalpha(self): ...
    def lnalpha_std_err(self): ...
    def aic(self): ...
    def bic(self): ...

class GeneralizedPoissonResults(NegativeBinomialResults):
    __doc__: Any

class L1CountResults(DiscreteResults):
    __doc__: Any
    trimmed: Any
    nnz_params: Any
    df_model: Any
    df_resid: Any
    def __init__(self, model, cntfit) -> None: ...

class PoissonResults(CountResults):
    def predict_prob(self, n: Any | None = ..., exog: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., transform: bool = ...): ...
    @property
    def resid_pearson(self): ...

class L1PoissonResults(L1CountResults, PoissonResults): ...
class L1NegativeBinomialResults(L1CountResults, NegativeBinomialResults): ...
class L1GeneralizedPoissonResults(L1CountResults, GeneralizedPoissonResults): ...

class OrderedResults(DiscreteResults):
    __doc__: Any

class BinaryResults(DiscreteResults):
    __doc__: Any
    def pred_table(self, threshold: float = ...): ...
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ..., yname_list: Any | None = ...): ...
    def resid_dev(self): ...
    def resid_pearson(self): ...
    def resid_response(self): ...

class LogitResults(BinaryResults):
    __doc__: Any
    def resid_generalized(self): ...

class ProbitResults(BinaryResults):
    __doc__: Any
    def resid_generalized(self): ...

class L1BinaryResults(BinaryResults):
    __doc__: Any
    trimmed: Any
    nnz_params: Any
    df_model: Any
    df_resid: Any
    def __init__(self, model, bnryfit) -> None: ...

class MultinomialResults(DiscreteResults):
    __doc__: Any
    J: Any
    K: Any
    def __init__(self, model, mlefit) -> None: ...
    def pred_table(self): ...
    def bse(self): ...
    def aic(self): ...
    def bic(self): ...
    def conf_int(self, alpha: float = ..., cols: Any | None = ...): ...
    def margeff(self) -> None: ...
    def resid_misclassified(self): ...
    def summary2(self, alpha: float = ..., float_format: str = ...): ...

class L1MultinomialResults(MultinomialResults):
    __doc__: Any
    trimmed: Any
    nnz_params: Any
    df_model: Any
    df_resid: Any
    def __init__(self, model, mlefit) -> None: ...

class OrderedResultsWrapper(lm.RegressionResultsWrapper): ...
class CountResultsWrapper(lm.RegressionResultsWrapper): ...
class NegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class GeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class PoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1CountResultsWrapper(lm.RegressionResultsWrapper): ...
class L1PoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1NegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class L1GeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class BinaryResultsWrapper(lm.RegressionResultsWrapper): ...
class L1BinaryResultsWrapper(lm.RegressionResultsWrapper): ...
class MultinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class L1MultinomialResultsWrapper(lm.RegressionResultsWrapper): ...
