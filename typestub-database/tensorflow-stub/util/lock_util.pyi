class GroupLock:
    def __init__(self, num_groups: int = ...) -> None: ...
    def group(self, group_id): ...
    def acquire(self, group_id) -> None: ...
    def release(self, group_id) -> None: ...
    class _Context:
        def __init__(self, lock, group_id) -> None: ...
        def __enter__(self) -> None: ...
        def __exit__(self, type_arg, value_arg, traceback_arg) -> None: ...
