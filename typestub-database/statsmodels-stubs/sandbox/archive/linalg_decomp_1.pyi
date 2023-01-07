from statsmodels.tools.decorators import cache_readonly as cache_readonly
from typing import Any

class PlainMatrixArray:
    x: Any
    m: Any
    def __init__(self, data: Any | None = ..., sym: Any | None = ...) -> None: ...
    def minv(self): ...
    def m_y(self, y): ...
    def minv_y(self, y): ...
    def mpinv(self): ...
    def xpinv(self): ...
    def yt_m_y(self, y): ...
    def yt_minv_y(self, y): ...
    def y_m_yt(self, y): ...
    def y_minv_yt(self, y): ...
    def mdet(self): ...
    def mlogdet(self): ...
    def meigh(self): ...
    def mhalf(self): ...
    def minvhalf(self): ...

class SvdArray(PlainMatrixArray):
    sdiag: Any
    sinvdiag: Any
    def __init__(self, data: Any | None = ..., sym: Any | None = ...) -> None: ...
    def minv(self): ...
    def meigh(self): ...
    def mdet(self): ...
    def mlogdet(self): ...
    def mhalf(self): ...
    def xxthalf(self): ...
    def xxtinvhalf(self): ...

class CholArray(PlainMatrixArray):
    def __init__(self, data: Any | None = ..., sym: Any | None = ...) -> None: ...
    def yt_minv_y(self, y): ...

def testcompare(m1, m2) -> None: ...
def tiny2zero(x, eps: float = ...): ...
def maxabs(x): ...