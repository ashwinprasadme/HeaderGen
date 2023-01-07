from tensorflow.python.util import tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export

def is_traceback_filtering_enabled(): ...
def enable_traceback_filtering() -> None: ...
def disable_traceback_filtering() -> None: ...
def include_frame(fname): ...
def filter_traceback(fn): ...