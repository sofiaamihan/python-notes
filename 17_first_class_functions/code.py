# First Class Functions
# Functions that can be passed as arguments to other functions
# Don't include brackets when passing functions as arguments

# Practice of basic syntax
def calculate(*args, operator):
    return operator(*args)

def divide(dividend, divisor):
    if divisor != 0:
        return dividend/divisor
    else:
        raise ZeroDivisionError("Bruh")

print(calculate(20, 4, operator=divide))

# Practice searching via lambda
friends = [
    {
        "name": "daniella",
        "age": 22
    },
    {
        "name": "jilian",
        "age": 18
    }
]

def searching(database, expected, finder):
    for data in database:
        if finder(data) == expected:
            return data
    raise RuntimeError("They aren't here")

print(searching(friends, "daniella", finder = lambda data: data["name"]))

# Example of using built-in functions

from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

print(search(friends, "random", itemgetter("name")))