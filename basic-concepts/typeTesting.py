import math

from selenium import webdriver


class MyClass:
    def method(self):
        pass


def myfunction():
    return "pass"


myList = []
a = 10.00;
my_class = MyClass()


def printAll():
    print(type(MyClass))  # <class 'type'>
    print(type(my_class))  # class '__main__.MyClass'
    print(type(my_class.method()))  # <class 'NoneType'>, returns the RETURN TYPE
    print((type(my_class.method)))  # <class 'method'>
    print(type(myfunction))  # <class 'function'>
    print(type(myfunction()))  # <class 'str'>
    print(type(math))  # <class 'module'>
    print(type(math.factorial))  # <class 'builtin_function_or_method'>
    print(type(myList))  # <class 'list'>
    print(type(a))  # <class 'float'>
    print(type(webdriver))  # <class 'module'>
    print(type(webdriver.Chrome))  # <class 'abc.ABCMeta'>
    print(type(math.pi))  # <class 'float'>


def printAttr():
    print(hasattr(MyClass, "__class__"))
    print(hasattr(myfunction, "__name__"))
    print(hasattr(math, "__class__"))
    print(hasattr("madhur", "__class__"))


def printHelp():
    print(dir(math))
    print(help(math))
    print(dir(math.factorial))
    print(help(math.factorial))


if __name__ == "__main__":
    printAll()
    printAttr()
    printHelp()
