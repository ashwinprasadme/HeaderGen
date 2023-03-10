from tensorflow.python import tf2 as tf2
from typing import Any

ENABLE_CONTROL_FLOW_V2: Any

def enable_control_flow_v2() -> None: ...
def EnableControlFlowV2(graph): ...
def IsInXLAContext(op): ...
def InXlaContext(graph): ...
def GraphOrParentsInXlaContext(graph): ...
def IsInWhileLoop(op): ...
def IsInCond(op): ...
def IsSwitch(op): ...
def IsMerge(op): ...
def IsLoopEnter(op): ...
def IsLoopExit(op): ...
def IsCondSwitch(op): ...
def IsCondMerge(op): ...
def IsLoopSwitch(op): ...
def IsLoopMerge(op): ...
def IsLoopConstantEnter(op): ...
def GetLoopConstantEnter(value): ...
def GetOutputContext(op): ...
def GetContainingWhileContext(ctxt, stop_ctxt: Any | None = ...): ...
def GetContainingXLAContext(ctxt): ...
def GetContainingCondContext(ctxt): ...
def IsContainingContext(ctxt, maybe_containing_ctxt): ...
def OpInContext(op, ctxt): ...
def TensorInContext(tensor, ctxt): ...
def CheckInputFromValidContext(op, input_op) -> None: ...
def GetWhileContext(op): ...
