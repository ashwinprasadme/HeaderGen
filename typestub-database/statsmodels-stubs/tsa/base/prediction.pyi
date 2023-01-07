from typing import Any

class PredictionResults:
    dist: Any
    dist_args: Any
    def __init__(self, predicted_mean, var_pred_mean, dist: Any | None = ..., df: Any | None = ..., row_labels: Any | None = ...) -> None: ...
    @property
    def row_labels(self): ...
    @property
    def predicted_mean(self): ...
    @property
    def var_pred_mean(self): ...
    @property
    def se_mean(self): ...
    @property
    def tvalues(self): ...
    def t_test(self, value: int = ..., alternative: str = ...): ...
    def conf_int(self, alpha: float = ...): ...
    def summary_frame(self, alpha: float = ...): ...