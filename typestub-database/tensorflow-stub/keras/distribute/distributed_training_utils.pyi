from tensorflow.python.keras import backend as backend
from tensorflow.python.ops import variables as variables

def global_batch_size_supported(distribution_strategy): ...
def call_replica_local_fn(fn, *args, **kwargs): ...
def is_distributed_variable(v): ...
