from testPackage.pythonPackage1.subpackage1 import allVariables as av  # This is a module
from testPackage.pythonPackage1.subpackage1 import calculation as cl  # This is a module
from testPackage.pythonPackage1.subpackage1.bioData import MybioData as mb  # This is a Class

__all__ = ['mb', 'cl', 'av', 'operation']
operation = "done"
privateFunc = "done"
