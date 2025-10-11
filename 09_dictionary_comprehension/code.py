# This method prevents complex loops inside dictionaries
# Syntax is the same as List Comprehension when adding Conditionals
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users} # KEY : VALUE
userid_mapping = {user[0]: user for user in users}

print(username_mapping)
print(userid_mapping)