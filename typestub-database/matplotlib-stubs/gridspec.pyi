from matplotlib import rcParams as rcParams, tight_layout as tight_layout
from matplotlib.transforms import Bbox as Bbox
from typing import Any

class GridSpecBase:
    def __init__(self, nrows, ncols, height_ratios: Any | None = ..., width_ratios: Any | None = ...) -> None: ...
    nrows: Any
    ncols: Any
    def get_geometry(self): ...
    def get_subplot_params(self, figure: Any | None = ...) -> None: ...
    def new_subplotspec(self, loc, rowspan: int = ..., colspan: int = ...): ...
    def set_width_ratios(self, width_ratios) -> None: ...
    def get_width_ratios(self): ...
    def set_height_ratios(self, height_ratios) -> None: ...
    def get_height_ratios(self): ...
    def get_grid_positions(self, fig, raw: bool = ...): ...
    def __getitem__(self, key): ...
    def subplots(self, *, sharex: bool = ..., sharey: bool = ..., squeeze: bool = ..., subplot_kw: Any | None = ...): ...

class GridSpec(GridSpecBase):
    left: Any
    bottom: Any
    right: Any
    top: Any
    wspace: Any
    hspace: Any
    figure: Any
    def __init__(self, nrows, ncols, figure: Any | None = ..., left: Any | None = ..., bottom: Any | None = ..., right: Any | None = ..., top: Any | None = ..., wspace: Any | None = ..., hspace: Any | None = ..., width_ratios: Any | None = ..., height_ratios: Any | None = ...) -> None: ...
    def update(self, **kwargs) -> None: ...
    def get_subplot_params(self, figure: Any | None = ...): ...
    def locally_modified_subplot_params(self): ...
    def tight_layout(self, figure, renderer: Any | None = ..., pad: float = ..., h_pad: Any | None = ..., w_pad: Any | None = ..., rect: Any | None = ...) -> None: ...

class GridSpecFromSubplotSpec(GridSpecBase):
    figure: Any
    def __init__(self, nrows, ncols, subplot_spec, wspace: Any | None = ..., hspace: Any | None = ..., height_ratios: Any | None = ..., width_ratios: Any | None = ...) -> None: ...
    def get_subplot_params(self, figure: Any | None = ...): ...
    def get_topmost_subplotspec(self): ...

class SubplotSpec:
    num1: Any
    def __init__(self, gridspec, num1, num2: Any | None = ...) -> None: ...
    @property
    def num2(self): ...
    @num2.setter
    def num2(self, value) -> None: ...
    def get_gridspec(self): ...
    def get_geometry(self): ...
    @property
    def rowspan(self): ...
    @property
    def colspan(self): ...
    def is_first_row(self): ...
    def is_last_row(self): ...
    def is_first_col(self): ...
    def is_last_col(self): ...
    def get_position(self, figure, return_all: bool = ...): ...
    def get_topmost_subplotspec(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def subgridspec(self, nrows, ncols, **kwargs): ...
