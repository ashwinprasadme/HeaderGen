from sklearn.datasets import clear_data_home as clear_data_home, get_data_home as get_data_home, load_boston as load_boston, load_breast_cancer as load_breast_cancer, load_diabetes as load_diabetes, load_digits as load_digits, load_files as load_files, load_iris as load_iris, load_linnerud as load_linnerud, load_sample_image as load_sample_image, load_sample_images as load_sample_images, load_wine as load_wine
from sklearn.datasets._base import load_csv_data as load_csv_data, load_gzip_compressed_csv_data as load_gzip_compressed_csv_data
from sklearn.datasets.tests.test_common import check_as_frame as check_as_frame
from sklearn.externals._pilutil import pillow_installed as pillow_installed
from sklearn.utils import Bunch as Bunch, IS_PYPY as IS_PYPY
from sklearn.utils._testing import SkipTest as SkipTest

def data_home(tmpdir_factory) -> None: ...
def load_files_root(tmpdir_factory) -> None: ...
def test_category_dir_1(load_files_root) -> None: ...
def test_category_dir_2(load_files_root) -> None: ...
def test_data_home(data_home) -> None: ...
def test_default_empty_load_files(load_files_root) -> None: ...
def test_default_load_files(test_category_dir_1, test_category_dir_2, load_files_root) -> None: ...
def test_load_files_w_categories_desc_and_encoding(test_category_dir_1, test_category_dir_2, load_files_root) -> None: ...
def test_load_files_wo_load_content(test_category_dir_1, test_category_dir_2, load_files_root) -> None: ...
def test_load_csv_data(filename, expected_n_samples, expected_n_features, expected_target_names) -> None: ...
def test_load_csv_data_with_descr() -> None: ...
def test_load_gzip_compressed_csv_data(filename, kwargs, expected_shape) -> None: ...
def test_load_gzip_compressed_csv_data_with_descr() -> None: ...
def test_load_sample_images() -> None: ...
def test_load_sample_image() -> None: ...
def test_load_missing_sample_image_error() -> None: ...
def test_loader(loader_func, data_shape, target_shape, n_target, has_descr, filenames) -> None: ...
def test_toy_dataset_frame_dtype(loader_func, data_dtype, target_dtype) -> None: ...
def test_loads_dumps_bunch() -> None: ...
def test_bunch_pickle_generated_with_0_16_and_read_with_0_17() -> None: ...
def test_bunch_dir() -> None: ...
def test_load_boston_warning() -> None: ...
def test_load_boston_alternative() -> None: ...
