from sklearn import config_context as config_context
from sklearn.datasets.tests.test_common import check_return_X_y as check_return_X_y
from sklearn.externals._arff import ArffContainerType as ArffContainerType
from sklearn.utils import is_scalar_nan as is_scalar_nan
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_array_equal as assert_array_equal, fails_if_pypy as fails_if_pypy
from typing import Any

OPENML_TEST_DATA_MODULE: str
test_offline: bool
fetch_openml: Any

class _MockHTTPResponse:
    data: Any
    is_gzip: Any
    def __init__(self, data, is_gzip) -> None: ...
    def read(self, amt: int = ...): ...
    def close(self) -> None: ...
    def info(self): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

def test_feature_to_dtype(feature, expected_dtype) -> None: ...
def test_feature_to_dtype_error(feature) -> None: ...
def test_fetch_openml_iris_pandas(monkeypatch) -> None: ...
def test_fetch_openml_iris_pandas_equal_to_no_frame(monkeypatch) -> None: ...
def test_fetch_openml_iris_multitarget_pandas(monkeypatch) -> None: ...
def test_fetch_openml_anneal_pandas(monkeypatch) -> None: ...
def test_fetch_openml_cpu_pandas(monkeypatch) -> None: ...
def test_fetch_openml_australian_pandas_error_sparse(monkeypatch) -> None: ...
def test_fetch_openml_as_frame_auto(monkeypatch) -> None: ...
def test_convert_arff_data_dataframe_warning_low_memory_pandas(monkeypatch) -> None: ...
def test_fetch_openml_adultcensus_pandas_return_X_y(monkeypatch) -> None: ...
def test_fetch_openml_adultcensus_pandas(monkeypatch) -> None: ...
def test_fetch_openml_miceprotein_pandas(monkeypatch) -> None: ...
def test_fetch_openml_emotions_pandas(monkeypatch) -> None: ...
def test_fetch_openml_titanic_pandas(monkeypatch) -> None: ...
def test_fetch_openml_iris(monkeypatch, gzip_response) -> None: ...
def test_decode_iris(monkeypatch) -> None: ...
def test_fetch_openml_iris_multitarget(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_anneal(monkeypatch, gzip_response) -> None: ...
def test_decode_anneal(monkeypatch) -> None: ...
def test_fetch_openml_anneal_multitarget(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_cpu(monkeypatch, gzip_response) -> None: ...
def test_decode_cpu(monkeypatch) -> None: ...
def test_fetch_openml_australian(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_adultcensus(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_miceprotein(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_emotions(monkeypatch, gzip_response) -> None: ...
def test_decode_emotions(monkeypatch) -> None: ...
def test_open_openml_url_cache(monkeypatch, gzip_response, tmpdir) -> None: ...
def test_open_openml_url_unlinks_local_path(monkeypatch, gzip_response, tmpdir, write_to_disk) -> None: ...
def test_retry_with_clean_cache(tmpdir): ...
def test_retry_with_clean_cache_http_error(tmpdir) -> None: ...
def test_fetch_openml_cache(monkeypatch, gzip_response, tmpdir) -> None: ...
def test_fetch_openml_notarget(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_inactive(monkeypatch, gzip_response) -> None: ...
def test_fetch_nonexiting(monkeypatch, gzip_response) -> None: ...
def test_raises_illegal_multitarget(monkeypatch, gzip_response) -> None: ...
def test_warn_ignore_attribute(monkeypatch, gzip_response) -> None: ...
def test_string_attribute_without_dataframe(monkeypatch, gzip_response) -> None: ...
def test_dataset_with_openml_error(monkeypatch, gzip_response) -> None: ...
def test_dataset_with_openml_warning(monkeypatch, gzip_response) -> None: ...
def test_illegal_column(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_raises_missing_values_target(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_raises_illegal_argument() -> None: ...
def test_fetch_openml_with_ignored_feature(monkeypatch, gzip_response) -> None: ...
def test_fetch_openml_verify_checksum(monkeypatch, as_frame, cache, tmpdir): ...
def test_convert_arff_data_type() -> None: ...
def test_missing_values_pandas(monkeypatch) -> None: ...
