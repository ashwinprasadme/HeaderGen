from sklearn.base import is_classifier as is_classifier
from sklearn.ensemble import GradientBoostingClassifier as GradientBoostingClassifier
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.tree import DecisionTreeClassifier as DecisionTreeClassifier, DecisionTreeRegressor as DecisionTreeRegressor, export_graphviz as export_graphviz, export_text as export_text, plot_tree as plot_tree
from typing import Any

X: Any
y: Any
y2: Any
w: Any
y_degraded: Any

def test_graphviz_toy() -> None: ...
def test_graphviz_errors() -> None: ...
def test_friedman_mse_in_graphviz() -> None: ...
def test_precision() -> None: ...
def test_export_text_errors() -> None: ...
def test_export_text() -> None: ...
def test_plot_tree_entropy(pyplot) -> None: ...
def test_plot_tree_gini(pyplot) -> None: ...
def test_not_fitted_tree(pyplot) -> None: ...
