from sklearn.datasets import load_iris as load_iris
from sklearn.linear_model import LogisticRegression as LogisticRegression
from sklearn.tree import DecisionTreeClassifier as DecisionTreeClassifier, DecisionTreeRegressor as DecisionTreeRegressor

def test_get_response_error(estimator, err_msg, params) -> None: ...
def test_get_response_predict_proba() -> None: ...
def test_get_response_decision_function() -> None: ...