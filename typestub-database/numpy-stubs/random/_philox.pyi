from numpy import dtype as dtype, ndarray as ndarray, uint64 as uint64
from numpy.random.bit_generator import BitGenerator as BitGenerator, SeedSequence as SeedSequence
from numpy.typing import _ArrayLikeInt_co
from typing import Any, Union
from typing_extensions import TypedDict

class _PhiloxInternal(TypedDict):
    counter: ndarray[Any, dtype[uint64]]
    key: ndarray[Any, dtype[uint64]]

class _PhiloxState(TypedDict):
    bit_generator: str
    state: _PhiloxInternal
    buffer: ndarray[Any, dtype[uint64]]
    buffer_pos: int
    has_uint32: int
    uinteger: int

class Philox(BitGenerator):
    def __init__(self, seed: Union[None, _ArrayLikeInt_co, SeedSequence] = ..., counter: Union[None, _ArrayLikeInt_co] = ..., key: Union[None, _ArrayLikeInt_co] = ...) -> None: ...
    @property
    def state(self) -> _PhiloxState: ...
    @state.setter
    def state(self, value: _PhiloxState) -> None: ...
    def jumped(self, jumps: int = ...) -> Philox: ...
    def advance(self, delta: int) -> Philox: ...
