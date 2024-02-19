from testPackage.subPackage2.calc_class import Calculator

# Create an instance of the Calculator class
obj = Calculator()

# Call my_method using named arguments
obj.my_method(arg1=10, arg2=20)

calc = Calculator()
# Call the addNums method with keyword arguments
result = calc.addNums(x1=1, x2=2, x3=3)
print("Sum of numbers:", result)  # Output: Sum of numbers: 6
