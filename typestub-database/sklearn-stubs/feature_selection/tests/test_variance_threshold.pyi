from sklearn.feature_selection import VarianceThreshold as VarianceThreshold
from sklearn.utils._testing import assert_array_equal as assert_array_equal
from typing import Any

data: Any
data2: Any

def test_zero_variance() -> None: ...
def test_variance_threshold() -> None: ...
def test_variance_negative(X) -> None: ...
def test_zero_variance_floating_point_error() -> None: ...
def test_variance_nan() -> None: ...
