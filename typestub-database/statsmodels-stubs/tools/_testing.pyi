from typing import Any

class PytestTester:
    package_path: Any
    package_name: Any
    def __init__(self, package_path: Any | None = ...) -> None: ...
    def __call__(self, extra_args: Any | None = ..., exit: bool = ...) -> None: ...

def check_ttest_tvalues(results) -> None: ...
def check_ftest_pvalues(results) -> None: ...
def check_fitted(results) -> None: ...
def check_predict_types(results) -> None: ...