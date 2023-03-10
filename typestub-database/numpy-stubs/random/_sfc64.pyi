from numpy import dtype as dtype, ndarray as ndarray, uint64 as uint64
from numpy.random.bit_generator import BitGenerator as BitGenerator, SeedSequence as SeedSequence
from numpy.typing import _ArrayLikeInt_co
from typing import Any, Union
from typing_extensions import TypedDict

class _SFC64Internal(TypedDict):
    state: ndarray[Any, dtype[uint64]]

class _SFC64State(TypedDict):
    bit_generator: str
    state: _SFC64Internal
    has_uint32: int
    uinteger: int

class SFC64(BitGenerator):
    def __init__(self, seed: Union[None, _ArrayLikeInt_co, SeedSequence] = ...) -> None: ...
    @property
    def state(self) -> _SFC64State: ...
    @state.setter
    def state(self, value: _SFC64State) -> None: ...
