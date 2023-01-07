from tensorflow.python.eager import context as context
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def load_op_library(library_filename): ...
def load_file_system_library(library_filename) -> None: ...
def load_library(library_location) -> None: ...
def load_pluggable_device_library(library_location) -> None: ...
def register_filesystem_plugin(plugin_location) -> None: ...