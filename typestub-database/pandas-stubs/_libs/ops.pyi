import numpy as np
from pandas._typing import npt as npt
from typing import Union, Iterable, Literal, overload

def scalar_compare(values: np.ndarray, val: object, op: _BoolOp) -> npt.NDArray[np.bool_]: ...
def vec_compare(left: npt.NDArray[np.object_], right: npt.NDArray[np.object_], op: _BoolOp) -> npt.NDArray[np.bool_]: ...
def scalar_binop(values: np.ndarray, val: object, op: _BinOp) -> np.ndarray: ...
def vec_binop(left: np.ndarray, right: np.ndarray, op: _BinOp) -> np.ndarray: ...
@overload
def maybe_convert_bool(arr: npt.NDArray[np.object_], true_values: Iterable = ..., false_values: Iterable = ..., convert_to_masked_nullable: Literal[False] = ...) -> tuple[np.ndarray, None]: ...