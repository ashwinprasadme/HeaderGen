from statsmodels.tsa.regime_switching import markov_switching as markov_switching
from statsmodels.tsa.tsatools import rename_trend as rename_trend
from typing import Any

class MarkovRegression(markov_switching.MarkovSwitching):
    trend: Any
    switching_trend: Any
    switching_exog: Any
    switching_variance: Any
    k_trend: int
    switching_coeffs: Any
    def __init__(self, endog, k_regimes, trend: str = ..., exog: Any | None = ..., order: int = ..., exog_tvtp: Any | None = ..., switching_trend: bool = ..., switching_exog: bool = ..., switching_variance: bool = ..., dates: Any | None = ..., freq: Any | None = ..., missing: str = ...) -> None: ...
    def predict_conditional(self, params): ...
    @property
    def start_params(self): ...
    @property
    def param_names(self): ...
    def transform_params(self, unconstrained): ...
    def untransform_params(self, constrained): ...

class MarkovRegressionResults(markov_switching.MarkovSwitchingResults): ...
class MarkovRegressionResultsWrapper(markov_switching.MarkovSwitchingResultsWrapper): ...
