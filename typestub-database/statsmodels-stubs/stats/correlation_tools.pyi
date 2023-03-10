from statsmodels.tools.sm_exceptions import IterationLimitWarning as IterationLimitWarning, iteration_limit_doc as iteration_limit_doc
from statsmodels.tools.tools import Bunch as Bunch
from typing import Any

def clip_evals(x, value: int = ...): ...
def corr_nearest(corr, threshold: float = ..., n_fact: int = ...): ...
def corr_clipped(corr, threshold: float = ...): ...
def cov_nearest(cov, method: str = ..., threshold: float = ..., n_fact: int = ..., return_all: bool = ...): ...

class FactoredPSDMatrix:
    diag: Any
    root: Any
    factor: Any
    scales: Any
    def __init__(self, diag, root) -> None: ...
    def to_matrix(self): ...
    def decorrelate(self, rhs): ...
    def solve(self, rhs): ...
    def logdet(self): ...

def corr_nearest_factor(corr, rank, ctol: float = ..., lam_min: float = ..., lam_max: float = ..., maxiter: int = ...): ...
def cov_nearest_factor_homog(cov, rank): ...
def corr_thresholded(data, minabs: Any | None = ..., max_elt: float = ...): ...

class MultivariateKernel:
    def call(self, x, loc) -> None: ...
    bw: Any
    def set_bandwidth(self, bw) -> None: ...
    def set_default_bw(self, loc, bwm: Any | None = ...) -> None: ...

class GaussianMultivariateKernel(MultivariateKernel):
    def call(self, x, loc): ...

def kernel_covariance(exog, loc, groups, kernel: Any | None = ..., bw: Any | None = ...): ...
