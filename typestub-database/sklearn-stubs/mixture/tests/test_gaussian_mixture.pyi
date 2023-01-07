from sklearn.cluster import KMeans as KMeans
from sklearn.covariance import EmpiricalCovariance as EmpiricalCovariance
from sklearn.datasets import make_spd_matrix as make_spd_matrix
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning, NotFittedError as NotFittedError
from sklearn.metrics.cluster import adjusted_rand_score as adjusted_rand_score
from sklearn.mixture import GaussianMixture as GaussianMixture
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal, ignore_warnings as ignore_warnings
from sklearn.utils.extmath import fast_logdet as fast_logdet
from typing import Any

COVARIANCE_TYPE: Any

def generate_data(n_samples, n_features, weights, means, precisions, covariance_type): ...

class RandomData:
    n_samples: Any
    n_components: Any
    n_features: Any
    weights: Any
    means: Any
    covariances: Any
    precisions: Any
    X: Any
    Y: Any
    def __init__(self, rng, n_samples: int = ..., n_components: int = ..., n_features: int = ..., scale: int = ...) -> None: ...

def test_gaussian_mixture_attributes() -> None: ...
def test_check_weights() -> None: ...
def test_check_means() -> None: ...
def test_check_precisions() -> None: ...
def test_suffstat_sk_full() -> None: ...
def test_suffstat_sk_tied() -> None: ...
def test_suffstat_sk_diag() -> None: ...
def test_gaussian_suffstat_sk_spherical() -> None: ...
def test_compute_log_det_cholesky() -> None: ...
def test_gaussian_mixture_log_probabilities() -> None: ...
def test_gaussian_mixture_estimate_log_prob_resp() -> None: ...
def test_gaussian_mixture_predict_predict_proba() -> None: ...
def test_gaussian_mixture_fit_predict(seed, max_iter, tol) -> None: ...
def test_gaussian_mixture_fit_predict_n_init() -> None: ...
def test_gaussian_mixture_fit() -> None: ...
def test_gaussian_mixture_fit_best_params() -> None: ...
def test_gaussian_mixture_fit_convergence_warning() -> None: ...
def test_multiple_init() -> None: ...
def test_gaussian_mixture_n_parameters() -> None: ...
def test_bic_1d_1component() -> None: ...
def test_gaussian_mixture_aic_bic() -> None: ...
def test_gaussian_mixture_verbose() -> None: ...
def test_warm_start(seed) -> None: ...
def test_convergence_detected_with_warm_start() -> None: ...
def test_score() -> None: ...
def test_score_samples() -> None: ...
def test_monotonic_likelihood() -> None: ...
def test_regularisation() -> None: ...
def test_property() -> None: ...
def test_sample() -> None: ...
def test_init() -> None: ...
def test_gaussian_mixture_setting_best_params() -> None: ...
def test_gaussian_mixture_precisions_init_diag() -> None: ...