# creating a dictionary
dit = {"color": "red", "name": "dinesh", "price": 100, "items": ["shirts", "pants"]}
print(dit)
print(type(dit))

# Accessing the dit elements
dit_1 = dit['name']
print(dit_1)

# using for loop
lst = []
for value in dit:
    lst.append(dit[value])
print(lst)

# Accessing the dit keys
dit_2 = dit.keys()   # we get keys from the dictionary
print(dit_2)

# checking the dictionary values

dit_3 = dit.values()   # we get values from dictionary
print(dit_3)

dit_4 = dit.items()  # we get items in a tuple from dictionary
print(dit_4)