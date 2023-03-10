import wx
from matplotlib import backend_tools as backend_tools, cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, GraphicsContextBase as GraphicsContextBase, MouseButton as MouseButton, NavigationToolbar2 as NavigationToolbar2, RendererBase as RendererBase, TimerBase as TimerBase, ToolContainerBase as ToolContainerBase, _Backend, cursors as cursors
from matplotlib.backend_managers import ToolManager as ToolManager
from matplotlib.figure import Figure as Figure
from matplotlib.path import Path as Path
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.widgets import SubplotTool as SubplotTool
from typing import Any

PIXELS_PER_INCH: int

class __getattr__:
    IDLE_DELAY: Any
    cursord: Any

def error_msg_wx(msg, parent: Any | None = ...) -> None: ...

class TimerWx(TimerBase):
    def __init__(self, *args, **kwargs) -> None: ...

class RendererWx(RendererBase):
    fontweights: Any
    fontangles: Any
    fontnames: Any
    width: Any
    height: Any
    bitmap: Any
    fontd: Any
    dpi: Any
    gc: Any
    def __init__(self, bitmap, dpi) -> None: ...
    def flipy(self): ...
    def offset_text_height(self): ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
    def get_canvas_width_height(self): ...
    def handle_clip_rectangle(self, gc) -> None: ...
    @staticmethod
    def convert_path(gfx_ctx, path, transform): ...
    def draw_path(self, gc, path, transform, rgbFace: Any | None = ...) -> None: ...
    def draw_image(self, gc, x, y, im) -> None: ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = ..., mtext: Any | None = ...) -> None: ...
    def new_gc(self): ...
    def get_wx_font(self, s, prop): ...
    def points_to_pixels(self, points): ...

class GraphicsContextWx(GraphicsContextBase):
    bitmap: Any
    dc: Any
    gfx_ctx: Any
    renderer: Any
    def __init__(self, bitmap, renderer) -> None: ...
    IsSelected: bool
    def select(self) -> None: ...
    def unselect(self) -> None: ...
    def set_foreground(self, fg, isRGBA: Any | None = ...) -> None: ...
    def set_linewidth(self, w) -> None: ...
    def set_capstyle(self, cs) -> None: ...
    def set_joinstyle(self, js) -> None: ...
    def get_wxcolour(self, color): ...

class _FigureCanvasWxBase(FigureCanvasBase, wx.Panel):
    required_interactive_framework: str
    keyvald: Any
    bitmap: Any
    def __init__(self, parent, id, figure: Any | None = ...) -> None: ...
    def Copy_to_Clipboard(self, event: Any | None = ...) -> None: ...
    def draw_idle(self) -> None: ...
    def flush_events(self) -> None: ...
    def start_event_loop(self, timeout: int = ...) -> None: ...
    def stop_event_loop(self, event: Any | None = ...) -> None: ...
    def gui_repaint(self, drawDC: Any | None = ..., origin: str = ...) -> None: ...
    filetypes: Any
    def print_figure(self, filename, *args, **kwargs) -> None: ...
    def set_cursor(self, cursor) -> None: ...

class FigureCanvasWx(_FigureCanvasWxBase):
    renderer: Any
    def draw(self, drawDC: Any | None = ...) -> None: ...
    print_bmp: Any
    print_jpeg: Any
    print_jpg: Any
    print_pcx: Any
    print_png: Any
    print_tiff: Any
    print_tif: Any
    print_xpm: Any

class FigureFrameWx(wx.Frame):
    num: Any
    canvas: Any
    sizer: Any
    figmgr: Any
    toolbar: Any
    def __init__(self, num, fig) -> None: ...
    @property
    def toolmanager(self): ...
    def get_canvas(self, fig): ...
    def get_figure_manager(self): ...
    def GetToolBar(self): ...
    def Destroy(self, *args, **kwargs): ...

class FigureManagerWx(FigureManagerBase):
    frame: Any
    def __init__(self, canvas, num, frame) -> None: ...
    @property
    def toolbar(self): ...
    @toolbar.setter
    def toolbar(self, value) -> None: ...
    def show(self) -> None: ...
    def destroy(self, *args) -> None: ...
    def full_screen_toggle(self) -> None: ...
    def get_window_title(self): ...
    def set_window_title(self, title) -> None: ...
    def resize(self, width, height) -> None: ...

class NavigationToolbar2Wx(NavigationToolbar2, wx.ToolBar):
    wx_ids: Any
    def __init__(self, canvas, coordinates: bool = ...) -> None: ...
    def get_canvas(self, frame, fig): ...
    def zoom(self, *args) -> None: ...
    def pan(self, *args) -> None: ...
    def save_figure(self, *args) -> None: ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    def set_message(self, s) -> None: ...
    def set_history_buttons(self) -> None: ...

class ToolbarWx(ToolContainerBase, wx.ToolBar):
    def __init__(self, toolmanager, parent, style=...) -> None: ...
    def add_toolitem(self, name, group, position, image_file, description, toggle) -> None: ...
    def toggle_toolitem(self, name, toggled) -> None: ...
    def remove_toolitem(self, name) -> None: ...
    def set_message(self, s) -> None: ...

class ConfigureSubplotsWx(backend_tools.ConfigureSubplotsBase):
    def trigger(self, *args) -> None: ...

class SaveFigureWx(backend_tools.SaveFigureBase):
    def trigger(self, *args) -> None: ...

class SetCursorWx(backend_tools.SetCursorBase):
    def set_cursor(self, cursor) -> None: ...

class RubberbandWx(backend_tools.RubberbandBase):
    def draw_rubberband(self, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...

class _HelpDialog(wx.Dialog):
    headers: Any
    widths: Any
    def __init__(self, parent, help_entries) -> None: ...
    def OnClose(self, event) -> None: ...
    @classmethod
    def show(cls, parent, help_entries) -> None: ...

class HelpWx(backend_tools.ToolHelpBase):
    def trigger(self, *args) -> None: ...

class ToolCopyToClipboardWx(backend_tools.ToolCopyToClipboardBase):
    def trigger(self, *args, **kwargs) -> None: ...

class _BackendWx(_Backend):
    FigureCanvas: Any
    FigureManager: Any
    @classmethod
    def new_figure_manager(cls, num, *args, **kwargs): ...
    @classmethod
    def new_figure_manager_given_figure(cls, num, figure): ...
    @staticmethod
    def mainloop() -> None: ...
