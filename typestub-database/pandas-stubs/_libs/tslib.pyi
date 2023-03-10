import numpy as np
from datetime import tzinfo
from pandas._typing import npt as npt

def format_array_from_datetime(values: npt.NDArray[np.int64], tz: Union[tzinfo, None] = ..., format: Union[str, None] = ..., na_rep: object = ...) -> npt.NDArray[np.object_]: ...
def array_with_unit_to_datetime(values: np.ndarray, unit: str, errors: str = ...) -> tuple[np.ndarray, Union[tzinfo, None]]: ...
def array_to_datetime(values: npt.NDArray[np.object_], errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., require_iso8601: bool = ..., allow_mixed: bool = ...) -> tuple[np.ndarray, Union[tzinfo, None]]: ...
