from sklearn.metrics import DistanceMetric as DistanceMetric
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._testing import create_memmap_backed_data as create_memmap_backed_data
from sklearn.utils.fixes import parse_version as parse_version, sp_version as sp_version
from typing import Any

def dist_func(x1, x2, p): ...

rng: Any
d: int
n1: int
n2: int
X1: Any
X2: Any
X1_mmap: Any
X2_mmap: Any
X1_bool: Any
X2_bool: Any
X1_bool_mmap: Any
X2_bool_mmap: Any
V: Any
VI: Any
BOOL_METRICS: Any
METRICS_DEFAULT_PARAMS: Any

def check_cdist(metric, kwargs, X1, X2) -> None: ...
def test_cdist(metric_param_grid, X1, X2) -> None: ...
def test_cdist_bool_metric(metric, X1_bool, X2_bool) -> None: ...
def check_cdist_bool(metric, D_true) -> None: ...
def test_pdist(metric_param_grid, X1, X2) -> None: ...
def test_pdist_bool_metrics(metric, X1_bool) -> None: ...
def check_pdist(metric, kwargs, D_true) -> None: ...
def check_pdist_bool(metric, D_true) -> None: ...
def test_pickle(writable_kwargs, metric_param_grid) -> None: ...
def test_pickle_bool_metrics(metric, X1_bool) -> None: ...
def check_pickle(metric, kwargs) -> None: ...
def test_haversine_metric(): ...
def test_pyfunc_metric() -> None: ...
def test_input_data_size(): ...
def test_readonly_kwargs() -> None: ...
