import matplotlib.ticker as ticker
from typing import Any

class UnitDblFormatter(ticker.ScalarFormatter):
    def __call__(self, x, pos: Any | None = ...): ...
    def format_data_short(self, value): ...
    def format_data(self, value): ...