from matplotlib.backend_bases import MouseButton as MouseButton
from typing import Any

class BlockingInput:
    fig: Any
    eventslist: Any
    def __init__(self, fig, eventslist=...) -> None: ...
    def on_event(self, event) -> None: ...
    def post_event(self) -> None: ...
    callbacks: Any
    def cleanup(self) -> None: ...
    def add_event(self, event) -> None: ...
    def pop_event(self, index: int = ...) -> None: ...
    pop: Any
    n: Any
    events: Any
    def __call__(self, n: int = ..., timeout: int = ...): ...

class BlockingMouseInput(BlockingInput):
    button_add: Any
    button_pop: Any
    button_stop: Any
    def __init__(self, fig, mouse_add=..., mouse_pop=..., mouse_stop=...) -> None: ...
    def post_event(self) -> None: ...
    def mouse_event(self) -> None: ...
    def key_event(self) -> None: ...
    def mouse_event_add(self, event) -> None: ...
    def mouse_event_stop(self, event) -> None: ...
    def mouse_event_pop(self, event) -> None: ...
    def add_click(self, event) -> None: ...
    def pop_click(self, event, index: int = ...) -> None: ...
    def pop(self, event, index: int = ...) -> None: ...
    marks: Any
    def cleanup(self, event: Any | None = ...) -> None: ...
    show_clicks: Any
    clicks: Any
    def __call__(self, n: int = ..., timeout: int = ..., show_clicks: bool = ...): ...

class BlockingContourLabeler(BlockingMouseInput):
    cs: Any
    def __init__(self, cs) -> None: ...
    def add_click(self, event) -> None: ...
    def pop_click(self, event, index: int = ...) -> None: ...
    def button1(self, event) -> None: ...
    def button3(self, event) -> None: ...
    inline: Any
    inline_spacing: Any
    def __call__(self, inline, inline_spacing: int = ..., n: int = ..., timeout: int = ...) -> None: ...

class BlockingKeyMouseInput(BlockingInput):
    def __init__(self, fig) -> None: ...
    keyormouse: Any
    def post_event(self) -> None: ...
    def __call__(self, timeout: int = ...): ...
