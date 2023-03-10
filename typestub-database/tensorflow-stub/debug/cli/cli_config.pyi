from tensorflow.python.debug.cli import debugger_cli_common as debugger_cli_common
from tensorflow.python.platform import gfile as gfile
from typing import Any

RL: Any

class CLIConfig:
    def __init__(self, config_file_path: Any | None = ...) -> None: ...
    def get(self, property_name): ...
    def set(self, property_name, property_val) -> None: ...
    def set_callback(self, property_name, callback) -> None: ...
    def summarize(self, highlight: Any | None = ...): ...
