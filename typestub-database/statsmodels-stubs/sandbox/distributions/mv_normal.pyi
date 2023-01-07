from .extras import mvnormcdf as mvnormcdf
from statsmodels.sandbox.distributions.multivariate import mvstdtprob as mvstdtprob
from typing import Any

def expect_mc(dist, func=..., size: int = ...): ...
def expect_mc_bounds(dist, func=..., size: int = ..., lower: Any | None = ..., upper: Any | None = ..., conditional: bool = ..., overfact: float = ...): ...
def bivariate_normal(x, mu, cov): ...

class BivariateNormal:
    mean: Any
    cov: Any
    nvars: int
    def __init__(self, mean, cov) -> None: ...
    def rvs(self, size: int = ...): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...
    def cdf(self, x): ...
    def expect(self, func=..., lower=..., upper=...): ...
    def kl(self, other): ...
    def kl_mc(self, other, size: int = ...): ...

class MVElliptical:
    extra_args: Any
    mean: Any
    sigma: Any
    nvars: Any
    sigmainv: Any
    cholsigmainv: Any
    logdetsigma: Any
    def __init__(self, mean, sigma, *args, **kwds) -> None: ...
    def rvs(self, size: int = ...) -> None: ...
    def logpdf(self, x) -> None: ...
    def cdf(self, x, **kwds) -> None: ...
    def affine_transformed(self, shift, scale_matrix) -> None: ...
    def whiten(self, x): ...
    def pdf(self, x): ...
    def standardize(self, x): ...
    def standardized(self): ...
    def normalize(self, x): ...
    def normalized(self, demeaned: bool = ...): ...
    def normalized2(self, demeaned: bool = ...): ...
    @property
    def std(self): ...
    @property
    def std_sigma(self): ...
    @property
    def corr(self): ...
    expect_mc: Any
    def marginal(self, indices): ...

class MVNormal0:
    mean: Any
    cov: Any
    nvars: Any
    covinv: Any
    cholcovinv: Any
    logdetcov: Any
    def __init__(self, mean, cov) -> None: ...
    def whiten(self, x): ...
    def rvs(self, size: int = ...): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...
    expect_mc: Any

class MVNormal(MVElliptical):
    def rvs(self, size: int = ...): ...
    def logpdf(self, x): ...
    def cdf(self, x, **kwds): ...
    @property
    def cov(self): ...
    def affine_transformed(self, shift, scale_matrix): ...
    def conditional(self, indices, values): ...

np_log: Any
np_pi: Any
sps_gamln: Any

class MVT(MVElliptical):
    extra_args: Any
    df: Any
    def __init__(self, mean, sigma, df) -> None: ...
    def rvs(self, size: int = ...): ...
    def logpdf(self, x): ...
    def cdf(self, x, **kwds): ...
    @property
    def cov(self): ...
    def affine_transformed(self, shift, scale_matrix): ...

def quad2d(func=..., lower=..., upper=...): ...