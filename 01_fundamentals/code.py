# ----- Printing -----
greeting = "Hello, {}"
print(greeting.format("World"))

string = "This is the most commonly used"
print(f"{string} formatting")

gpa = 3.97
name = "Sofia"
print(f"My name is {name: >15s}, I have a GPA of {gpa:5.3f}")
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
# round() - Round to the Nearest Whole Number
# math.ceil() - Round Up
# 23 // 7 = 3 - Floor Division: Round Down
# int(8.9) - Casting: Omits Decimal Values
# type(item)