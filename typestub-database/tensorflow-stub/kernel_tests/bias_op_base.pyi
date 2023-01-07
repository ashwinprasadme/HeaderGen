from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, test_util as test_util
from tensorflow.python.ops import array_ops as array_ops, gradient_checker as gradient_checker, gradient_checker_v2 as gradient_checker_v2, gradients_impl as gradients_impl, nn_ops as nn_ops
from tensorflow.python.platform import test as test

class BiasAddTestBase(test.TestCase):
    def testNpBias(self) -> None: ...
    def testInputDims(self) -> None: ...
    def testBiasVec(self) -> None: ...
    def testBiasInputsMatch(self) -> None: ...
    def testIntTypes(self) -> None: ...
    def testFloatTypes(self) -> None: ...
    def test4DFloatTypes(self) -> None: ...
    def test5DFloatTypes(self) -> None: ...
    def testGradientTensor2D(self) -> None: ...
    def testGradientTensor3D(self) -> None: ...
    def testGradientTensor4D(self) -> None: ...
    def testGradientTensor5D(self) -> None: ...
    def test1x1Image(self) -> None: ...
    def testEmpty(self) -> None: ...
    def testEmptyGradient(self) -> None: ...