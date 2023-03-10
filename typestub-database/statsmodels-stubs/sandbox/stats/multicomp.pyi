from statsmodels.compat.python import lrange as lrange, lzip as lzip
from statsmodels.graphics import utils as utils
from statsmodels.iolib.table import SimpleTable as SimpleTable
from statsmodels.stats.libqsturng import psturng as psturng, qsturng as qsturng
from statsmodels.stats.multitest import fdrcorrection_twostage as fdrcorrection_twostage, multipletests as multipletests
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning
from typing import Any, NamedTuple

class studentized_range_tuple(NamedTuple):
    ppf: Any
    sf: Any
qcrit: str
res: Any
c: Any
ccols: Any
crows: Any
cv005: Any
cv001: Any

def get_tukeyQcrit(k, df, alpha: float = ...): ...
def get_tukeyQcrit2(k, df, alpha: float = ...): ...
def get_tukey_pvalue(k, df, q): ...
def Tukeythreegene(first, second, third): ...
def Tukeythreegene2(genes) -> None: ...
def catstack(args): ...
def maxzero(x): ...
def maxzerodown(x): ...
def rejectionline(n, alpha: float = ...): ...
def fdrcorrection_bak(pvals, alpha: float = ..., method: str = ...): ...
def mcfdr(nrepl: int = ..., nobs: int = ..., ntests: int = ..., ntrue: int = ..., mu: float = ..., alpha: float = ..., rho: float = ...): ...
def randmvn(rho, size=..., standardize: bool = ...): ...
def tiecorrect(xranks): ...

class GroupsStats:
    x: Any
    useranks: Any
    uni: Any
    intlab: Any
    groupnobs: Any
    def __init__(self, x, useranks: bool = ..., uni: Any | None = ..., intlab: Any | None = ...) -> None: ...
    xx: Any
    groupsum: Any
    groupmean: Any
    groupmeanfilter: Any
    def runbasic_old(self, useranks: bool = ...) -> None: ...
    def runbasic(self, useranks: bool = ...) -> None: ...
    def groupdemean(self): ...
    def groupsswithin(self): ...
    def groupvarwithin(self): ...

class TukeyHSDResults:
    q_crit: Any
    reject: Any
    meandiffs: Any
    std_pairs: Any
    confint: Any
    df_total: Any
    reject2: Any
    variance: Any
    pvalues: Any
    data: Any
    groups: Any
    groupsunique: Any
    def __init__(self, mc_object, results_table, q_crit, reject: Any | None = ..., meandiffs: Any | None = ..., std_pairs: Any | None = ..., confint: Any | None = ..., df_total: Any | None = ..., reject2: Any | None = ..., variance: Any | None = ..., pvalues: Any | None = ...) -> None: ...
    def summary(self): ...
    def plot_simultaneous(self, comparison_name: Any | None = ..., ax: Any | None = ..., figsize=..., xlabel: Any | None = ..., ylabel: Any | None = ...): ...

class MultiComparison:
    data: Any
    groups: Any
    groupsunique: Any
    groupintlab: Any
    datali: Any
    pairindices: Any
    nobs: Any
    ngroups: Any
    def __init__(self, data, groups, group_order: Any | None = ...) -> None: ...
    ranks: Any
    rankdata: Any
    def getranks(self) -> None: ...
    def kruskal(self, pairs: Any | None = ..., multimethod: str = ...): ...
    def allpairtest(self, testfunc, alpha: float = ..., method: str = ..., pvalidx: int = ...): ...
    groupstats: Any
    def tukeyhsd(self, alpha: float = ...): ...

def rankdata(x): ...
def compare_ordered(vals, alpha) -> None: ...
def varcorrection_unbalanced(nobs_all, srange: bool = ...): ...
def varcorrection_pairs_unbalanced(nobs_all, srange: bool = ...): ...
def varcorrection_unequal(var_all, nobs_all, df_all): ...
def varcorrection_pairs_unequal(var_all, nobs_all, df_all): ...
def tukeyhsd(mean_all, nobs_all, var_all, df: Any | None = ..., alpha: float = ..., q_crit: Any | None = ...): ...
def simultaneous_ci(q_crit, var, groupnobs, pairindices: Any | None = ...): ...
def distance_st_range(mean_all, nobs_all, var_all, df: Any | None = ..., triu: bool = ...): ...
def contrast_allpairs(nm): ...
def contrast_all_one(nm): ...
def contrast_diff_mean(nm): ...
def tukey_pvalues(std_range, nm, df): ...
def multicontrast_pvalues(tstat, tcorr, df: Any | None = ..., dist: str = ..., alternative: str = ...): ...

class StepDown:
    vals: Any
    n_vals: Any
    nobs_all: Any
    var_all: Any
    df: Any
    def __init__(self, vals, nobs_all, var_all, df: Any | None = ...) -> None: ...
    def get_crit(self, alpha): ...
    distance_matrix: Any
    def get_distance_matrix(self) -> None: ...
    def iter_subsets(self, indices) -> None: ...
    def check_set(self, indices): ...
    def stepdown(self, indices): ...
    cache_result: Any
    crit: Any
    accepted: Any
    rejected: Any
    def run(self, alpha): ...

def homogeneous_subsets(vals, dcrit): ...
def set_partition(ssli): ...
def set_remove_subs(ssli): ...
