from statsmodels.genmod import families as families
from statsmodels.genmod.generalized_linear_model import GLM as GLM
from statsmodels.sandbox.nonparametric.smoothers import PolySmoother as PolySmoother
from statsmodels.tools.sm_exceptions import IterationLimitWarning as IterationLimitWarning, iteration_limit_doc as iteration_limit_doc
from typing import Any

DEBUG: bool

def default_smoother(x, s_arg: Any | None = ...): ...

class Offset:
    fn: Any
    offset: Any
    def __init__(self, fn, offset) -> None: ...
    def __call__(self, *args, **kw): ...

class Results:
    Y: Any
    alpha: Any
    smoothers: Any
    offset: Any
    family: Any
    exog: Any
    mu: Any
    def __init__(self, Y, alpha, exog, smoothers, family, offset) -> None: ...
    def __call__(self, exog): ...
    def linkinversepredict(self, exog): ...
    def predict(self, exog): ...
    def smoothed(self, exog): ...
    def smoothed_demeaned(self, exog): ...

class AdditiveModel:
    exog: Any
    weights: Any
    smoothers: Any
    family: Any
    def __init__(self, exog, smoothers: Any | None = ..., weights: Any | None = ..., family: Any | None = ...) -> None: ...
    iter: int
    dev: Any
    def _iter__(self): ...
    def next(self): ...
    def cont(self): ...
    def df_resid(self): ...
    def estimate_scale(self): ...
    rtol: Any
    maxiter: Any
    results: Any
    def fit(self, Y, rtol: float = ..., maxiter: int = ...): ...

class Model(GLM, AdditiveModel):
    def __init__(self, endog, exog, smoothers: Any | None = ..., family=...) -> None: ...
    weights: Any
    results: Any
    def next(self): ...
    def estimate_scale(self, Y: Any | None = ...): ...
    rtol: Any
    maxiter: Any
    Y: Any
    history: Any
    scale: Any
    def fit(self, Y, rtol: float = ..., maxiter: int = ...): ...
