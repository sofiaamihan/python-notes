classes = {
    "Math": "Blue",
    "English": "Red",
    "Physics": "Purple",
    "Biology": "Green",
    "Chemistry": "Orange"
}

for key in classes:
    print(key)
    value = classes[key]
    print(value)

# Output is unique type
list_of_keys = classes.keys()
list_of_values = classes.values()

for key, value in classes.items():
    print(key)
    print(value)