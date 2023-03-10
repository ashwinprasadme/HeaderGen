from scipy import stats
from typing import Any

class gaussian_kde_set_covariance(stats.gaussian_kde):
    covariance: Any
    def __init__(self, dataset, covariance) -> None: ...

class gaussian_kde_covfact(stats.gaussian_kde):
    covfact: Any
    def __init__(self, dataset, covfact: str = ...) -> None: ...
    def covariance_factor(self): ...
    def reset_covfact(self, covfact) -> None: ...

def plotkde(covfact) -> None: ...
def test_kde_1d() -> None: ...
