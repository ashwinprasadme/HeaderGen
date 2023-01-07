from numpy import dtype as dtype, int_ as int_, ndarray as ndarray
from numpy.polynomial._polybase import ABCPolyBase as ABCPolyBase
from numpy.polynomial.polyutils import trimcoef as trimcoef
from typing import Any

legtrim = trimcoef

def poly2leg(pol) -> None: ...
def leg2poly(c) -> None: ...

legdomain: ndarray[Any, dtype[int_]]
legzero: ndarray[Any, dtype[int_]]
legone: ndarray[Any, dtype[int_]]
legx: ndarray[Any, dtype[int_]]

def legline(off, scl) -> None: ...
def legfromroots(roots) -> None: ...
def legadd(c1, c2) -> None: ...
def legsub(c1, c2) -> None: ...
def legmulx(c) -> None: ...
def legmul(c1, c2) -> None: ...
def legdiv(c1, c2) -> None: ...
def legpow(c, pow, maxpower=...) -> None: ...
def legder(c, m=..., scl=..., axis=...) -> None: ...
def legint(c, m=..., k=..., lbnd=..., scl=..., axis=...) -> None: ...
def legval(x, c, tensor=...) -> None: ...
def legval2d(x, y, c) -> None: ...
def leggrid2d(x, y, c) -> None: ...
def legval3d(x, y, z, c) -> None: ...
def leggrid3d(x, y, z, c) -> None: ...
def legvander(x, deg) -> None: ...
def legvander2d(x, y, deg) -> None: ...
def legvander3d(x, y, z, deg) -> None: ...
def legfit(x, y, deg, rcond=..., full=..., w=...) -> None: ...
def legcompanion(c) -> None: ...
def legroots(c) -> None: ...
def leggauss(deg) -> None: ...
def legweight(x) -> None: ...

class Legendre(ABCPolyBase):
    domain: Any
    window: Any
    basis_name: Any