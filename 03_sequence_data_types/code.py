l = ["Apple", "Orange", "Mango"]
t = ("Apple", "Orange", "Mango")
s = {"Apple", "Orange", "Mango"}

# Access
print(l[0])
print(t[0])
# print(s[0]) # No order = No index

# Modify
l.append("Grapes")
s.add("Grapes")
s.add("Grapes") # Ignored
print(s)

# ----- Lists -----
# Extend
l.extend(["Dragonfruit"])
# Get Position
l.index("Dragonfruit")
# Remove Item
removed_last_item = l.pop()
l.remove("Grapes")
# Insert after index
l.insert(1, "Strawberry")
# Sorting Alphabetically
l.sort()

# ----- Sets -----
# set.difference(set)
# set.union(set)
# set.intersection(set)
