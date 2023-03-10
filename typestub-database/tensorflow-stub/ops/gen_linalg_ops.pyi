from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def banded_triangular_solve(matrix, rhs, lower: bool = ..., adjoint: bool = ..., name: Any | None = ...): ...

BandedTriangularSolve: Any

def banded_triangular_solve_eager_fallback(matrix, rhs, lower, adjoint, name, ctx): ...
def batch_cholesky(input, name: Any | None = ...): ...

BatchCholesky: Any

def batch_cholesky_eager_fallback(input, name, ctx): ...
def batch_cholesky_grad(l, grad, name: Any | None = ...): ...

BatchCholeskyGrad: Any

def batch_cholesky_grad_eager_fallback(l, grad, name, ctx): ...
def batch_matrix_determinant(input, name: Any | None = ...): ...

BatchMatrixDeterminant: Any

def batch_matrix_determinant_eager_fallback(input, name, ctx): ...
def batch_matrix_inverse(input, adjoint: bool = ..., name: Any | None = ...): ...

BatchMatrixInverse: Any

def batch_matrix_inverse_eager_fallback(input, adjoint, name, ctx): ...
def batch_matrix_solve(matrix, rhs, adjoint: bool = ..., name: Any | None = ...): ...

BatchMatrixSolve: Any

def batch_matrix_solve_eager_fallback(matrix, rhs, adjoint, name, ctx): ...
def batch_matrix_solve_ls(matrix, rhs, l2_regularizer, fast: bool = ..., name: Any | None = ...): ...

BatchMatrixSolveLs: Any

def batch_matrix_solve_ls_eager_fallback(matrix, rhs, l2_regularizer, fast, name, ctx): ...
def batch_matrix_triangular_solve(matrix, rhs, lower: bool = ..., adjoint: bool = ..., name: Any | None = ...): ...

BatchMatrixTriangularSolve: Any

def batch_matrix_triangular_solve_eager_fallback(matrix, rhs, lower, adjoint, name, ctx): ...
def batch_self_adjoint_eig(input, name: Any | None = ...): ...

BatchSelfAdjointEig: Any

def batch_self_adjoint_eig_eager_fallback(input, name, ctx): ...

class _BatchSelfAdjointEigV2Output(NamedTuple):
    e: Any
    v: Any

def batch_self_adjoint_eig_v2(input, compute_v: bool = ..., name: Any | None = ...): ...

BatchSelfAdjointEigV2: Any

def batch_self_adjoint_eig_v2_eager_fallback(input, compute_v, name, ctx): ...

class _BatchSvdOutput(NamedTuple):
    s: Any
    u: Any
    v: Any

def batch_svd(input, compute_uv: bool = ..., full_matrices: bool = ..., name: Any | None = ...): ...

BatchSvd: Any

def batch_svd_eager_fallback(input, compute_uv, full_matrices, name, ctx): ...
def cholesky(input, name: Any | None = ...): ...

Cholesky: Any

def cholesky_eager_fallback(input, name, ctx): ...
def cholesky_grad(l, grad, name: Any | None = ...): ...

CholeskyGrad: Any

def cholesky_grad_eager_fallback(l, grad, name, ctx): ...

class _EigOutput(NamedTuple):
    e: Any
    v: Any

def eig(input, Tout, compute_v: bool = ..., name: Any | None = ...): ...

Eig: Any

def eig_eager_fallback(input, Tout, compute_v, name, ctx): ...
def einsum(inputs, equation, name: Any | None = ...): ...

Einsum: Any

def einsum_eager_fallback(inputs, equation, name, ctx): ...

class _LogMatrixDeterminantOutput(NamedTuple):
    sign: Any
    log_abs_determinant: Any

def log_matrix_determinant(input, name: Any | None = ...): ...

LogMatrixDeterminant: Any

def log_matrix_determinant_eager_fallback(input, name, ctx): ...

class _LuOutput(NamedTuple):
    lu: Any
    p: Any

def lu(input, output_idx_type=..., name: Any | None = ...): ...

Lu: Any

def lu_eager_fallback(input, output_idx_type, name, ctx): ...
def matrix_determinant(input, name: Any | None = ...): ...

MatrixDeterminant: Any

def matrix_determinant_eager_fallback(input, name, ctx): ...
def matrix_exponential(input, name: Any | None = ...): ...

MatrixExponential: Any

def matrix_exponential_eager_fallback(input, name, ctx): ...
def matrix_inverse(input, adjoint: bool = ..., name: Any | None = ...): ...

MatrixInverse: Any

def matrix_inverse_eager_fallback(input, adjoint, name, ctx): ...
def matrix_logarithm(input, name: Any | None = ...): ...

MatrixLogarithm: Any

def matrix_logarithm_eager_fallback(input, name, ctx): ...
def matrix_solve(matrix, rhs, adjoint: bool = ..., name: Any | None = ...): ...

MatrixSolve: Any

def matrix_solve_eager_fallback(matrix, rhs, adjoint, name, ctx): ...
def matrix_solve_ls(matrix, rhs, l2_regularizer, fast: bool = ..., name: Any | None = ...): ...

MatrixSolveLs: Any

def matrix_solve_ls_eager_fallback(matrix, rhs, l2_regularizer, fast, name, ctx): ...
def matrix_square_root(input, name: Any | None = ...): ...

MatrixSquareRoot: Any

def matrix_square_root_eager_fallback(input, name, ctx): ...
def matrix_triangular_solve(matrix, rhs, lower: bool = ..., adjoint: bool = ..., name: Any | None = ...): ...

MatrixTriangularSolve: Any

def matrix_triangular_solve_eager_fallback(matrix, rhs, lower, adjoint, name, ctx): ...

class _QrOutput(NamedTuple):
    q: Any
    r: Any

def qr(input, full_matrices: bool = ..., name: Any | None = ...): ...

Qr: Any

def qr_eager_fallback(input, full_matrices, name, ctx): ...
def self_adjoint_eig(input, name: Any | None = ...): ...

SelfAdjointEig: Any

def self_adjoint_eig_eager_fallback(input, name, ctx): ...

class _SelfAdjointEigV2Output(NamedTuple):
    e: Any
    v: Any

def self_adjoint_eig_v2(input, compute_v: bool = ..., name: Any | None = ...): ...

SelfAdjointEigV2: Any

def self_adjoint_eig_v2_eager_fallback(input, compute_v, name, ctx): ...

class _SvdOutput(NamedTuple):
    s: Any
    u: Any
    v: Any

def svd(input, compute_uv: bool = ..., full_matrices: bool = ..., name: Any | None = ...): ...

Svd: Any

def svd_eager_fallback(input, compute_uv, full_matrices, name, ctx): ...
def tridiagonal_mat_mul(superdiag, maindiag, subdiag, rhs, name: Any | None = ...): ...

TridiagonalMatMul: Any

def tridiagonal_mat_mul_eager_fallback(superdiag, maindiag, subdiag, rhs, name, ctx): ...
def tridiagonal_solve(diagonals, rhs, partial_pivoting: bool = ..., perturb_singular: bool = ..., name: Any | None = ...): ...

TridiagonalSolve: Any

def tridiagonal_solve_eager_fallback(diagonals, rhs, partial_pivoting, perturb_singular, name, ctx): ...
