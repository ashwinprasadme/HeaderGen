import abc
from . import NBitBase as NBitBase
from ._array_like import ArrayLike as ArrayLike
from ._generic_alias import NDArray as NDArray
from ._nbit import _NBitDouble, _NBitInt
from ._scalars import _BoolLike_co, _FloatLike_co, _IntLike_co, _NumberLike_co
from numpy import bool_ as bool_, complex128 as complex128, complexfloating as complexfloating, dtype as dtype, float64 as float64, floating as floating, generic as generic, int8 as int8, int_ as int_, integer as integer, ndarray as ndarray, number as number, signedinteger as signedinteger, timedelta64 as timedelta64, unsignedinteger as unsignedinteger
from typing import Any, NoReturn, Union, overload
from typing_extensions import Protocol as Protocol

HAVE_PROTOCOL: bool

class _BoolOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: _BoolLike_co) -> _GenericType_co: ...
    @overload
    def __call__(self, __other: int) -> int_: ...
    @overload
    def __call__(self, __other: float) -> float64: ...
    @overload
    def __call__(self, __other: complex) -> complex128: ...
    @overload
    def __call__(self, __other: _NumberType) -> _NumberType: ...

class _BoolBitOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: _BoolLike_co) -> _GenericType_co: ...
    @overload
    def __call__(self, __other: int) -> int_: ...
    @overload
    def __call__(self, __other: _IntType) -> _IntType: ...

class _BoolSub(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> NoReturn: ...
    @overload
    def __call__(self, __other: int) -> int_: ...
    @overload
    def __call__(self, __other: float) -> float64: ...
    @overload
    def __call__(self, __other: complex) -> complex128: ...
    @overload
    def __call__(self, __other: _NumberType) -> _NumberType: ...

class _BoolTrueDiv(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: Union[float, _IntLike_co]) -> float64: ...
    @overload
    def __call__(self, __other: complex) -> complex128: ...
    @overload
    def __call__(self, __other: _NumberType) -> _NumberType: ...

class _BoolMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: _BoolLike_co) -> int8: ...
    @overload
    def __call__(self, __other: int) -> int_: ...
    @overload
    def __call__(self, __other: float) -> float64: ...
    @overload
    def __call__(self, __other: _IntType) -> _IntType: ...
    @overload
    def __call__(self, __other: _FloatType) -> _FloatType: ...

class _BoolDivMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: _BoolLike_co) -> _2Tuple[int8]: ...
    @overload
    def __call__(self, __other: int) -> _2Tuple[int_]: ...
    @overload
    def __call__(self, __other: float) -> _2Tuple[floating[Union[_NBit1, _NBitDouble]]]: ...
    @overload
    def __call__(self, __other: _IntType) -> _2Tuple[_IntType]: ...
    @overload
    def __call__(self, __other: _FloatType) -> _2Tuple[_FloatType]: ...

class _TD64Div(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: timedelta64) -> _NumberType_co: ...
    @overload
    def __call__(self, __other: _BoolLike_co) -> NoReturn: ...
    @overload
    def __call__(self, __other: _FloatLike_co) -> timedelta64: ...

