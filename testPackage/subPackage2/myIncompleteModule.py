def addition(a, b):
    return (a + b)


def subtract(a, b):  # _ signifies private function
    return sanitize(a - b)


def multiplication(x, y):
    return x * y


def sanitize(x):
    return abs(x)
