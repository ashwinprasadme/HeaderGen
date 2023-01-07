from sklearn.datasets import load_iris as load_iris
from sklearn.linear_model import Perceptron as Perceptron
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_array_almost_equal as assert_array_almost_equal
from typing import Any

iris: Any
random_state: Any
indices: Any
X: Any
y: Any
X_csr: Any

class MyPerceptron:
    n_iter: Any
    def __init__(self, n_iter: int = ...) -> None: ...
    w: Any
    b: float
    def fit(self, X, y) -> None: ...
    def project(self, X): ...
    def predict(self, X): ...

def test_perceptron_accuracy() -> None: ...
def test_perceptron_correctness() -> None: ...
def test_undefined_methods() -> None: ...
def test_perceptron_l1_ratio() -> None: ...