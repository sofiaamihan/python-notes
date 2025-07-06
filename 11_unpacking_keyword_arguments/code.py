# a dictionary is printed
# KEYWORD = KEY (works vic versa)
# PARAMETER = VALUE
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

# Overview of syntax
def overview(*args, **kwargs):
    print(args) # Tuple
    print(kwargs)

overview(1, 3, 5, name = "bob", age=25)

# Practice 1
# Print the keyword arguments nicely
def name(**kwargs):
    return kwargs

def print_nicely(**kwargs):
    # Convert into dictionary
    info = name(**kwargs)
    for key, value in info.items():
        print(f"{key}: {value}")


print_nicely(name="bob", age=25)