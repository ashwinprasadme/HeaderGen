from statsmodels.distributions.copula.copulas import Copula as Copula
from statsmodels.tools.rng_qrng import check_random_state as check_random_state
from typing import Any

class IndependenceCopula(Copula):
    def __init__(self, k_dim: int = ...) -> None: ...
    def rvs(self, nobs: int = ..., args=..., random_state: Any | None = ...): ...
    def pdf(self, u, args=...): ...
    def cdf(self, u, args=...): ...
    def tau(self): ...
    def plot_pdf(self, *args) -> None: ...

def rvs_kernel(sample, size, bw: int = ..., k_func: Any | None = ..., return_extras: bool = ...): ...
