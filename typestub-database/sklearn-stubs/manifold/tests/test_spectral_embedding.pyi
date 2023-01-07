from sklearn.cluster import KMeans as KMeans
from sklearn.datasets import make_blobs as make_blobs
from sklearn.manifold import SpectralEmbedding as SpectralEmbedding, spectral_embedding as spectral_embedding
from sklearn.metrics import normalized_mutual_info_score as normalized_mutual_info_score
from sklearn.metrics.pairwise import rbf_kernel as rbf_kernel
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils._testing import assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal
from typing import Any

centers: Any
n_samples: int
n_clusters: Any
n_features: Any
S: Any
true_labels: Any

def test_sparse_graph_connected_component() -> None: ...
def test_spectral_embedding_two_components(seed: int = ...) -> None: ...
def test_spectral_embedding_precomputed_affinity(X, seed: int = ...) -> None: ...
def test_precomputed_nearest_neighbors_filtering() -> None: ...
def test_spectral_embedding_callable_affinity(X, seed: int = ...): ...
def test_spectral_embedding_amg_solver(seed: int = ...) -> None: ...
def test_spectral_embedding_amg_solver_failure() -> None: ...
def test_pipeline_spectral_clustering(seed: int = ...) -> None: ...
def test_spectral_embedding_unknown_eigensolver(seed: int = ...) -> None: ...
def test_spectral_embedding_unknown_affinity(seed: int = ...) -> None: ...
def test_connectivity(seed: int = ...) -> None: ...
def test_spectral_embedding_deterministic() -> None: ...
def test_spectral_embedding_unnormalized() -> None: ...
def test_spectral_embedding_first_eigen_vector() -> None: ...
def test_spectral_embedding_pairwise_deprecated(affinity) -> None: ...