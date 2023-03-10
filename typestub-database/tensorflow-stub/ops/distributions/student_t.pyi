from tensorflow.python.ops.distributions import distribution

class StudentT(distribution.Distribution):
    def __init__(self, df, loc, scale, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def df(self): ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...

class StudentTWithAbsDfSoftplusScale(StudentT):
    def __init__(self, df, loc, scale, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
