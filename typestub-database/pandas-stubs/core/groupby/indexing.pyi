from pandas.core.frame import DataFrame as DataFrame, Series as Series
from pandas._typing import PositionalIndexer as PositionalIndexer
from pandas.core.dtypes.common import is_integer as is_integer, is_list_like as is_list_like
from pandas.core.groupby import groupby as groupby
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Union, Any, Literal

class GroupByIndexingMixin: ...

class GroupByPositionalSelector:
    groupby_object: Any
    def __init__(self, groupby_object: groupby.GroupBy) -> None: ...
    def __getitem__(self, arg: Union[PositionalIndexer, tuple]) -> Union[DataFrame, Series]: ...

class GroupByNthSelector:
    groupby_object: Any
    def __init__(self, groupby_object: groupby.GroupBy) -> None: ...
    def __call__(self, n: Union[PositionalIndexer, tuple], dropna: Literal[any, all, None] = ...) -> Union[DataFrame, Series]: ...
    def __getitem__(self, n: Union[PositionalIndexer, tuple]) -> Union[DataFrame, Series]: ...