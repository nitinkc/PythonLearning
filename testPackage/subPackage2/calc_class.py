class Calculator:
    def __init__(self):
        pass

    def my_method(self, arg1=None, arg2=None):
        # Check if arg1 is provided
        if arg1 is None:
            raise ValueError("arg1 must be provided")

        # Check if arg2 is provided, if not, set default value
        if arg2 is None:
            arg2 = 20

        # Method implementation
        print("sum = ", arg1 + arg2)

    def addNums(self, **kwargs):
        total = 0
        for key, value in kwargs.items():
            if isinstance(value, int):
                total += value
            else:
                raise ValueError(f"Value '{value}' for key '{key}' is not an integer.")
        return total