from matplotlib import cbook as cbook
from matplotlib.backends.backend_agg import RendererAgg as RendererAgg
from matplotlib.tight_bbox import process_figure_for_rasterizing as process_figure_for_rasterizing
from typing import Any

class MixedModeRenderer:
    dpi: Any
    figure: Any
    def __init__(self, figure, width, height, dpi, vector_renderer, raster_renderer_class: Any | None = ..., bbox_inches_restore: Any | None = ...) -> None: ...
    def __getattr__(self, attr): ...
    def start_rasterizing(self) -> None: ...
    def stop_rasterizing(self) -> None: ...
