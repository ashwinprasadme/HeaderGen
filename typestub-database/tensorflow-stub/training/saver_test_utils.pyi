from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops import gen_lookup_ops as gen_lookup_ops
from tensorflow.python.training import saver as saver_module
from typing import Any

class CheckpointedOp:
    table_ref: Any
    def __init__(self, name, table_ref: Any | None = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def saveable(self): ...
    def insert(self, keys, values): ...
    def lookup(self, keys, default): ...
    def keys(self): ...
    def values(self): ...
    class CustomSaveable(saver_module.BaseSaverBuilder.SaveableObject):
        def __init__(self, table, name) -> None: ...
        def restore(self, restore_tensors, shapes): ...
