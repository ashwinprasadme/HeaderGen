from sklearn.utils._weight_vector import WeightVector32 as WeightVector32, WeightVector64 as WeightVector64

def test_type_invariance(dtype, WeightVector) -> None: ...