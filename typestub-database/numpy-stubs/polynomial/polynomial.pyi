from numpy import dtype as dtype, int_ as int_, ndarray as ndarray
from numpy.polynomial._polybase import ABCPolyBase as ABCPolyBase
from numpy.polynomial.polyutils import trimcoef as trimcoef
from typing import Any

polytrim = trimcoef
polydomain: ndarray[Any, dtype[int_]]
polyzero: ndarray[Any, dtype[int_]]
polyone: ndarray[Any, dtype[int_]]
polyx: ndarray[Any, dtype[int_]]

def polyline(off, scl) -> None: ...
def polyfromroots(roots) -> None: ...
def polyadd(c1, c2) -> None: ...
def polysub(c1, c2) -> None: ...
def polymulx(c) -> None: ...
def polymul(c1, c2) -> None: ...
def polydiv(c1, c2) -> None: ...
def polypow(c, pow, maxpower=...) -> None: ...
def polyder(c, m=..., scl=..., axis=...) -> None: ...
def polyint(c, m=..., k=..., lbnd=..., scl=..., axis=...) -> None: ...
def polyval(x, c, tensor=...) -> None: ...
def polyvalfromroots(x, r, tensor=...) -> None: ...
def polyval2d(x, y, c) -> None: ...
def polygrid2d(x, y, c) -> None: ...
def polyval3d(x, y, z, c) -> None: ...
def polygrid3d(x, y, z, c) -> None: ...
def polyvander(x, deg) -> None: ...
def polyvander2d(x, y, deg) -> None: ...
def polyvander3d(x, y, z, deg) -> None: ...
def polyfit(x, y, deg, rcond=..., full=..., w=...) -> None: ...
def polyroots(c) -> None: ...

class Polynomial(ABCPolyBase):
    domain: Any
    window: Any
    basis_name: Any