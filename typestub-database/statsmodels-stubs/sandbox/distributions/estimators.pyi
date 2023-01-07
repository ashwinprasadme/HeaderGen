from typing import Any

cache: Any

def gammamomentcond(distfn, params, mom2, quantile: Any | None = ...): ...
def gammamomentcond2(distfn, params, mom2, quantile: Any | None = ...): ...
def momentcondunbound(distfn, params, mom2, quantile: Any | None = ...): ...
def momentcondunboundls(distfn, params, mom2, quantile: Any | None = ..., shape: Any | None = ...): ...
def momentcondquant(distfn, params, mom2, quantile: Any | None = ..., shape: Any | None = ...): ...
def fitquantilesgmm(distfn, x, start: Any | None = ..., pquant: Any | None = ..., frozen: Any | None = ...): ...
def fitbinned(distfn, freq, binedges, start, fixed: Any | None = ...): ...
def fitbinnedgmm(distfn, freq, binedges, start, fixed: Any | None = ..., weightsoptimal: bool = ...): ...
def hess_ndt(fun, pars, args, options): ...
def logmps(params, xsorted, dist): ...
def getstartparams(dist, data): ...
def fit_mps(dist, data, x0: Any | None = ...): ...