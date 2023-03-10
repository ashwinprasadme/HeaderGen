import threading

class SaveContext(threading.local):
    def __init__(self) -> None: ...
    def options(self): ...
    def enter_save_context(self, options) -> None: ...
    def exit_save_context(self) -> None: ...
    def in_save_context(self): ...

def save_context(options) -> None: ...
def in_save_context(): ...
def get_save_options(): ...
