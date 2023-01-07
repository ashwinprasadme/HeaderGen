from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.debug.lib import debug_utils as debug_utils
from tensorflow.python.debug.wrappers import dumping_wrapper as dumping_wrapper, framework as framework, grpc_wrapper as grpc_wrapper, local_cli_wrapper as local_cli_wrapper
from tensorflow.python.training import session_run_hook as session_run_hook
from typing import Any

class LocalCLIDebugHook(session_run_hook.SessionRunHook):
    def __init__(self, ui_type: str = ..., dump_root: Any | None = ..., thread_name_filter: Any | None = ..., config_file_path: Any | None = ...) -> None: ...
    def add_tensor_filter(self, filter_name, tensor_filter) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class DumpingDebugHook(session_run_hook.SessionRunHook):
    def __init__(self, session_root, watch_fn: Any | None = ..., thread_name_filter: Any | None = ..., log_usage: bool = ...) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class GrpcDebugHook(session_run_hook.SessionRunHook):
    def __init__(self, grpc_debug_server_addresses, watch_fn: Any | None = ..., thread_name_filter: Any | None = ..., log_usage: bool = ...) -> None: ...
    def before_run(self, run_context): ...

class TensorBoardDebugHook(GrpcDebugHook):
    def __init__(self, grpc_debug_server_addresses, thread_name_filter: Any | None = ..., send_traceback_and_source_code: bool = ..., log_usage: bool = ...): ...
    def before_run(self, run_context): ...