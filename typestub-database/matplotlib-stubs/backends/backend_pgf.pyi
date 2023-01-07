from matplotlib import cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, GraphicsContextBase as GraphicsContextBase, RendererBase as RendererBase, _Backend
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.figure import Figure as Figure
from matplotlib.path import Path as Path
from typing import Any

def get_fontspec(): ...
def get_preamble(): ...

latex_pt_to_in: Any
latex_in_to_pt: Any
mpl_pt_to_in: Any
mpl_in_to_pt: Any
NO_ESCAPE: str
re_mathsep: Any

def common_texification(text): ...
def writeln(fh, line) -> None: ...
def make_pdf_to_png_converter(): ...

class LatexError(Exception):
    latex_output: Any
    def __init__(self, message, latex_output: str = ...) -> None: ...

class LatexManager:
    tmpdir: Any
    texcommand: Any
    latex_header: Any
    latex: Any
    def __init__(self) -> None: ...
    str_cache: Any
    def get_width_height_descent(self, text, prop): ...

class RendererPgf(RendererBase):
    dpi: Any
    fh: Any
    figure: Any
    image_counter: int
    def __init__(self, figure, fh) -> None: ...
    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace: Any | None = ...) -> None: ...
    def draw_path(self, gc, path, transform, rgbFace: Any | None = ...) -> None: ...
    def option_scale_image(self): ...
    def option_image_nocomposite(self): ...
    def draw_image(self, gc, x, y, im, transform: Any | None = ...) -> None: ...
    def draw_tex(self, gc, x, y, s, prop, angle, ismath: str = ..., mtext: Any | None = ...) -> None: ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = ..., mtext: Any | None = ...) -> None: ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
    def flipy(self): ...
    def get_canvas_width_height(self): ...
    def points_to_pixels(self, points): ...

class TmpDirCleaner:
    def remaining_tmpdirs(cls): ...
    @staticmethod
    def add(tmpdir) -> None: ...
    @staticmethod
    def cleanup_remaining_tmpdirs(): ...

class FigureCanvasPgf(FigureCanvasBase):
    filetypes: Any
    def get_default_filetype(self): ...
    def print_pgf(self, fname_or_fh, **kwargs) -> None: ...
    def print_pdf(self, fname_or_fh, *, metadata: Any | None = ..., **kwargs) -> None: ...
    def print_png(self, fname_or_fh, **kwargs) -> None: ...
    def get_renderer(self): ...
    def draw(self): ...
FigureManagerPgf = FigureManagerBase

class _BackendPgf(_Backend):
    FigureCanvas: Any

class PdfPages:
    keep_empty: Any
    def __init__(self, filename, *, keep_empty: bool = ..., metadata: Any | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def close(self) -> None: ...
    def savefig(self, figure: Any | None = ..., **kwargs) -> None: ...
    def get_pagecount(self): ...