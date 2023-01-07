from statsmodels.stats.moment_helpers import se_cov as se_cov
from typing import Any

def cov_hc0(results): ...
def cov_hc1(results): ...
def cov_hc2(results): ...
def cov_hc3(results): ...
def weights_bartlett(nlags): ...
def weights_uniform(nlags): ...
def cov_cluster(results, group, use_correction: bool = ...): ...
def cov_cluster_2groups(results, group, group2: Any | None = ..., use_correction: bool = ...): ...
def cov_white_simple(results, use_correction: bool = ...): ...
cov_hac = cov_hac_simple

def cov_nw_panel(results, nlags, groupidx, weights_func=..., use_correction: str = ...): ...