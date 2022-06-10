
# Taking the number input from user.
num = int(input("enter a number\n"))


# defining a function for even odd numbers.
def even_odd():
    global num
    if num % 2 == 0:
        print("Even Number : {}".format(num))
        if 10 <= num <= 99:
            print(f"It is a even two digit number : {num}")
        elif 99 < num <= 999:
            print(f"It is even three digit number : {num}")
        else:
            print(f"It is even single digit number : {num}")
    else:
        print("Odd Number : {}".format(num))


# calling the function
even_odd()
