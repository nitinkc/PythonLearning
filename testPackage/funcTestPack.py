def testPackFunc():
    print("I am from Test Package")


def myfunc(x):
    return [num for num in range(x) if num % 2 == 0]


list1 = myfunc(11)
testString = "Testing"
