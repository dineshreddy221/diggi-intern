# taking a list of values

lst = ['dinesh', "reddy", 1, 23, {23, 34, 45, 56}, [1, 2, 3, 4], {"pencil": 5, "pen": 10}]

print("list : ", lst)
print(type(lst))

# Accessing the list items
lst_1 = lst[0]      # we can access the elements of list by indexing
print(f"{lst_1} type is : ", type(lst_1))

# Accessing set inside a list
lst_2 = lst[4]
print(f"{lst_2} type is : ", type(lst_2))
print("*"*15)

# Accessing the list inside a list
lst_3 = lst[5][3]
print("value : ", lst_3)
print(type(lst_3))
print("*"*15)

# Accessing the dictionary inside a list
lst_4 = lst[6]["pen"]
print(lst_4)
print(type(lst_4))

# methods
lst_5 = lst.append("mountains")
print(lst)

lst.insert(2, "cars")
print(lst)
