import abc
from typing import Any, ClassVar

class ABCPolyBase(abc.ABC, metaclass=abc.ABCMeta):
    __hash__: ClassVar[None]
    __array_ufunc__: ClassVar[None]
    maxpower: ClassVar[int]
    coef: Any
    @property
    @abc.abstractmethod
    def domain(self): ...
    @property
    @abc.abstractmethod
    def window(self): ...
    @property
    @abc.abstractmethod
    def basis_name(self): ...
    def has_samecoef(self, other) -> None: ...
    def has_samedomain(self, other) -> None: ...
    def has_samewindow(self, other) -> None: ...
    def has_sametype(self, other) -> None: ...
    def __init__(self, coef, domain=..., window=...) -> None: ...
    def __format__(self, fmt_str) -> None: ...
    def __call__(self, arg) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> None: ...
    def __neg__(self) -> None: ...
    def __pos__(self) -> None: ...
    def __add__(self, other) -> None: ...
    def __sub__(self, other) -> None: ...
    def __mul__(self, other) -> None: ...
    def __truediv__(self, other) -> None: ...
    def __floordiv__(self, other) -> None: ...
    def __mod__(self, other) -> None: ...
    def __divmod__(self, other) -> None: ...
    def __pow__(self, other) -> None: ...
    def __radd__(self, other) -> None: ...
    def __rsub__(self, other) -> None: ...
    def __rmul__(self, other) -> None: ...
    def __rdiv__(self, other) -> None: ...
    def __rtruediv__(self, other) -> None: ...
    def __rfloordiv__(self, other) -> None: ...
    def __rmod__(self, other) -> None: ...
    def __rdivmod__(self, other) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def copy(self) -> None: ...
    def degree(self) -> None: ...
    def cutdeg(self, deg) -> None: ...
    def trim(self, tol=...) -> None: ...
    def truncate(self, size) -> None: ...
    def convert(self, domain=..., kind=..., window=...) -> None: ...
    def mapparms(self) -> None: ...
    def integ(self, m=..., k=..., lbnd=...) -> None: ...
    def deriv(self, m=...) -> None: ...
    def roots(self) -> None: ...
    def linspace(self, n=..., domain=...) -> None: ...
    @classmethod
    def fit(cls, x, y, deg, domain=..., rcond=..., full=..., w=..., window=...) -> None: ...
    @classmethod
    def fromroots(cls, roots, domain=..., window=...) -> None: ...
    @classmethod
    def identity(cls, domain=..., window=...) -> None: ...
    @classmethod
    def basis(cls, deg, domain=..., window=...) -> None: ...
    @classmethod
    def cast(cls, series, domain=..., window=...) -> None: ...
