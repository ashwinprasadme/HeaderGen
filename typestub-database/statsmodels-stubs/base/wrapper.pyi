from typing import Any

class ResultsWrapper:
    __doc__: Any
    def __init__(self, results) -> None: ...
    def __dir__(self): ...
    def __getattribute__(self, attr): ...
    def save(self, fname, remove_data: bool = ...) -> None: ...
    @classmethod
    def load(cls, fname): ...

def union_dicts(*dicts): ...
def make_wrapper(func, how): ...
def populate_wrapper(klass, wrapping) -> None: ...
