from sklearn.cluster import MeanShift as MeanShift, estimate_bandwidth as estimate_bandwidth, get_bin_seeds as get_bin_seeds, mean_shift as mean_shift
from sklearn.datasets import make_blobs as make_blobs
from sklearn.metrics import v_measure_score as v_measure_score
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal
from typing import Any

n_clusters: int
centers: Any
X: Any

def test_estimate_bandwidth() -> None: ...
def test_estimate_bandwidth_1sample() -> None: ...
def test_mean_shift(bandwidth, cluster_all, expected, first_cluster_label) -> None: ...
def test_mean_shift_negative_bandwidth() -> None: ...
def test_estimate_bandwidth_with_sparse_matrix() -> None: ...
def test_parallel() -> None: ...
def test_meanshift_predict() -> None: ...
def test_meanshift_all_orphans() -> None: ...
def test_unfitted() -> None: ...
def test_cluster_intensity_tie() -> None: ...
def test_bin_seeds() -> None: ...
def test_max_iter(max_iter) -> None: ...
def test_mean_shift_zero_bandwidth() -> None: ...
