from . import legend_handler as legend_handler
from matplotlib import colors as colors, docstring as docstring, offsetbox as offsetbox
from matplotlib.artist import Artist as Artist, allow_rasterization as allow_rasterization
from matplotlib.cbook import silent_list as silent_list
from matplotlib.collections import CircleCollection as CircleCollection, Collection as Collection, LineCollection as LineCollection, PathCollection as PathCollection, PolyCollection as PolyCollection, RegularPolyCollection as RegularPolyCollection
from matplotlib.container import BarContainer as BarContainer, ErrorbarContainer as ErrorbarContainer, StemContainer as StemContainer
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.lines import Line2D as Line2D
from matplotlib.offsetbox import AnchoredOffsetbox as AnchoredOffsetbox, DraggableOffsetBox as DraggableOffsetBox, DrawingArea as DrawingArea, HPacker as HPacker, TextArea as TextArea, VPacker as VPacker
from matplotlib.patches import FancyBboxPatch as FancyBboxPatch, Patch as Patch, Rectangle as Rectangle, Shadow as Shadow, StepPatch as StepPatch
from matplotlib.transforms import Bbox as Bbox, BboxBase as BboxBase, BboxTransformFrom as BboxTransformFrom, BboxTransformTo as BboxTransformTo, TransformedBbox as TransformedBbox
from typing import Any

class DraggableLegend(DraggableOffsetBox):
    legend: Any
    def __init__(self, legend, use_blit: bool = ..., update: str = ...) -> None: ...
    def finalize_offset(self) -> None: ...

class Legend(Artist):
    codes: Any
    zorder: int
    prop: Any
    texts: Any
    legendHandles: Any
    isaxes: bool
    axes: Any
    parent: Any
    legendPatch: Any
    def __init__(self, parent, handles, labels, loc: Any | None = ..., numpoints: Any | None = ..., markerscale: Any | None = ..., markerfirst: bool = ..., scatterpoints: Any | None = ..., scatteryoffsets: Any | None = ..., prop: Any | None = ..., fontsize: Any | None = ..., labelcolor: Any | None = ..., borderpad: Any | None = ..., labelspacing: Any | None = ..., handlelength: Any | None = ..., handleheight: Any | None = ..., handletextpad: Any | None = ..., borderaxespad: Any | None = ..., columnspacing: Any | None = ..., ncol: int = ..., mode: Any | None = ..., fancybox: Any | None = ..., shadow: Any | None = ..., title: Any | None = ..., title_fontsize: Any | None = ..., framealpha: Any | None = ..., edgecolor: Any | None = ..., facecolor: Any | None = ..., bbox_to_anchor: Any | None = ..., bbox_transform: Any | None = ..., frameon: Any | None = ..., handler_map: Any | None = ..., title_fontproperties: Any | None = ...) -> None: ...
    stale: bool
    def draw(self, renderer) -> None: ...
    @classmethod
    def get_default_handler_map(cls): ...
    @classmethod
    def set_default_handler_map(cls, handler_map) -> None: ...
    @classmethod
    def update_default_handler_map(cls, handler_map) -> None: ...
    def get_legend_handler_map(self): ...
    @staticmethod
    def get_legend_handler(legend_handler_map, orig_handle): ...
    def get_children(self): ...
    def get_frame(self): ...
    def get_lines(self): ...
    def get_patches(self): ...
    def get_texts(self): ...
    def set_title(self, title, prop: Any | None = ...) -> None: ...
    def get_title(self): ...
    def get_window_extent(self, renderer: Any | None = ...): ...
    def get_tightbbox(self, renderer): ...
    def get_frame_on(self): ...
    def set_frame_on(self, b) -> None: ...
    draw_frame: Any
    def get_bbox_to_anchor(self): ...
    def set_bbox_to_anchor(self, bbox, transform: Any | None = ...) -> None: ...
    def contains(self, event): ...
    def set_draggable(self, state, use_blit: bool = ..., update: str = ...): ...
    def get_draggable(self): ...
