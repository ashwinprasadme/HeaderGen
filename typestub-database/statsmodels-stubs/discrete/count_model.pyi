import statsmodels.regression.linear_model as lm
from statsmodels.discrete.discrete_model import CountModel, CountResults, L1CountResults
from typing import Any

class GenericZeroInflated(CountModel):
    __doc__: Any
    k_inflate: int
    exog_infl: Any
    k_exog: int
    infl: Any
    model_infl: Any
    inflation: Any
    k_extra: Any
    def __init__(self, endog, exog, exog_infl: Any | None = ..., offset: Any | None = ..., inflation: str = ..., exposure: Any | None = ..., missing: str = ..., **kwargs) -> None: ...
    def loglike(self, params): ...
    def loglikeobs(self, params): ...
    def fit(self, start_params: Any | None = ..., method: str = ..., maxiter: int = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., cov_type: str = ..., cov_kwds: Any | None = ..., use_t: Any | None = ..., **kwargs): ...
    def fit_regularized(self, start_params: Any | None = ..., method: str = ..., maxiter: str = ..., full_output: int = ..., disp: int = ..., callback: Any | None = ..., alpha: int = ..., trim_mode: str = ..., auto_trim_tol: float = ..., size_trim_tol: float = ..., qc_tol: float = ..., **kwargs): ...
    def score_obs(self, params): ...
    def score(self, params): ...
    def hessian(self, params): ...
    def predict(self, params, exog: Any | None = ..., exog_infl: Any | None = ..., exposure: Any | None = ..., offset: Any | None = ..., which: str = ...): ...

class ZeroInflatedPoisson(GenericZeroInflated):
    __doc__: Any
    model_main: Any
    distribution: Any
    result_class: Any
    result_class_wrapper: Any
    result_class_reg: Any
    result_class_reg_wrapper: Any
    def __init__(self, endog, exog, exog_infl: Any | None = ..., offset: Any | None = ..., exposure: Any | None = ..., inflation: str = ..., missing: str = ..., **kwargs) -> None: ...

class ZeroInflatedGeneralizedPoisson(GenericZeroInflated):
    __doc__: Any
    model_main: Any
    distribution: Any
    result_class: Any
    result_class_wrapper: Any
    result_class_reg: Any
    result_class_reg_wrapper: Any
    def __init__(self, endog, exog, exog_infl: Any | None = ..., offset: Any | None = ..., exposure: Any | None = ..., inflation: str = ..., p: int = ..., missing: str = ..., **kwargs) -> None: ...

class ZeroInflatedNegativeBinomialP(GenericZeroInflated):
    __doc__: Any
    model_main: Any
    distribution: Any
    result_class: Any
    result_class_wrapper: Any
    result_class_reg: Any
    result_class_reg_wrapper: Any
    def __init__(self, endog, exog, exog_infl: Any | None = ..., offset: Any | None = ..., exposure: Any | None = ..., inflation: str = ..., p: int = ..., missing: str = ..., **kwargs) -> None: ...

class ZeroInflatedPoissonResults(CountResults):
    __doc__: Any
    def get_margeff(self, at: str = ..., method: str = ..., atexog: Any | None = ..., dummy: bool = ..., count: bool = ...) -> None: ...

class L1ZeroInflatedPoissonResults(L1CountResults, ZeroInflatedPoissonResults): ...
class ZeroInflatedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1ZeroInflatedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...

class ZeroInflatedGeneralizedPoissonResults(CountResults):
    __doc__: Any
    def get_margeff(self, at: str = ..., method: str = ..., atexog: Any | None = ..., dummy: bool = ..., count: bool = ...) -> None: ...

class L1ZeroInflatedGeneralizedPoissonResults(L1CountResults, ZeroInflatedGeneralizedPoissonResults): ...
class ZeroInflatedGeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1ZeroInflatedGeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...

class ZeroInflatedNegativeBinomialResults(CountResults):
    __doc__: Any
    def get_margeff(self, at: str = ..., method: str = ..., atexog: Any | None = ..., dummy: bool = ..., count: bool = ...) -> None: ...

class L1ZeroInflatedNegativeBinomialResults(L1CountResults, ZeroInflatedNegativeBinomialResults): ...
class ZeroInflatedNegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class L1ZeroInflatedNegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
