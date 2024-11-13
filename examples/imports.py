import math
import sys

# import legb  # the module is executed on import
from legb import X, func as legb_func
# import pypackage.pymodule
from pypackage import pymodule

print(math.sqrt(9))
# print(legb.X)
print(X)
# legb_func(1)

# print(pypackage.pymodule.pyvar)
# pypackage.pymodule.pyfunc()

print(pymodule.pyvar)
pymodule.pyfunc()

print(sys.path)
