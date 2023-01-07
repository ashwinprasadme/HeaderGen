import numpy as np
from pandas.core._numba.kernels.shared import is_monotonic_increasing as is_monotonic_increasing

def add_sum(val: float, nobs: int, sum_x: float, compensation: float) -> tuple[int, float, float]: ...
def remove_sum(val: float, nobs: int, sum_x: float, compensation: float) -> tuple[int, float, float]: ...
def sliding_sum(values: np.ndarray, start: np.ndarray, end: np.ndarray, min_periods: int) -> np.ndarray: ...