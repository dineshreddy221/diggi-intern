# defining the integer
num = 5
print(f"{num} : ", type(num))
print("*"*15)

num_1 = "5"
int_num = int(num_1)  # type casting from string to integer

print(f"before type casting {type(num_1)} : After type casting{type(int_num)}")
print("*"*15)
# taking inputs from user
num_2 = input("enter a number\n")
print(f"{num_2} : ", type(num_2))

print("*"*15)
num_3 = int(input("enter a number\n"))
print(f"{num_3} : ", type(num_3))

