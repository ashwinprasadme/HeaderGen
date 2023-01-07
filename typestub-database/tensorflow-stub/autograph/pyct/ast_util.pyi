import gast
from tensorflow.python.autograph.pyct import anno as anno, parser as parser, qual_names as qual_names
from typing import Any

class CleanCopier:
    preserve_annos: Any
    def __init__(self, preserve_annos) -> None: ...
    def copy(self, node): ...

def copy_clean(node, preserve_annos: Any | None = ...): ...

class SymbolRenamer(gast.NodeTransformer):
    name_map: Any
    def __init__(self, name_map) -> None: ...
    def visit_Nonlocal(self, node): ...
    def visit_Global(self, node): ...
    def visit_Name(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_FunctionDef(self, node): ...

def rename_symbols(node, name_map): ...
def keywords_to_dict(keywords): ...

class PatternMatcher(gast.NodeVisitor):
    pattern: Any
    pattern_stack: Any
    matches: bool
    def __init__(self, pattern) -> None: ...
    def compare_and_visit(self, node, pattern) -> None: ...
    def no_match(self): ...
    def is_wildcard(self, p): ...
    def generic_visit(self, node): ...

def matches(node, pattern): ...
def apply_to_single_assignments(targets, values, apply_fn) -> None: ...
def parallel_walk(node, other) -> None: ...