class _IntTrueDiv(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> floating[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> floating[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: complex) -> complexfloating[Union[_NBit1, _NBitDouble], Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: integer[_NBit2]) -> floating[Union[_NBit1, _NBit2]]: ...

class _UnsignedIntOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> unsignedinteger[_NBit1]: ...
    @overload
    def __call__(self, __other: Union[int, signedinteger[Any]]) -> Any: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: complex) -> complexfloating[Union[_NBit1, _NBitDouble], Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: unsignedinteger[_NBit2]) -> unsignedinteger[Union[_NBit1, _NBit2]]: ...

class _UnsignedIntBitOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> unsignedinteger[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> signedinteger[Any]: ...
    @overload
    def __call__(self, __other: signedinteger[Any]) -> signedinteger[Any]: ...
    @overload
    def __call__(self, __other: unsignedinteger[_NBit2]) -> unsignedinteger[Union[_NBit1, _NBit2]]: ...

class _UnsignedIntMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> unsignedinteger[_NBit1]: ...
    @overload
    def __call__(self, __other: Union[int, signedinteger[Any]]) -> Any: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: unsignedinteger[_NBit2]) -> unsignedinteger[Union[_NBit1, _NBit2]]: ...

class _UnsignedIntDivMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> _2Tuple[signedinteger[_NBit1]]: ...
    @overload
    def __call__(self, __other: Union[int, signedinteger[Any]]) -> _2Tuple[Any]: ...
    @overload
    def __call__(self, __other: float) -> _2Tuple[floating[Union[_NBit1, _NBitDouble]]]: ...
    @overload
    def __call__(self, __other: unsignedinteger[_NBit2]) -> _2Tuple[unsignedinteger[Union[_NBit1, _NBit2]]]: ...

class _SignedIntOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> signedinteger[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> signedinteger[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: complex) -> complexfloating[Union[_NBit1, _NBitDouble], Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: signedinteger[_NBit2]) -> signedinteger[Union[_NBit1, _NBit2]]: ...

class _SignedIntBitOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> signedinteger[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> signedinteger[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: signedinteger[_NBit2]) -> signedinteger[Union[_NBit1, _NBit2]]: ...

class _SignedIntMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> signedinteger[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> signedinteger[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: signedinteger[_NBit2]) -> signedinteger[Union[_NBit1, _NBit2]]: ...

class _SignedIntDivMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> _2Tuple[signedinteger[_NBit1]]: ...
    @overload
    def __call__(self, __other: int) -> _2Tuple[signedinteger[Union[_NBit1, _NBitInt]]]: ...
    @overload
    def __call__(self, __other: float) -> _2Tuple[floating[Union[_NBit1, _NBitDouble]]]: ...
    @overload
    def __call__(self, __other: signedinteger[_NBit2]) -> _2Tuple[signedinteger[Union[_NBit1, _NBit2]]]: ...

class _FloatOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> floating[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> floating[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: complex) -> complexfloating[Union[_NBit1, _NBitDouble], Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: Union[integer[_NBit2], floating[_NBit2]]) -> floating[Union[_NBit1, _NBit2]]: ...

class _FloatMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> floating[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> floating[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: Union[integer[_NBit2], floating[_NBit2]]) -> floating[Union[_NBit1, _NBit2]]: ...

class _FloatDivMod(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> _2Tuple[floating[_NBit1]]: ...
    @overload
    def __call__(self, __other: int) -> _2Tuple[floating[Union[_NBit1, _NBitInt]]]: ...
    @overload
    def __call__(self, __other: float) -> _2Tuple[floating[Union[_NBit1, _NBitDouble]]]: ...
    @overload
    def __call__(self, __other: Union[integer[_NBit2], floating[_NBit2]]) -> _2Tuple[floating[Union[_NBit1, _NBit2]]]: ...

class _ComplexOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: bool) -> complexfloating[_NBit1, _NBit1]: ...
    @overload
    def __call__(self, __other: int) -> complexfloating[Union[_NBit1, _NBitInt], Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: Union[float, complex]) -> complexfloating[Union[_NBit1, _NBitDouble], Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(self, __other: Union[integer[_NBit2], floating[_NBit2], complexfloating[_NBit2, _NBit2]]) -> complexfloating[Union[_NBit1, _NBit2], Union[_NBit1, _NBit2]]: ...

class _NumberOp:
    def __call__(self, __other: _NumberLike_co) -> Any: ...

class _ComparisonOp(metaclass=abc.ABCMeta):
    @overload
    def __call__(self, __other: _T1) -> bool_: ...
    @overload
    def __call__(self, __other: _T2) -> NDArray[bool_]: ...