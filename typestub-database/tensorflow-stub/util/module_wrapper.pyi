from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.util import fast_module_type as fast_module_type, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.tools.compatibility import all_renames_v2 as all_renames_v2
from typing import Any

FastModuleType: Any
compat_v1_usage_gauge: Any

def get_rename_v2(name): ...
def contains_deprecation_decorator(decorators): ...
def has_deprecation_decorator(symbol): ...

class TFModuleWrapper(FastModuleType):
    compat_v1_usage_recorded: bool
    def __init__(self, wrapped, module_name, public_apis: Any | None = ..., deprecation: bool = ..., has_lite: bool = ...) -> None: ...
    def __setattr__(self, arg, val) -> None: ...
    def __dir__(self): ...
    def __delattr__(self, name) -> None: ...
    def __reduce__(self): ...
