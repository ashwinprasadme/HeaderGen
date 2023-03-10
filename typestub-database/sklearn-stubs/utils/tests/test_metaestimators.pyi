from sklearn.utils.metaestimators import available_if as available_if, if_delegate_has_method as if_delegate_has_method
from typing import Any

class Prefix:
    def func(self) -> None: ...

class MockMetaEstimator:
    a_prefix: Any
    def func(self) -> None: ...

def test_delegated_docstring() -> None: ...

class MetaEst:
    sub_est: Any
    better_sub_est: Any
    def __init__(self, sub_est, better_sub_est: Any | None = ...) -> None: ...
    def predict(self) -> None: ...

class MetaEstTestTuple(MetaEst):
    def predict(self) -> None: ...

class MetaEstTestList(MetaEst):
    def predict(self) -> None: ...

class HasPredict:
    def predict(self) -> None: ...

class HasNoPredict: ...

class HasPredictAsNDArray:
    predict: Any

def test_if_delegate_has_method() -> None: ...

class AvailableParameterEstimator:
    available: Any
    def __init__(self, available: bool = ...) -> None: ...
    def available_func(self) -> None: ...

def test_available_if_docstring() -> None: ...
def test_available_if() -> None: ...
def test_available_if_unbound_method() -> None: ...
def test_if_delegate_has_method_numpy_array() -> None: ...
