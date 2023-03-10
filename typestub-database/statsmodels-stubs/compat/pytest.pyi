from _pytest.recwarn import WarningsChecker
from typing import Any, Tuple, Type, Union

class NoWarningsChecker:
    cw: Any
    rec: Any
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type, value, traceback) -> None: ...

def pytest_warns(warning: Union[Type[Warning], Tuple[Type[Warning], ...], None]) -> Union[WarningsChecker, NoWarningsChecker]: ...
