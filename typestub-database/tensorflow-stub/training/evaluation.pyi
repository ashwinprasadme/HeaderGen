from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, monitored_session as monitored_session, session_run_hook as session_run_hook

class _MultiStepStopAfterNEvalsHook(session_run_hook.SessionRunHook):
    def __init__(self, num_evals, steps_per_run: int = ...) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class _StopAfterNEvalsHook(session_run_hook.SessionRunHook):
    def __init__(self, num_evals, log_progress: bool = ...) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...