from sklearn.datasets import load_iris as load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LinearDiscriminantAnalysis
from sklearn.ensemble import BaggingClassifier as BaggingClassifier
from sklearn.feature_selection import SelectFromModel as SelectFromModel
from sklearn.linear_model import Perceptron as Perceptron
from sklearn.pipeline import Pipeline as Pipeline

def test_base() -> None: ...
def test_base_zero_n_estimators() -> None: ...
def test_base_not_int_n_estimators() -> None: ...
def test_set_random_states(): ...
