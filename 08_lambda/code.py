# Long Version
def add(x, y):
    return x + y
print(add(5,3))

# Short Version
subtract = lambda x, y: x-y
print(subtract(5, 3))

# Syntax
# lambda params : return value
# Directly apply the function on the return value

test = [1, 2, 3, 4, 5]

# Practice 1
# Create a lambda function that will square each value in this list
square = lambda x: x**2
new_list = [square(result) for result in test]
print(new_list)

# Practice 2
# Use map()
# map() executes a specified function for each item in the list
new_list2 = list(map(lambda x:x**2, test))
print(new_list2)
