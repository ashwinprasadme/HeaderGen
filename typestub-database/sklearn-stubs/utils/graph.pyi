from ..metrics.pairwise import pairwise_distances as pairwise_distances
from .deprecation import deprecated as deprecated
from typing import Any

def single_source_shortest_path_length(graph, source, *, cutoff: Any | None = ...): ...
def graph_shortest_path(dist_matrix, directed: bool = ..., method: str = ...): ...
