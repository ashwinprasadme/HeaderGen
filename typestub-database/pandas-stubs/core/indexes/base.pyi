import numpy as np
from pandas import DataFrame, Series
from pandas._typing import ArrayLike, Dtype, DtypeObj, Shape, npt
from pandas.core.arrays import ExtensionArray
from pandas.core.base import IndexOpsMixin, PandasObject
from pandas.io.formats.printing import PrettyDict
from typing import Union, Any, Callable, Hashable, Literal, Sequence

str_t = str

class Index(IndexOpsMixin, PandasObject):
    str: Any
    def __new__(cls, data: Any | None = ..., dtype: Any | None = ..., copy: bool = ..., name: Any | None = ..., tupleize_cols: bool = ..., **kwargs) -> Index: ...
    @property
    def asi8(self) -> None: ...
    def is_(self, other) -> bool: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype: Any | None = ...) -> np.ndarray: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str_t, *inputs, **kwargs): ...
    def __array_wrap__(self, result, context: Any | None = ...): ...
    def dtype(self) -> DtypeObj: ...
    def ravel(self, order: str = ...): ...
    def view(self, cls: Any | None = ...): ...
    def astype(self, dtype, copy: bool = ...): ...
    def take(self, indices, axis: int = ..., allow_fill: bool = ..., fill_value: Any | None = ..., **kwargs): ...
    def repeat(self, repeats, axis: Any | None = ...): ...
    def copy(self, name: Union[Hashable, None] = ..., deep: bool = ..., dtype: Union[Dtype, None] = ..., names: Union[Sequence[Hashable], None] = ...) -> _IndexT: ...
    def __copy__(self, **kwargs) -> _IndexT: ...
    def __deepcopy__(self, memo: Any | None = ...) -> _IndexT: ...
    def format(self, name: bool = ..., formatter: Union[Callable, None] = ..., na_rep: str_t = ...) -> list[str_t]: ...
    def to_native_types(self, slicer: Any | None = ..., **kwargs) -> np.ndarray: ...
    def to_flat_index(self): ...
    def to_series(self, index: Any | None = ..., name: Hashable = ...) -> Series: ...
    def to_frame(self, index: bool = ..., name: Hashable = ...) -> DataFrame: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value: Hashable): ...
    names: Any
    def set_names(self, names, level: Any | None = ..., inplace: bool = ...): ...
    def rename(self, name, inplace: bool = ...): ...
    @property
    def nlevels(self) -> int: ...
    def sortlevel(self, level: Any | None = ..., ascending: bool = ..., sort_remaining: Any | None = ...): ...
    get_level_values: Any
    def droplevel(self, level: int = ...): ...
    @property
    def is_monotonic(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_integer(self) -> bool: ...
    def is_floating(self) -> bool: ...
    def is_numeric(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_categorical(self) -> bool: ...
    def is_interval(self) -> bool: ...
    def is_mixed(self) -> bool: ...
    def holds_integer(self) -> bool: ...
    def inferred_type(self) -> str_t: ...
    def is_all_dates(self) -> bool: ...
    def __reduce__(self): ...
    def hasnans(self) -> bool: ...
    def isna(self) -> npt.NDArray[np.bool_]: ...
    isnull: Any
    def notna(self) -> npt.NDArray[np.bool_]: ...
    notnull: Any
    def fillna(self, value: Any | None = ..., downcast: Any | None = ...): ...
    def dropna(self, how: str_t = ...) -> _IndexT: ...
    def unique(self, level: Union[Hashable, None] = ...) -> _IndexT: ...
    def drop_duplicates(self, keep: Union[str_t, bool] = ...) -> _IndexT: ...
    def duplicated(self, keep: Literal[first, last, False] = ...) -> npt.NDArray[np.bool_]: ...
    def __iadd__(self, other): ...
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __xor__(self, other): ...
    def __nonzero__(self) -> None: ...
    __bool__: Any
    def union(self, other, sort: Any | None = ...): ...
    def intersection(self, other, sort: bool = ...): ...
    def difference(self, other, sort: Any | None = ...): ...
    def symmetric_difference(self, other, result_name: Any | None = ..., sort: Any | None = ...): ...
    def get_loc(self, key, method: Any | None = ..., tolerance: Any | None = ...): ...
    def get_indexer(self, target, method: Union[str_t, None] = ..., limit: Union[int, None] = ..., tolerance: Any | None = ...) -> npt.NDArray[np.intp]: ...
    def reindex(self, target, method: Any | None = ..., level: Any | None = ..., limit: Any | None = ..., tolerance: Any | None = ...) -> tuple[Index, Union[npt.NDArray[np.intp], None]]: ...
    def join(self, other, how: str_t = ..., level: Any | None = ..., return_indexers: bool = ..., sort: bool = ...): ...
    @property
    def values(self) -> ArrayLike: ...
    def array(self) -> ExtensionArray: ...
    def memory_usage(self, deep: bool = ...) -> int: ...
    def where(self, cond, other: Any | None = ...) -> Index: ...
    def is_type_compatible(self, kind: str_t) -> bool: ...
    def __contains__(self, key: Any) -> bool: ...
    __hash__: None
    def __setitem__(self, key, value) -> None: ...
    def __getitem__(self, key): ...
    def append(self, other: Union[Index, Sequence[Index]]) -> Index: ...
    def putmask(self, mask, value) -> Index: ...
    def equals(self, other: Any) -> bool: ...
    def identical(self, other) -> bool: ...
    def asof(self, label): ...
    def asof_locs(self, where: Index, mask: np.ndarray) -> npt.NDArray[np.intp]: ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ..., na_position: str_t = ..., key: Union[Callable, None] = ...): ...
    def sort(self, *args, **kwargs) -> None: ...
    def shift(self, periods: int = ..., freq: Any | None = ...) -> None: ...
    def argsort(self, *args, **kwargs) -> npt.NDArray[np.intp]: ...
    def get_value(self, series: Series, key): ...
    def set_value(self, arr, key, value) -> None: ...
    def get_indexer_non_unique(self, target) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...
    def get_indexer_for(self, target) -> npt.NDArray[np.intp]: ...
    def groupby(self, values) -> PrettyDict[Hashable, np.ndarray]: ...
    def map(self, mapper, na_action: Any | None = ...): ...
    def isin(self, values, level: Any | None = ...) -> np.ndarray: ...
    def slice_indexer(self, start: Union[Hashable, None] = ..., end: Union[Hashable, None] = ..., step: Union[int, None] = ..., kind=...) -> slice: ...
    def get_slice_bound(self, label, side: Literal[left, right], kind=...) -> int: ...
    def slice_locs(self, start: Any | None = ..., end: Any | None = ..., step: Any | None = ..., kind=...) -> tuple[int, int]: ...
    def delete(self, loc) -> _IndexT: ...
    def insert(self, loc: int, item) -> Index: ...
    def drop(self, labels, errors: str_t = ...) -> Index: ...
    def __abs__(self): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __invert__(self): ...
    def any(self, *args, **kwargs): ...
    def all(self, *args, **kwargs): ...
    def argmin(self, axis: Any | None = ..., skipna: bool = ..., *args, **kwargs): ...
    def argmax(self, axis: Any | None = ..., skipna: bool = ..., *args, **kwargs): ...
    def min(self, axis: Any | None = ..., skipna: bool = ..., *args, **kwargs): ...
    def max(self, axis: Any | None = ..., skipna: bool = ..., *args, **kwargs): ...
    @property
    def shape(self) -> Shape: ...