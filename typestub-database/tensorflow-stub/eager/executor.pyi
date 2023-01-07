from tensorflow.python import pywrap_tfe as pywrap_tfe

class Executor:
    def __init__(self, handle) -> None: ...
    def __del__(self) -> None: ...
    def is_async(self): ...
    def handle(self): ...
    def wait(self) -> None: ...
    def clear_error(self) -> None: ...

def new_executor(enable_async): ...