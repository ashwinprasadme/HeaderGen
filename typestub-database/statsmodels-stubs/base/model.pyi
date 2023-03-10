import statsmodels.base.wrapper as wrap
from statsmodels.base.data import handle_data as handle_data
from statsmodels.base.optimizer import Optimizer as Optimizer
from statsmodels.compat.python import lzip as lzip
from statsmodels.formula import handle_formula_data as handle_formula_data
from statsmodels.stats.contrast import ContrastResults as ContrastResults, WaldTestResults as WaldTestResults, t_test_pairwise as t_test_pairwise
from statsmodels.tools.decorators import cache_readonly as cache_readonly, cached_data as cached_data, cached_value as cached_value
from statsmodels.tools.numdiff import approx_fprime as approx_fprime
from statsmodels.tools.sm_exceptions import HessianInversionWarning as HessianInversionWarning, ValueWarning as ValueWarning
from statsmodels.tools.tools import nan_dot as nan_dot, recipr as recipr
from statsmodels.tools.validation import bool_like as bool_like
from typing import Any

ERROR_INIT_KWARGS: bool

class Model:
    __doc__: Any
    data: Any
    k_constant: Any
    exog: Any
    endog: Any
    def __init__(self, endog, exog: Any | None = ..., **kwargs) -> None: ...
    @classmethod
    def from_formula(cls, formula, data, subset: Any | None = ..., drop_cols: Any | None = ..., *args, **kwargs): ...
    @property
    def endog_names(self): ...
    @property
    def exog_names(self): ...
    def fit(self) -> None: ...
    def predict(self, params, exog: Any | None = ..., *args, **kwargs) -> None: ...

class LikelihoodModel(Model):
    def __init__(self, endog, exog: Any | None = ..., **kwargs) -> None: ...
    def initialize(self) -> None: ...
    def loglike(self, params) -> None: ...
    def score(self, params) -> None: ...
    def information(self, params) -> None: ...
    def hessian(self, params) -> None: ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: bool = ..., disp: bool = ..., fargs=..., callback: Any | None = ..., retall: bool = ..., skip_hessian: bool = ..., **kwargs): ...

class GenericLikelihoodModel(LikelihoodModel):
    nparams: Any
    def __init__(self, endog, exog: Any | None = ..., loglike: Any | None = ..., score: Any | None = ..., hessian: Any | None = ..., missing: str = ..., extra_params_names: Any | None = ..., **kwds) -> None: ...
    df_model: Any
    df_resid: Any
    def initialize(self): ...
    def expandparams(self, params): ...
    def reduceparams(self, params): ...
    def loglike(self, params): ...
    def nloglike(self, params): ...
    def loglikeobs(self, params): ...
    def score(self, params): ...
    def score_obs(self, params, **kwds): ...
    def hessian(self, params): ...
    def hessian_factor(self, params, scale: Any | None = ..., observed: bool = ...) -> None: ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., retall: int = ..., **kwargs): ...

class Results:
    def __init__(self, model, params, **kwd) -> None: ...
    params: Any
    model: Any
    k_constant: Any
    def initialize(self, model, params, **kwargs) -> None: ...
    def predict(self, exog: Any | None = ..., transform: bool = ..., *args, **kwargs): ...
    def summary(self) -> None: ...

class LikelihoodModelResults(Results):
    scale: Any
    cov_type: str
    cov_kwds: Any
    def __init__(self, model, params, normalized_cov_params: Any | None = ..., scale: float = ..., **kwargs) -> None: ...
    def normalized_cov_params(self) -> None: ...
    @property
    def use_t(self): ...
    @use_t.setter
    def use_t(self, value) -> None: ...
    def llf(self): ...
    def bse(self): ...
    def tvalues(self): ...
    def pvalues(self): ...
    def cov_params(self, r_matrix: Any | None = ..., column: Any | None = ..., scale: Any | None = ..., cov_p: Any | None = ..., other: Any | None = ...): ...
    def t_test(self, r_matrix, cov_p: Any | None = ..., use_t: Any | None = ...): ...
    def f_test(self, r_matrix, cov_p: Any | None = ..., invcov: Any | None = ...): ...
    def wald_test(self, r_matrix, cov_p: Any | None = ..., invcov: Any | None = ..., use_f: Any | None = ..., df_constraints: Any | None = ..., scalar: Any | None = ...): ...
    def wald_test_terms(self, skip_single: bool = ..., extra_constraints: Any | None = ..., combine_terms: Any | None = ..., scalar: Any | None = ...): ...
    def t_test_pairwise(self, term_name, method: str = ..., alpha: float = ..., factor_labels: Any | None = ...): ...
    def conf_int(self, alpha: float = ..., cols: Any | None = ...): ...
    def save(self, fname, remove_data: bool = ...) -> None: ...
    @classmethod
    def load(cls, fname): ...
    def remove_data(self) -> None: ...

class LikelihoodResultsWrapper(wrap.ResultsWrapper): ...

class ResultMixin:
    def df_modelwc(self): ...
    def aic(self): ...
    def bic(self): ...
    def score_obsv(self): ...
    def hessv(self): ...
    def covjac(self): ...
    def covjhj(self): ...
    def bsejhj(self): ...
    def bsejac(self): ...
    bootstrap_results: Any
    def bootstrap(self, nrep: int = ..., method: str = ..., disp: int = ..., store: int = ...): ...
    def get_nlfun(self, fun) -> None: ...

class _LLRMixin:
    def pseudo_rsquared(self, kind: str = ...): ...
    def llr(self): ...
    df_lr_null: Any
    def llr_pvalue(self): ...
    def set_null_options(self, llnull: Any | None = ..., attach_results: bool = ..., **kwargs) -> None: ...
    res_null: Any
    k_null: Any
    df_resid_null: Any
    def llnull(self): ...

class GenericLikelihoodModelResults(LikelihoodModelResults, ResultMixin):
    model: Any
    endog: Any
    exog: Any
    nobs: Any
    df_model: Any
    df_resid: Any
    def __init__(self, model, mlefit) -> None: ...
    def summary(self, yname: Any | None = ..., xname: Any | None = ..., title: Any | None = ..., alpha: float = ...): ...
