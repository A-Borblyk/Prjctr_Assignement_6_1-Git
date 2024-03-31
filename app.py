import sys

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
except ValueError:
    print("Please provide numeric arguments.")
    sys.exit(1)


def add_two_numbers(a, b):
    return x + y


def subtract_two_numbers(a, b):
    return x - y


def multiply_two_numbers(a, b):
    return x * y


def divide_two_numbers(a, b):
    return x / y


print(add_two_numbers(x, y))
print(subtract_two_numbers(x, y))
print(multiply_two_numbers(x, y))
print(divide_two_numbers(x, y))
