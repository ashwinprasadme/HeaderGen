from tensorflow.python.eager import backprop as backprop
from tensorflow.python.framework import config as config, constant_op as constant_op, dtypes as dtypes, ops as ops, test_util as test_util
from tensorflow.python.ops import array_ops as array_ops, gradient_checker as gradient_checker, gradients_impl as gradients_impl, math_ops as math_ops, nn_ops as nn_ops
from tensorflow.python.platform import test as test

class XentOpTestBase(test.TestCase):
    def testSingleClass(self) -> None: ...
    def testNpXent(self) -> None: ...
    def testLabelsBroadcast(self) -> None: ...
    def testShapeMismatch(self) -> None: ...
    def testHalf(self) -> None: ...
    def testFloat(self) -> None: ...
    def testDouble(self) -> None: ...
    def testGradient(self) -> None: ...
    def testGradientLabelWithV2(self) -> None: ...
    def testSecondGradient(self) -> None: ...
    def test3D(self) -> None: ...
    def testZeroDimension(self) -> None: ...
