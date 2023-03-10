from sklearn import datasets as datasets
from sklearn.datasets import load_iris as load_iris
from sklearn.decomposition import PCA as PCA
from sklearn.utils._testing import assert_allclose as assert_allclose
from typing import Any

iris: Any
PCA_SOLVERS: Any

def test_pca(svd_solver, n_components) -> None: ...
def test_no_empty_slice_warning() -> None: ...
def test_whitening(solver, copy) -> None: ...
def test_pca_explained_variance_equivalence_solver(svd_solver) -> None: ...
def test_pca_explained_variance_empirical(X, svd_solver) -> None: ...
def test_pca_singular_values_consistency(svd_solver) -> None: ...
def test_pca_singular_values(svd_solver) -> None: ...
def test_pca_check_projection(svd_solver) -> None: ...
def test_pca_check_projection_list(svd_solver) -> None: ...
def test_pca_inverse(svd_solver, whiten) -> None: ...
def test_pca_validation(svd_solver, data, n_components, err_msg) -> None: ...
def test_n_components_none(data, solver, n_components_) -> None: ...
def test_n_components_mle(svd_solver) -> None: ...
def test_n_components_mle_error(svd_solver) -> None: ...
def test_pca_dim() -> None: ...
def test_infer_dim_1() -> None: ...
def test_infer_dim_2() -> None: ...
def test_infer_dim_3() -> None: ...
def test_infer_dim_by_explained_variance(X, n_components, n_components_validated) -> None: ...
def test_pca_score(svd_solver) -> None: ...
def test_pca_score3() -> None: ...
def test_pca_sanity_noise_variance(svd_solver) -> None: ...
def test_pca_score_consistency_solvers(svd_solver) -> None: ...
def test_pca_zero_noise_variance_edge_cases(svd_solver) -> None: ...
def test_pca_svd_solver_auto(data, n_components, expected_solver) -> None: ...
def test_pca_sparse_input(svd_solver) -> None: ...
def test_pca_bad_solver() -> None: ...
def test_pca_deterministic_output(svd_solver) -> None: ...
def test_pca_dtype_preservation(svd_solver) -> None: ...
def check_pca_float_dtype_preservation(svd_solver) -> None: ...
def check_pca_int_dtype_upcast_to_double(svd_solver) -> None: ...
def test_pca_n_components_mostly_explained_variance_ratio() -> None: ...
def test_assess_dimension_bad_rank() -> None: ...
def test_small_eigenvalues_mle() -> None: ...
def test_mle_redundant_data() -> None: ...
def test_fit_mle_too_few_samples() -> None: ...
def test_mle_simple_case() -> None: ...
def test_assess_dimesion_rank_one() -> None: ...
