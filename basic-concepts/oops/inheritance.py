class Parent:
    def __init__(self, wealth=None, marriage=None):
        self.wealth = wealth
        self.marriage = marriage

    def setMarriage(self):
        print("Running from Parent")
        print(f" Parents choice is : {self.marriage}")

    def printParent(self):
        print(f" Parents wealth is : {self.wealth} and Parents marriage is {self.marriage}")


class Child(Parent):
    def __init__(self, wealth, marriage, education):
        super().__init__(wealth, marriage)
        self.education = education

    def setMarriage(self):  # Overriding Parents method
        print(f" Child choice is : {self.marriage}")


c = Child(123, "Sonam", "MS")
c.setMarriage()
c.printParent()
