from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.core.protobuf.tpu import tpu_embedding_configuration_pb2 as tpu_embedding_configuration_pb2
from tensorflow.python.distribute import device_util as device_util, distribute_utils as distribute_utils, distribution_strategy_context as distribution_strategy_context, sharded_variable as sharded_variable, tpu_strategy as tpu_strategy
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, embedding_ops as embedding_ops, math_ops as math_ops, sparse_ops as sparse_ops, variable_scope as variable_scope, variables as tf_variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.saved_model import save_context as save_context
from tensorflow.python.tpu import tpu as tpu, tpu_embedding_v2_utils as tpu_embedding_v2_utils
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.training.saving import saveable_hook as saveable_hook
from tensorflow.python.training.tracking import base as base, tracking as tracking
from tensorflow.python.types import core as core
from tensorflow.python.util import compat as compat, nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Callable, Dict, Iterable, List, Optional, Text, Tuple, Union

class TPUShardedVariable(sharded_variable.ShardedVariableMixin): ...

class TPUEmbedding(tracking.AutoTrackable):
    def __init__(self, feature_config: Union[tpu_embedding_v2_utils.FeatureConfig, Iterable], optimizer: Optional[tpu_embedding_v2_utils._Optimizer], pipeline_execution_with_tensor_core: bool = ...) -> None: ...
    def build(self, per_replica_batch_size: Optional[int] = ...): ...
    @property
    def embedding_tables(self) -> Dict[tpu_embedding_v2_utils.TableConfig, tf_variables.Variable]: ...
    def apply_gradients(self, gradients, name: Optional[Text] = ...): ...
    def dequeue(self, name: Optional[Text] = ...): ...
    def enqueue(self, features, weights: Any | None = ..., training: bool = ..., name: Optional[Text] = ..., device: Optional[Text] = ...): ...

class TPUEmbeddingSaveable(saveable_hook.SaveableHook):
    def __init__(self, name: Text, load: Callable[[], Any], retrieve: Callable[[], Any]) -> None: ...
    def before_save(self) -> None: ...
    def after_restore(self) -> None: ...

def cpu_embedding_lookup(inputs, weights, tables, feature_config): ...
def get_list_of_hosts(strategy: tpu_strategy.TPUStrategy) -> List[Text]: ...
def extract_variable_info(kwargs) -> Tuple[Text, Tuple[int, ...], dtypes.DType, Callable[[], Any]]: ...
def make_sharded_variable_creator(hosts: List[Text]) -> Callable[..., TPUShardedVariable]: ...