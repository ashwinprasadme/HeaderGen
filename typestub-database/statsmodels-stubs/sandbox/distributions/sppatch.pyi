from statsmodels.compat.python import lmap as lmap
from typing import Any

def nnlf_fr(self, thetash, x, frmask): ...
def fit_fr(self, data, *args, **kwds): ...
def expect(self, fn: Any | None = ..., args=..., loc: int = ..., scale: int = ..., lb: Any | None = ..., ub: Any | None = ..., conditional: bool = ...): ...
def expect_v2(self, fn: Any | None = ..., args=..., loc: int = ..., scale: int = ..., lb: Any | None = ..., ub: Any | None = ..., conditional: bool = ...): ...
def expect_discrete(self, fn: Any | None = ..., args=..., loc: int = ..., lb: Any | None = ..., ub: Any | None = ..., conditional: bool = ...): ...
def distfitbootstrap(sample, distr, nrepl: int = ...): ...
def distfitmc(sample, distr, nrepl: int = ..., distkwds=...): ...
def printresults(sample, arg, bres, kind: str = ...) -> None: ...