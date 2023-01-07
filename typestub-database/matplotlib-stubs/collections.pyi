from . import artist as artist, cbook as cbook, cm as cm, docstring as docstring, transforms as transforms
from ._enums import CapStyle as CapStyle, JoinStyle as JoinStyle
from typing import Any

class Collection(artist.Artist, cm.ScalarMappable):
    def __init__(self, edgecolors: Any | None = ..., facecolors: Any | None = ..., linewidths: Any | None = ..., linestyles: str = ..., capstyle: Any | None = ..., joinstyle: Any | None = ..., antialiaseds: Any | None = ..., offsets: Any | None = ..., transOffset: Any | None = ..., norm: Any | None = ..., cmap: Any | None = ..., pickradius: float = ..., hatch: Any | None = ..., urls: Any | None = ..., *, zorder: int = ..., **kwargs) -> None: ...
    def get_paths(self): ...
    def set_paths(self) -> None: ...
    def get_transforms(self): ...
    def get_offset_transform(self): ...
    def set_offset_transform(self, transOffset) -> None: ...
    def get_datalim(self, transData): ...
    def get_window_extent(self, renderer): ...
    stale: bool
    def draw(self, renderer) -> None: ...
    def set_pickradius(self, pr) -> None: ...
    def get_pickradius(self): ...
    def contains(self, mouseevent): ...
    def set_urls(self, urls) -> None: ...
    def get_urls(self): ...
    def set_hatch(self, hatch) -> None: ...
    def get_hatch(self): ...
    def set_offsets(self, offsets) -> None: ...
    def get_offsets(self): ...
    def set_linewidth(self, lw) -> None: ...
    def set_linestyle(self, ls) -> None: ...
    def set_capstyle(self, cs) -> None: ...
    def get_capstyle(self): ...
    def set_joinstyle(self, js) -> None: ...
    def get_joinstyle(self): ...
    def set_antialiased(self, aa) -> None: ...
    def set_color(self, c) -> None: ...
    def set_facecolor(self, c) -> None: ...
    def get_facecolor(self): ...
    def get_edgecolor(self): ...
    def set_edgecolor(self, c) -> None: ...
    def set_alpha(self, alpha) -> None: ...
    def get_linewidth(self): ...
    def get_linestyle(self): ...
    def update_scalarmappable(self) -> None: ...
    def get_fill(self): ...
    norm: Any
    cmap: Any
    def update_from(self, other) -> None: ...

class _CollectionWithSizes(Collection):
    def get_sizes(self): ...
    stale: bool
    def set_sizes(self, sizes, dpi: float = ...) -> None: ...
    def draw(self, renderer) -> None: ...

class PathCollection(_CollectionWithSizes):
    stale: bool
    def __init__(self, paths, sizes: Any | None = ..., **kwargs) -> None: ...
    def set_paths(self, paths) -> None: ...
    def get_paths(self): ...
    def legend_elements(self, prop: str = ..., num: str = ..., fmt: Any | None = ..., func=..., **kwargs): ...

class PolyCollection(_CollectionWithSizes):
    stale: bool
    def __init__(self, verts, sizes: Any | None = ..., closed: bool = ..., **kwargs) -> None: ...
    def set_verts(self, verts, closed: bool = ...) -> None: ...
    set_paths: Any
    def set_verts_and_codes(self, verts, codes) -> None: ...

class BrokenBarHCollection(PolyCollection):
    def __init__(self, xranges, yrange, **kwargs) -> None: ...
    @classmethod
    def span_where(cls, x, ymin, ymax, where, **kwargs): ...

class RegularPolyCollection(_CollectionWithSizes):
    def __init__(self, numsides, rotation: int = ..., sizes=..., **kwargs) -> None: ...
    def get_numsides(self): ...
    def get_rotation(self): ...
    def draw(self, renderer) -> None: ...

class StarPolygonCollection(RegularPolyCollection): ...
class AsteriskPolygonCollection(RegularPolyCollection): ...

class LineCollection(Collection):
    def __init__(self, segments, *args, zorder: int = ..., **kwargs) -> None: ...
    stale: bool
    def set_segments(self, segments) -> None: ...
    set_verts: Any
    set_paths: Any
    def get_segments(self): ...
    def set_color(self, c) -> None: ...
    set_colors: Any
    def get_color(self): ...
    get_colors: Any

class EventCollection(LineCollection):
    def __init__(self, positions, orientation: str = ..., lineoffset: int = ..., linelength: int = ..., linewidth: Any | None = ..., color: Any | None = ..., linestyle: str = ..., antialiased: Any | None = ..., **kwargs) -> None: ...
    def get_positions(self): ...
    def set_positions(self, positions) -> None: ...
    def add_positions(self, position) -> None: ...
    extend_positions: Any
    append_positions: Any
    def is_horizontal(self): ...
    def get_orientation(self): ...
    stale: bool
    def switch_orientation(self) -> None: ...
    def set_orientation(self, orientation) -> None: ...
    def get_linelength(self): ...
    def set_linelength(self, linelength) -> None: ...
    def get_lineoffset(self): ...
    def set_lineoffset(self, lineoffset) -> None: ...
    def get_linewidth(self): ...
    def get_linewidths(self): ...
    def get_color(self): ...

class CircleCollection(_CollectionWithSizes):
    def __init__(self, sizes, **kwargs) -> None: ...

class EllipseCollection(Collection):
    def __init__(self, widths, heights, angles, units: str = ..., **kwargs) -> None: ...
    def draw(self, renderer) -> None: ...

class PatchCollection(Collection):
    def __init__(self, patches, match_original: bool = ..., **kwargs): ...
    def set_paths(self, patches) -> None: ...

class TriMesh(Collection):
    def __init__(self, triangulation, **kwargs) -> None: ...
    def get_paths(self): ...
    def set_paths(self) -> None: ...
    @staticmethod
    def convert_mesh_to_paths(tri): ...
    def draw(self, renderer) -> None: ...

class QuadMesh(Collection):
    def __init__(self, *args, **kwargs): ...
    def get_paths(self): ...
    stale: bool
    def set_paths(self) -> None: ...
    def set_array(self, A): ...
    def get_datalim(self, transData): ...
    def get_coordinates(self): ...
    @staticmethod
    def convert_mesh_to_paths(meshWidth, meshHeight, coordinates): ...
    def convert_mesh_to_triangles(self, meshWidth, meshHeight, coordinates): ...
    def draw(self, renderer) -> None: ...
    def get_cursor_data(self, event): ...