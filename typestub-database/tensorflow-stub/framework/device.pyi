from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import device_spec as device_spec
from typing import Any

DeviceSpec: Any

def check_valid(spec) -> None: ...
def is_device_spec(obj): ...
def canonical_name(device): ...
def merge_device(spec): ...

class MergeDevice:
    def __init__(self, spec) -> None: ...
    def __call__(self, node_def): ...
    def shortcut_string_merge(self, node_def): ...
    @property
    def is_null_merge(self): ...