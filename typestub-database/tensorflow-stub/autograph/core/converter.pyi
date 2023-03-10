import enum
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, parser as parser, templates as templates, transformer as transformer
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class Feature(enum.Enum):
    ALL: str
    AUTO_CONTROL_DEPS: str
    ASSERT_STATEMENTS: str
    BUILTIN_FUNCTIONS: str
    EQUALITY_OPERATORS: str
    LISTS: str
    NAME_SCOPES: str
    @classmethod
    def all(cls): ...
    @classmethod
    def all_but(cls, exclude): ...

STANDARD_OPTIONS: Any

class ConversionOptions:
    recursive: Any
    user_requested: Any
    internal_convert_user_code: Any
    optional_features: Any
    def __init__(self, recursive: bool = ..., user_requested: bool = ..., internal_convert_user_code: bool = ..., optional_features=...) -> None: ...
    def as_tuple(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def uses(self, feature): ...
    def call_options(self): ...
    def to_ast(self): ...

class ProgramContext:
    options: Any
    autograph_module: Any
    def __init__(self, options, autograph_module: Any | None = ...) -> None: ...

class Base(transformer.Base):
    def __init__(self, ctx) -> None: ...
    def get_definition_directive(self, node, directive, arg, default): ...
    def visit(self, node): ...
