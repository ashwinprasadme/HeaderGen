from typing import Any

def kl_divergence(distribution_a, distribution_b, allow_nan_stats: bool = ..., name: Any | None = ...): ...

class RegisterKL:
    def __init__(self, dist_cls_a, dist_cls_b) -> None: ...
    def __call__(self, kl_fn): ...