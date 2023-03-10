from matplotlib import docstring as docstring
from typing import Any

def window_hanning(x): ...
def window_none(x): ...
def detrend(x, key: Any | None = ..., axis: Any | None = ...): ...
def detrend_mean(x, axis: Any | None = ...): ...
def detrend_none(x, axis: Any | None = ...): ...
def detrend_linear(y): ...
def stride_windows(x, n, noverlap: Any | None = ..., axis: int = ...): ...
def psd(x, NFFT: Any | None = ..., Fs: Any | None = ..., detrend: Any | None = ..., window: Any | None = ..., noverlap: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale_by_freq: Any | None = ...): ...
def csd(x, y, NFFT: Any | None = ..., Fs: Any | None = ..., detrend: Any | None = ..., window: Any | None = ..., noverlap: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale_by_freq: Any | None = ...): ...

complex_spectrum: Any
magnitude_spectrum: Any
angle_spectrum: Any
phase_spectrum: Any

def specgram(x, NFFT: Any | None = ..., Fs: Any | None = ..., detrend: Any | None = ..., window: Any | None = ..., noverlap: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale_by_freq: Any | None = ..., mode: Any | None = ...): ...
def cohere(x, y, NFFT: int = ..., Fs: int = ..., detrend=..., window=..., noverlap: int = ..., pad_to: Any | None = ..., sides: str = ..., scale_by_freq: Any | None = ...): ...

class GaussianKDE:
    dataset: Any
    covariance_factor: Any
    factor: Any
    data_covariance: Any
    data_inv_cov: Any
    covariance: Any
    inv_cov: Any
    norm_factor: Any
    def __init__(self, dataset, bw_method: Any | None = ...): ...
    def scotts_factor(self): ...
    def silverman_factor(self): ...
    def evaluate(self, points): ...
    __call__: Any
