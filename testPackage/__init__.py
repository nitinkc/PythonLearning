# you can directly access addModule and multiplyModule as tp.addModule and tp.multiplyModule after importing testPackage.
from .subPackage1 import addModule  # not including subtModule
from .subPackage2 import multiplyModule

# MORE COMMON : control what objects are imported when someone imports your package by defining __all__ in __init__.py.
# This limits the objects that are imported when using from muPackage mport *

# include specific modules
__all__ = ['addModule', 'multiplyModule','funcTestPack']

# initialization code that needs to be executed when the package is imported.
print("testPackage is being imported.")

# Define package-level attributes: You can define variables, constants, or functions that are accessible at the package level.
PI = 3.14159  # you can access PI as tp.PI after importing testPackage.


def initFunction():
    return "This is init function."
