# creating a function
def my_function():
    """reusing this code"""
    return "you are in function"


function = my_function()
print(function)

num_1 = int(input("enter a number\n"))


# global variable
def square():
    global num_1
    return num_1**2


s = square()
print(f"square of {num_1} : ", s)


# local variable
def cubic():
    n = int(input("enter a number\n"))
    return n**3


cubic_n = cubic()
print(f"cubic : ", cubic_n)