from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def eager_py_func(input, token, Tout, is_async: bool = ..., name: Any | None = ...): ...

EagerPyFunc: Any

def eager_py_func_eager_fallback(input, token, Tout, is_async, name, ctx): ...
def py_func(input, token, Tout, name: Any | None = ...): ...

PyFunc: Any

def py_func_eager_fallback(input, token, Tout, name, ctx): ...
def py_func_stateless(input, token, Tout, name: Any | None = ...): ...

PyFuncStateless: Any

def py_func_stateless_eager_fallback(input, token, Tout, name, ctx): ...
