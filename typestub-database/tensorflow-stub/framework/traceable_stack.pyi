from typing import Any

class TraceableObject:
    SUCCESS: Any
    HEURISTIC_USED: Any
    FAILURE: Any
    obj: Any
    filename: Any
    lineno: Any
    def __init__(self, obj, filename: Any | None = ..., lineno: Any | None = ...) -> None: ...
    def set_filename_and_line_from_caller(self, offset: int = ...): ...
    def copy_metadata(self): ...

class TraceableStack:
    def __init__(self, existing_stack: Any | None = ...) -> None: ...
    def push_obj(self, obj, offset: int = ...): ...
    def pop_obj(self): ...
    def peek_top_obj(self): ...
    def peek_objs(self): ...
    def peek_traceable_objs(self): ...
    def __len__(self): ...
    def copy(self): ...
