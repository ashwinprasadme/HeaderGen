from statsmodels.regression.linear_model import OLS as OLS
from typing import Any

class PanelAR1:
    endog: Any
    exog: Any
    groups_start: Any
    groups_valid: Any
    def __init__(self, endog, exog: Any | None = ..., groups: Any | None = ...) -> None: ...
    def ar1filter(self, xy, alpha): ...
    def fit_conditional(self, alpha): ...
    def fit(self): ...