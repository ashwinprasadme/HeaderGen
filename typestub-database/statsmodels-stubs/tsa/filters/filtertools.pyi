from statsmodels.tools.validation import PandasWrapper as PandasWrapper, array_like as array_like
from typing import Any

def fftconvolveinv(in1, in2, mode: str = ...): ...
def fftconvolve3(in1, in2: Any | None = ..., in3: Any | None = ..., mode: str = ...): ...
def recursive_filter(x, ar_coeff, init: Any | None = ...): ...
def convolution_filter(x, filt, nsides: int = ...): ...
def miso_lfilter(ar, ma, x, useic: bool = ...): ...