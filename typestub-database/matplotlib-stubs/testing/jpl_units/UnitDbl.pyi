from typing import Any

class UnitDbl:
    allowed: Any
    def __init__(self, value, units) -> None: ...
    def convert(self, units): ...
    def __abs__(self): ...
    def __neg__(self): ...
    def __bool__(self): ...
    __eq__: Any
    __ne__: Any
    __lt__: Any
    __le__: Any
    __gt__: Any
    __ge__: Any
    __add__: Any
    __sub__: Any
    __mul__: Any
    __rmul__: Any
    def type(self): ...
    @staticmethod
    def range(start, stop, step: Any | None = ...): ...
    def checkSameUnits(self, rhs, func) -> None: ...