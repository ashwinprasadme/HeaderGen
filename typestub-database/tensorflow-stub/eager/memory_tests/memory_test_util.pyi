from tensorflow.python.eager import context as context

def assert_no_leak(f, num_iters: int = ..., increase_threshold_absolute_mb: int = ...) -> None: ...
def memory_profiler_is_available(): ...
