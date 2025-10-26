# Dictionary

fruits = {
    1: "Apple",
    2: "Orange",
    3: "Bananas",
    4: "Pears",
    5: "Grapes"
}

del fruits[3]

def insert_fruit(fruit):
    """Insert new fruit in empty index instead of at the end"""
    keys = [key for key in fruits.keys()]
    if len(fruits) == keys[-1]:
        # Add a new fruit if keys are filled
        fruits[len(fruit)+1] = fruit
    else:
        # Add a new fruit into missing key
        for num in range(len(fruits)+1):
            expected_index = num+1
            if expected_index not in keys:
                fruits[expected_index] = fruit
                break

insert_fruit("Lemons")
insert_fruit("Peaches")

fruits = dict(sorted(fruits.items()))
print(fruits)
