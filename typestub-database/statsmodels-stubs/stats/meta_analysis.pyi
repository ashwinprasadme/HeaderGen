from statsmodels.stats.base import HolderTuple as HolderTuple
from typing import Any

class CombineResults:
    df_resid: Any
    sd_eff_w_fe_hksj: Any
    sd_eff_w_re_hksj: Any
    h2: Any
    i2: Any
    cache_ci: Any
    def __init__(self, **kwds) -> None: ...
    ci_sample_distr: str
    def conf_int_samples(self, alpha: float = ..., use_t: Any | None = ..., nobs: Any | None = ..., ci_func: Any | None = ...): ...
    def conf_int(self, alpha: float = ..., use_t: Any | None = ...): ...
    def test_homogeneity(self): ...
    def summary_array(self, alpha: float = ..., use_t: Any | None = ...): ...
    def summary_frame(self, alpha: float = ..., use_t: Any | None = ...): ...
    def plot_forest(self, alpha: float = ..., use_t: Any | None = ..., use_exp: bool = ..., ax: Any | None = ..., **kwds): ...

def effectsize_smd(mean1, sd1, nobs1, mean2, sd2, nobs2): ...
def effectsize_2proportions(count1, nobs1, count2, nobs2, statistic: str = ..., zero_correction: Any | None = ..., zero_kwds: Any | None = ...): ...
def combine_effects(effect, variance, method_re: str = ..., row_names: Any | None = ..., use_t: bool = ..., alpha: float = ..., **kwds): ...