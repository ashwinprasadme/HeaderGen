from typing import Union, Any

class TablePlotter:
    cell_width: Any
    cell_height: Any
    font_size: Any
    def __init__(self, cell_width: float = ..., cell_height: float = ..., font_size: float = ...) -> None: ...
    def plot(self, left, right, labels: Any | None = ..., vertical: bool = ...): ...
