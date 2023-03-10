from tensorflow.python.ops.distributions import distribution

class DirichletMultinomial(distribution.Distribution):
    def __init__(self, total_count, concentration, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def total_count(self): ...
    @property
    def concentration(self): ...
    @property
    def total_concentration(self): ...
