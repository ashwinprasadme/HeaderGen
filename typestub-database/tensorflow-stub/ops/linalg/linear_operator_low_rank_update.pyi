from tensorflow.python.ops.linalg import linear_operator
from typing import Any

class LinearOperatorLowRankUpdate(linear_operator.LinearOperator):
    def __init__(self, base_operator, u, diag_update: Any | None = ..., v: Any | None = ..., is_diag_update_positive: Any | None = ..., is_non_singular: Any | None = ..., is_self_adjoint: Any | None = ..., is_positive_definite: Any | None = ..., is_square: Any | None = ..., name: str = ...) -> None: ...
    @property
    def u(self): ...
    @property
    def v(self): ...
    @property
    def is_diag_update_positive(self): ...
    @property
    def diag_update(self): ...
    @property
    def diag_operator(self): ...
    @property
    def base_operator(self): ...