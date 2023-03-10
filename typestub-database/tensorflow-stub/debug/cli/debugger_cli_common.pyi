from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.platform import gfile as gfile
from typing import Any

HELP_INDENT: str
EXPLICIT_USER_EXIT: str
REGEX_MATCH_LINES_KEY: str
INIT_SCROLL_POS_KEY: str
MAIN_MENU_KEY: str

class CommandLineExit(Exception):
    def __init__(self, exit_token: Any | None = ...) -> None: ...
    @property
    def exit_token(self): ...

class RichLine:
    text: Any
    font_attr_segs: Any
    def __init__(self, text: str = ..., font_attr: Any | None = ...) -> None: ...
    def __add__(self, other): ...
    def __len__(self): ...

def rich_text_lines_from_rich_line_list(rich_text_list, annotations: Any | None = ...): ...
def get_tensorflow_version_lines(include_dependency_versions: bool = ...): ...

class RichTextLines:
    def __init__(self, lines, font_attr_segs: Any | None = ..., annotations: Any | None = ...) -> None: ...
    @property
    def lines(self): ...
    @property
    def font_attr_segs(self): ...
    @property
    def annotations(self): ...
    def num_lines(self): ...
    def slice(self, begin, end): ...
    def extend(self, other) -> None: ...
    def append(self, line, font_attr_segs: Any | None = ...) -> None: ...
    def append_rich_line(self, rich_line) -> None: ...
    def prepend(self, line, font_attr_segs: Any | None = ...) -> None: ...
    def write_to_file(self, file_path) -> None: ...

def regex_find(orig_screen_output, regex, font_attr): ...
def wrap_rich_text_lines(inp, cols): ...

class CommandHandlerRegistry:
    HELP_COMMAND: str
    HELP_COMMAND_ALIASES: Any
    VERSION_COMMAND: str
    VERSION_COMMAND_ALIASES: Any
    def __init__(self) -> None: ...
    def register_command_handler(self, prefix, handler, help_info, prefix_aliases: Any | None = ...) -> None: ...
    def dispatch_command(self, prefix, argv, screen_info: Any | None = ...): ...
    def is_registered(self, prefix): ...
    def get_help(self, cmd_prefix: Any | None = ...): ...
    def set_help_intro(self, help_intro) -> None: ...

class TabCompletionRegistry:
    def __init__(self) -> None: ...
    def register_tab_comp_context(self, context_words, comp_items) -> None: ...
    def deregister_context(self, context_words) -> None: ...
    def extend_comp_items(self, context_word, new_comp_items) -> None: ...
    def remove_comp_items(self, context_word, comp_items) -> None: ...
    def get_completions(self, context_word, prefix): ...

class CommandHistory:
    def __init__(self, limit: int = ..., history_file_path: Any | None = ...) -> None: ...
    def add_command(self, command) -> None: ...
    def most_recent_n(self, n): ...
    def lookup_prefix(self, prefix, n): ...

class MenuItem:
    def __init__(self, caption, content, enabled: bool = ...) -> None: ...
    @property
    def caption(self): ...
    @property
    def type(self): ...
    @property
    def content(self): ...
    def is_enabled(self): ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...

class Menu:
    def __init__(self, name: Any | None = ...) -> None: ...
    def append(self, item) -> None: ...
    def insert(self, index, item) -> None: ...
    def num_items(self): ...
    def captions(self): ...
    def caption_to_item(self, caption): ...
    def format_as_single_line(self, prefix: Any | None = ..., divider: str = ..., enabled_item_attrs: Any | None = ..., disabled_item_attrs: Any | None = ...): ...
