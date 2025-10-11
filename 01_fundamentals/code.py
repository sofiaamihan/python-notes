# ----- Printing -----
greeting = "Hello, {}"
print(greeting.format("World."))

string = "This is the most commonly used"
print(f"{string} formatting.")

age = 19.0
name = "Sofia"
print(f"My name is {name: >15s}, I am {age:5.3f} years old.")
# > - Right-Aligned
# 15 - Spacing
# 5.3 - 5 Spacing, 3 Decimal Points
# f - Float Type

select = "This is selective printing. Okay?"
print(select[:27])

# ----- Backslash -----
# \n - Newline
# \r - Reset Curser (Everything before this is omitted)
# \t - Tab
# \ - Ignore Symbols

# ----- Basic Functions -----
# import math
# round() - Round to the Nearest Whole Number
# math.ceil() - Round Up
# math.floor() - Round Down
# 23 // 7 = 3 - Floor Division: Round Down
# int(8.9) - Casting: Omits Decimal Values
# type(item)
# len(var)
# var.lower()
# var.upper()
# var.capitalize() - First Letter
# len()
# var.count("a") - Counts how many times "a" appears

# ----- Variables and Value Assignment -----
# num = 60
# word = "string"
# CONSTANT = "Never changes"
# name: str = "Static Variable"

# ----- Mathematical, Comparison, Logical, and Membership Operations -----
# Comparison or Relational (==, >, <)
# Logical (and, or, not)
# Membership (in, not in)
# Arithmetic (+, -, *, /, %, //, **)
# Assignment (=)

# ----- Randomisation -----
# import random
# random.randint(1, 100) # Any number from 1-100
# random.random()*5 # Any float (0-1 so multiplication is needed)
# random.sample(list, 1) # Suggest a random item from a list
# random.choice(list) # Suggest a random item from a list
# random.shuffle(password) # Shuffle a string

# ----- Splitting, Joining, Replacing Strings -----
# string.split('.') # String is split everytime there's a '.'
# string.split() # String is split after every word
# "".join(list) # Join a list of strings into one string
# string.replace('.', '').lower() # Replaces the fullstops and makes everything lowercase

# ----- End Literals -----
# print("hello world", end='') # Removes the newline at the end
# print("hello","world", sep="--") # Words separated by -- instead of spaces

# ----- Slicing -----
# nums = ["a", "b", "c", "d", "e", "f"]
# nums[2:5] # c-e, exclusive of last index
# nums[:4] # a-d
# nums[::2] # Multiples of 2
# nums[::-1] # Reversed Order