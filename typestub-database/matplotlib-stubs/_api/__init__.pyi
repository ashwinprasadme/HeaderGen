from .deprecation import MatplotlibDeprecationWarning as MatplotlibDeprecationWarning, delete_parameter as delete_parameter, deprecate_method_override as deprecate_method_override, deprecate_privatize_attribute as deprecate_privatize_attribute, deprecated as deprecated, make_keyword_only as make_keyword_only, rename_parameter as rename_parameter, suppress_matplotlib_deprecation_warning as suppress_matplotlib_deprecation_warning, warn_deprecated as warn_deprecated
from typing import Any

class classproperty:
    fset: Any
    fdel: Any
    def __init__(self, fget, fset: Any | None = ..., fdel: Any | None = ..., doc: Any | None = ...) -> None: ...
    def __get__(self, instance, owner): ...
    @property
    def fget(self): ...

def check_isinstance(_types, **kwargs): ...
def check_in_list(_values, *, _print_supported_values: bool = ..., **kwargs) -> None: ...
def check_shape(_shape, **kwargs) -> None: ...
def check_getitem(_mapping, **kwargs): ...
def caching_module_getattr(cls): ...
def select_matching_signature(funcs, *args, **kwargs): ...
def warn_external(message, category: Any | None = ...) -> None: ...