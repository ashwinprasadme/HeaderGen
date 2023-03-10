def get_qualified_name(function): ...
def add_notice_to_docstring(doc, instructions, no_doc_str, suffix_str, notice): ...
def validate_callable(func, decorator_name) -> None: ...

class classproperty:
    def __init__(self, func) -> None: ...
    def __get__(self, owner_self, owner_cls): ...

class _CachedClassProperty:
    def __init__(self, func) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, value) -> None: ...
    def __delete__(self, obj) -> None: ...

def cached_classproperty(func): ...
