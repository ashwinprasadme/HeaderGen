from typing import Any

class ParametricMixtureD:
    mixing_dist: Any
    base_dist: Any
    ma: Any
    mb: Any
    mixing_probs: Any
    bd_args: Any
    bd_kwds: Any
    def __init__(self, mixing_dist, base_dist, bd_args_func, bd_kwds_func, cutoff: float = ...) -> None: ...
    def rvs(self, size: int = ...): ...
    def pdf(self, x): ...
    def cdf(self, x): ...

class ClippedContinuous:
    base_dist: Any
    clip_lower: Any
    def __init__(self, base_dist, clip_lower) -> None: ...
    def rvs(self, *args, **kwds): ...
    def pdf(self, x, *args, **kwds): ...
    def cdf(self, x, *args, **kwds): ...
    def sf(self, x, *args, **kwds): ...
    def ppf(self, x, *args, **kwds) -> None: ...
    def plot(self, x, *args, **kwds) -> None: ...
