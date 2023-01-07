from pandas._config.config import OptionError as OptionError
from pandas._libs.tslibs import OutOfBoundsDatetime as OutOfBoundsDatetime, OutOfBoundsTimedelta as OutOfBoundsTimedelta
from typing import Union, Any

class IntCastingNaNError(ValueError): ...
class NullFrequencyError(ValueError): ...
class PerformanceWarning(Warning): ...
class UnsupportedFunctionCall(ValueError): ...
class UnsortedIndexError(KeyError): ...
class ParserError(ValueError): ...
class DtypeWarning(Warning): ...
class EmptyDataError(ValueError): ...
class ParserWarning(Warning): ...
class MergeError(ValueError): ...
class AccessorRegistrationWarning(Warning): ...

class AbstractMethodError(NotImplementedError):
    methodtype: Any
    class_instance: Any
    def __init__(self, class_instance, methodtype: str = ...) -> None: ...

class NumbaUtilError(Exception): ...
class DuplicateLabelError(ValueError): ...
class InvalidIndexError(Exception): ...