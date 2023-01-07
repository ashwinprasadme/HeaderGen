from .initialization import Initialization as Initialization
from .mlemodel import MLEModel as MLEModel, MLEResults as MLEResults, MLEResultsWrapper as MLEResultsWrapper
from .tools import companion_matrix as companion_matrix, constrain_stationary_univariate as constrain_stationary_univariate, diff as diff, is_invertible as is_invertible, prepare_exog as prepare_exog, prepare_trend_data as prepare_trend_data, prepare_trend_spec as prepare_trend_spec, unconstrain_stationary_univariate as unconstrain_stationary_univariate
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.arima.params import SARIMAXParams as SARIMAXParams
from statsmodels.tsa.arima.specification import SARIMAXSpecification as SARIMAXSpecification
from statsmodels.tsa.tsatools import lagmat as lagmat
from typing import Any

class SARIMAX(MLEModel):
    order: Any
    seasonal_order: Any
    seasonal_periods: Any
    measurement_error: Any
    time_varying_regression: Any
    mle_regression: Any
    simple_differencing: Any
    enforce_stationarity: Any
    enforce_invertibility: Any
    hamilton_representation: Any
    concentrate_scale: Any
    use_exact_diffuse: Any
    polynomial_ar: Any
    polynomial_ma: Any
    polynomial_seasonal_ar: Any
    polynomial_seasonal_ma: Any
    trend: Any
    trend_offset: Any
    k_ar: Any
    k_ar_params: Any
    k_diff: Any
    k_ma: Any
    k_ma_params: Any
    k_seasonal_ar: Any
    k_seasonal_ar_params: Any
    k_seasonal_diff: Any
    k_seasonal_ma: Any
    k_seasonal_ma_params: Any
    k_exog: Any
    state_regression: Any
    state_error: Any
    k_params: Any
    orig_endog: Any
    orig_exog: Any
    orig_k_diff: Any
    orig_k_seasonal_diff: Any
    nobs: Any
    k_states: Any
    k_posdef: Any
    def __init__(self, endog, exog: Any | None = ..., order=..., seasonal_order=..., trend: Any | None = ..., measurement_error: bool = ..., time_varying_regression: bool = ..., mle_regression: bool = ..., simple_differencing: bool = ..., enforce_stationarity: bool = ..., enforce_invertibility: bool = ..., hamilton_representation: bool = ..., concentrate_scale: bool = ..., trend_offset: int = ..., use_exact_diffuse: bool = ..., dates: Any | None = ..., freq: Any | None = ..., missing: str = ..., validate_specification: bool = ..., **kwargs) -> None: ...
    def prepare_data(self): ...
    transition_ar_params_idx: Any
    selection_ma_params_idx: Any
    design_ma_params_idx: Any
    def initialize(self) -> None: ...
    loglikelihood_burn: Any
    def initialize_default(self, approximate_diffuse_variance: Any | None = ...) -> None: ...
    def initial_design(self): ...
    def initial_state_intercept(self): ...
    def initial_transition(self): ...
    def initial_selection(self): ...
    def clone(self, endog, exog: Any | None = ..., **kwargs): ...
    def start_params(self): ...
    def endog_names(self, latex: bool = ...): ...
    params_complete: Any
    def param_terms(self): ...
    def param_names(self): ...
    def state_names(self): ...
    def model_orders(self): ...
    def model_names(self): ...
    def model_latex_names(self): ...
    def transform_params(self, unconstrained): ...
    def untransform_params(self, constrained): ...
    def update(self, params, transformed: bool = ..., includes_fixed: bool = ..., complex_step: bool = ...): ...

class SARIMAXResults(MLEResults):
    df_resid: Any
    specification: Any
    polynomial_trend: Any
    polynomial_ar: Any
    polynomial_ma: Any
    polynomial_seasonal_ar: Any
    polynomial_seasonal_ma: Any
    polynomial_reduced_ar: Any
    polynomial_reduced_ma: Any
    model_orders: Any
    param_terms: Any
    def __init__(self, model, params, filter_results, cov_type: Any | None = ..., **kwargs) -> None: ...
    def extend(self, endog, exog: Any | None = ..., **kwargs): ...
    def arroots(self): ...
    def maroots(self): ...
    def arfreq(self): ...
    def mafreq(self): ...
    def arparams(self): ...
    def seasonalarparams(self): ...
    def maparams(self): ...
    def seasonalmaparams(self): ...
    def summary(self, alpha: float = ..., start: Any | None = ...): ...

class SARIMAXResultsWrapper(MLEResultsWrapper): ...