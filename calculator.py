def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
 

def divide(a, b):
    if b == 0:
        print("Error")     # Code smell
        return None
    return a / b


def unused_function():
    print("This function is never used")
