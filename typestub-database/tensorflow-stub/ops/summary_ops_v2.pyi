import threading
from tensorflow.core.framework import graph_pb2 as graph_pb2, summary_pb2 as summary_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, smart_cond as smart_cond, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_resource_variable_ops as gen_resource_variable_ops, gen_summary_ops as gen_summary_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, summary_op_util as summary_op_util
from tensorflow.python.training import training_util as training_util
from tensorflow.python.training.tracking import tracking as tracking
from tensorflow.python.util import deprecation as deprecation, tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _SummaryState(threading.local):
    is_recording: Any
    is_recording_distribution_strategy: bool
    writer: Any
    step: Any
    def __init__(self) -> None: ...

class _SummaryContextManager:
    def __init__(self, writer, step: Any | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc): ...

def should_record_summaries(): ...
def record_if(condition) -> None: ...
def record_summaries_every_n_global_steps(n, global_step: Any | None = ...): ...
def always_record_summaries(): ...
def never_record_summaries(): ...
def get_step(): ...
def set_step(step) -> None: ...

class SummaryWriter:
    def set_as_default(self, step: Any | None = ...) -> None: ...
    def as_default(self, step: Any | None = ...): ...
    def init(self) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

class _ResourceSummaryWriter(SummaryWriter):
    def __init__(self, create_fn, init_op_fn) -> None: ...
    def set_as_default(self, step: Any | None = ...) -> None: ...
    def as_default(self, step: Any | None = ...): ...
    def init(self): ...
    def flush(self): ...
    def close(self): ...

class _MultiMetaclass: ...

class _TrackableResourceSummaryWriter(_ResourceSummaryWriter, tracking.TrackableResource, metaclass=_MultiMetaclass):
    def __init__(self, create_fn, init_op_fn): ...

class _LegacyResourceSummaryWriter(SummaryWriter):
    def __init__(self, resource, init_op_fn) -> None: ...
    def init(self): ...
    def flush(self): ...
    def close(self): ...

class _NoopSummaryWriter(SummaryWriter):
    def set_as_default(self, step: Any | None = ...) -> None: ...
    def as_default(self, step: Any | None = ...) -> None: ...
    def init(self) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

def initialize(graph: Any | None = ..., session: Any | None = ...) -> None: ...
def create_file_writer_v2(logdir, max_queue: Any | None = ..., flush_millis: Any | None = ..., filename_suffix: Any | None = ..., name: Any | None = ..., experimental_trackable: bool = ...): ...
def create_file_writer(logdir, max_queue: Any | None = ..., flush_millis: Any | None = ..., filename_suffix: Any | None = ..., name: Any | None = ...): ...
def create_noop_writer(): ...
def all_v2_summary_ops(): ...
def summary_writer_initializer_op(): ...
def summary_scope(name, default_name: str = ..., values: Any | None = ...) -> None: ...
def write(tag, tensor, step: Any | None = ..., metadata: Any | None = ..., name: Any | None = ...): ...
def write_raw_pb(tensor, step: Any | None = ..., name: Any | None = ...): ...
def summary_writer_function(name, tensor, function, family: Any | None = ...): ...
def generic(name, tensor, metadata: Any | None = ..., family: Any | None = ..., step: Any | None = ...): ...
def scalar(name, tensor, family: Any | None = ..., step: Any | None = ...): ...
def histogram(name, tensor, family: Any | None = ..., step: Any | None = ...): ...
def image(name, tensor, bad_color: Any | None = ..., max_images: int = ..., family: Any | None = ..., step: Any | None = ...): ...
def audio(name, tensor, sample_rate, max_outputs, family: Any | None = ..., step: Any | None = ...): ...
def graph_v1(param, step: Any | None = ..., name: Any | None = ...): ...
def graph(graph_data): ...
def import_event(tensor, name: Any | None = ...): ...
def flush(writer: Any | None = ..., name: Any | None = ...): ...
def eval_dir(model_dir, name: Any | None = ...): ...
def create_summary_file_writer(*args, **kwargs): ...
def run_metadata(name, data, step: Any | None = ...): ...
def run_metadata_graphs(name, data, step: Any | None = ...): ...

class _TraceContext(NamedTuple):
    graph: Any
    profiler: Any

def trace_on(graph: bool = ..., profiler: bool = ...) -> None: ...
def trace_export(name, step: Any | None = ..., profiler_outdir: Any | None = ...) -> None: ...
def trace_off() -> None: ...