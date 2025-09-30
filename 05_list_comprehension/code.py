# Conditional For-Loops shortened into one line
# Syntax = [new_item for item in list if condition]
# You can apply functions on new_item in the list comprehension
names = ["Abby", "Bob", "Cindy", "Drew"]
friends = [friend for friend in names if friend.startswith("A")]
print(friends)
