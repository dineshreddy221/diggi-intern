# creating a lambda function
num = int(input("enter a number\n"))

# squaring a value using lambda function
square_value = (lambda x: x**2 if x % 2 == 0 else x)
print(f"square values of {num} is :", square_value(num))

cubic_value = (lambda x: x**3)
print(f"cubic value of {num} is : ", cubic_value(num))
