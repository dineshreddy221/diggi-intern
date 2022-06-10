# for loop
n = int(input("enter a number\n"))
for i in range(0, n+1):
    print(i)

# stored in variable
temp = []
for i in range(0, 10):
    temp.append(i)
print("list of numbers : ", temp)

# Accessing the list items using for loop
lst = ["dinesh", "reddy", 1, 3, 5]
temp_1 = []
for item in range(len(lst)):
    temp_1.append(lst[item])
print("Access list items with for loop : ", temp_1)

# accessing dictionary elements
dit = {"name": "dinesh", "rno": 8}
dit_values = []
for values in dit:
    dit_values.append(dit[values])
print(dit_values)

# while loop
num = int(input("enter a number\n"))
while num < 20:
    print(num)
    num += 1
