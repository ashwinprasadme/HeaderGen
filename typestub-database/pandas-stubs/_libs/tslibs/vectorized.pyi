import numpy as np
from datetime import tzinfo
from pandas._libs.tslibs.dtypes import Resolution as Resolution
from pandas._libs.tslibs.offsets import BaseOffset as BaseOffset
from pandas._typing import npt as npt

def dt64arr_to_periodarr(stamps: npt.NDArray[np.int64], freq: int, tz: Union[tzinfo, None]) -> npt.NDArray[np.int64]: ...
def is_date_array_normalized(stamps: npt.NDArray[np.int64], tz: Union[tzinfo, None] = ...) -> bool: ...
def normalize_i8_timestamps(stamps: npt.NDArray[np.int64], tz: Union[tzinfo, None]) -> npt.NDArray[np.int64]: ...
def get_resolution(stamps: npt.NDArray[np.int64], tz: Union[tzinfo, None] = ...) -> Resolution: ...
def ints_to_pydatetime(arr: npt.NDArray[np.int64], tz: Union[tzinfo, None] = ..., freq: Union[str, BaseOffset, None] = ..., fold: bool = ..., box: str = ...) -> npt.NDArray[np.object_]: ...
