from statsmodels.compat.python import lfilter as lfilter, lzip as lzip
from typing import Any

class NdKernel:
    weights: Any
    def __init__(self, n, kernels: Any | None = ..., H: Any | None = ...) -> None: ...
    def getH(self): ...
    def setH(self, value) -> None: ...
    H: Any
    def density(self, xs, x): ...
    def __call__(self, x): ...

class CustomKernel:
    domain: Any
    weights: Any
    def __init__(self, shape, h: float = ..., domain: Any | None = ..., norm: Any | None = ...) -> None: ...
    def geth(self): ...
    def seth(self, value) -> None: ...
    h: Any
    def in_domain(self, xs, ys, x): ...
    def density(self, xs, x): ...
    def density_var(self, density, nobs): ...
    def density_confint(self, density, nobs, alpha: float = ...): ...
    def smooth(self, xs, ys, x): ...
    def smoothvar(self, xs, ys, x): ...
    def smoothconf(self, xs, ys, x, alpha: float = ...): ...
    @property
    def L2Norm(self): ...
    @property
    def norm_const(self): ...
    @property
    def kernel_var(self): ...
    def moments(self, n): ...
    @property
    def normal_reference_constant(self): ...
    def weight(self, x): ...
    def __call__(self, x): ...

class Uniform(CustomKernel):
    def __init__(self, h: float = ...): ...

class Triangular(CustomKernel):
    def __init__(self, h: float = ...): ...

class Epanechnikov(CustomKernel):
    def __init__(self, h: float = ...): ...

class Biweight(CustomKernel):
    def __init__(self, h: float = ...): ...
    def smooth(self, xs, ys, x): ...
    def smoothvar(self, xs, ys, x): ...
    def smoothconf_(self, xs, ys, x): ...

class Triweight(CustomKernel):
    def __init__(self, h: float = ...): ...

class Gaussian(CustomKernel):
    def __init__(self, h: float = ...): ...
    def smooth(self, xs, ys, x): ...

class Cosine(CustomKernel):
    def __init__(self, h: float = ...): ...

class Cosine2(CustomKernel):
    def __init__(self, h: float = ...): ...

class Tricube(CustomKernel):
    def __init__(self, h: float = ...): ...
