from . import tools as tools
from typing import Any

class CFASimulationSmoother:
    model: Any
    prefix_simulation_smoother_map: Any
    def __init__(self, model, cfa_simulation_smoother_classes: Any | None = ...) -> None: ...
    @property
    def posterior_mean(self): ...
    @property
    def posterior_cov_inv_chol_sparse(self): ...
    @property
    def posterior_cov(self): ...
    simulated_state: Any
    def simulate(self, variates: Any | None = ..., update_posterior: bool = ...) -> None: ...
