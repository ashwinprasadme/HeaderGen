from typing import Any

class DeterministicRandomTestTool:
    seed_implementation: Any
    def __init__(self, seed: int = ..., mode: str = ...) -> None: ...
    @property
    def operation_seed(self): ...
    @operation_seed.setter
    def operation_seed(self, value) -> None: ...
    def scope(self): ...
