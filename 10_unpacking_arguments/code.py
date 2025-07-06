# args - the variable name
# * - it takes in an unlimited number of arguments as a tuple
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 5))

# * - splits the list such that each item in the list is taken as one parameter
def add(x, y):
    return x+y

nums = [4, 6]
print(add(*nums))

# ** - pass in each key as a named argument
# long version --> add(x=nums["x"], y=nums["y"])
nums = {
    "x": 4,
    "y": 6
}
print(add(**nums))

# Collect all the arguments as a tuple in front but a compulsory named argument at the back
def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # args is a tuple so you need * to split into individual params
    else:
        return "No function executed."

print(apply(1, 2, 3, 4, operator="*"))



