from typing import Any

def bytescale(data, cmin: Any | None = ..., cmax: Any | None = ..., high: int = ..., low: int = ...): ...
def imread(name, flatten: bool = ..., mode: Any | None = ...): ...
def imsave(name, arr, format: Any | None = ...) -> None: ...
def fromimage(im, flatten: bool = ..., mode: Any | None = ...): ...
def toimage(arr, high: int = ..., low: int = ..., cmin: Any | None = ..., cmax: Any | None = ..., pal: Any | None = ..., mode: Any | None = ..., channel_axis: Any | None = ...): ...
def imresize(arr, size, interp: str = ..., mode: Any | None = ...): ...